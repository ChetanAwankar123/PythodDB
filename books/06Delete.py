import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

try:
    cod=int(input("enter Books Code: "))
    curs.execute('select * from books where bookcode=%d' %cod)
    data=curs.fetchall()

    if data:
        print(data)
        cho=input('Do you want to delete book (Yes/No): ')

        if cho.upper()=='YES':
            curs.execute('delete from books where bookcode=%d' %cod)
            con.commit()

            print('Account deleted sucessfully')

        else:
            print('Thanks for using python')

    else:
        print('Entered Bookcode is not found.......')

    

except:
        print('Enter valid details')

con.close()


