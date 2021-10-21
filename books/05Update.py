import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

try:
    bkcd= int(input('Enter the Book Code: '))

    curs.execute("select * from books where bookcode=%d" %bkcd)
    data=curs.fetchall()

    if data:
        rate= int(input('Enter New price of book: '))
        curs.execute("update books set price=%d where bookcode=%d" %(rate,bkcd))
        con.commit()
        print('-'*50)
        print("Price updated sucessfully...")

    else:
        print('-'*50)
        print('Invalid Bookcode entered.......')
        
except:
    print('-'*50)
    print('Enter valid Bookcode or price........')

con.close()
