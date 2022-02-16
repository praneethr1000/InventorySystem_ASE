from LoginFlow.userLogin import *
import pyodbc

def addItem():
    showItems()


def showItems():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-0BSMBQL\SQLEXPRESS;'
                          'Database=praneeth;'
                          'Trusted_Connection=yes;')
    cur = conn.cursor()

    try:
        cur.execute("select * from products")
        data = cur.fetchall()

        headers = [i[0] for i in cur.description]
        print(*headers)

        # print the rows
        for row in data:
            print(*row)

    except Exception as e:
        print(e)
    conn.commit()
    conn.close()


def showItemsLessthanFive():
    pass


def quantityOfItems():
    pass


def wareHouse():
    print("Warehouse deails")
    print("1.Add item to inventory")
    print("2.Show product details")
    print("3.Show products less than or equal to 5")
    print("4.Show quantity of each product by warehouse")
    print("Press any other key to exit to main menu")
    ware_house_input = int(input("Enter the number based on the operation that you want to perform: "))
    if ware_house_input == 1:
        addItem()
    elif ware_house_input == 2:
        showItems()
    elif ware_house_input == 3:
        showItemsLessthanFive()
    elif ware_house_input == 4:
        quantityOfItems()
    else:
        displayMenu()
