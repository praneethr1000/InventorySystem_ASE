from LoginFlow.userLogin import *
from datetime import datetime

def generateInvoice():
    customer_id = int(input('Please enter customer ID'))
    connection = getConnection()
    cursor = connection.cursor()

    try: 
        cursor.execute(f"select * from customerDetails where custmerID = {customer_id};")
        result = list(cursor.fetchall)[0]
        if not result:
            print('Customer has not registered yet. Please register before generating an invice')
            return
        else:
            cursor.execute('select max(id) from invoiceDetails')
            if cursor.fetchone():
                max_id = int(cursor.fetchone()[0])+1
            else:
                max_id = 1
            name = result[1]
            zip = result[2]
            tax_rate = result[3]
            email = result[4]
            item_name = input('Enter the name of the item purchased: ')
            selling_price = int(input('Enter selling price of the item: '))
            delivery_charges = input('Enter delivery charges if applicable. Else enter 0: ')
            total_price = selling_price+delivery_charges+((tax_rate/100)*selling_price)
            date = datetime.today().strftime('%m-%d-%Y')
            query = f'insert into invoiceDetails values ({max_id},{name},{zip},{email},{tax_rate},{item_name},{selling_price},{delivery_charges},{total_price});'
            cursor.execute(query)
            cursor.commit()
            print('Invoice has been generated successfully')
    except Exception as e:
        print(f'Invoice generating failed with exception: {e}.')
        connection.close()

def payInstallment():
    invoice_id = int(input('Enter invoice Id: '))
    try:
        connection = getConnection()
        cursor = connection.cursor()
        query = f'select totalPrice from invoiceDetails where id = {invoice_id};'
        cursor.execute(query)
        total_price = cursor.fetchone()[0]
        installment_amount = int(input('Enter installment amount: '))
        balance = total_price - installment_amount
        if balance>0:
            query = f'update invoiceDetails set totalPrice = {balance} where id = {invoice_id};'
            cursor.execute(query)
            cursor.commit()
        else:
            closeInvoice()
        connection.close()
    except Exception as e:
        print(f'Payment process failed with exeption:{e}')

def closeInvoice():
    invoice_id = int(input('Enter invoice Id: '))
    try:
        connection = getConnection()
        cursor = connection.cursor()
        query = f'delete from invoieDetails where id = {invoice_id};'
        cursor.execute(query)
        cursor.commit()
        connection.close()
    except Exception as e:
        print(f'Failed closing invoice with exception: {e}')

def showOpenInvoices():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        query = f'select * from invoiceDetails order by date;'
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        connection.close()
    except Exception as e:
        print(f'Failed fetching invoices with exception: {e}')

def showClosedInvoices():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        query = f'select * from invoiceDetails order by totalPrice desc;'
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        connection.close()
    except Exception as e:
        print(f'Failed fetching invoices with exception: {e}')
            
def displayMenu():
    print('Welcme to Sales and Invoices module.')
    print('1. Generate an invoice')
    print('2. Pay an installment')
    print('3. Close an invoice')
    print('4. Show open invoices')
    print('5. Show closed invoices')
    print('6. Quit')
    
    option = int(input('Select an option from the abve menu'))
    
    if option == 1:
        generateInvoice()
    elif option == 2:
        payInstallment()
    elif option == 3:
        closeInvoice()
    elif option == 4:
        showOpenInvoices()
    elif option == 5:
        showClosedInvoices()
    else:
        return "exit"
    return "exit"

def salesDetails():
    print("Sales and Invoices")



