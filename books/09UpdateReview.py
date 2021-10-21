import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

try:
    bkcd= int(input('Enter the Book Code : '))

    curs.execute("select * from books where bookcode=%d" %bkcd)
    data=curs.fetchall()

    if data:
        review= input('Write a Review : ')
        curs.execute("update books set review='%s' where bookcode=%d" %(review,bkcd))
        con.commit()
        print('-'*50)
        print("Review updated sucessfully......")

    else:
        print('-'*50)
        print('Invalid Bookcode entered........')
        
except:
    print('-'*50)
    print('Error Please try again later.......')

con.close() 
