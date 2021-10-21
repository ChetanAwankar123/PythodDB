import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()


inp=input('Enter the category of books : ')
curs.execute("select bookname from books where category='%s'" %inp)
data=curs.fetchall()
lst=[]

if data:
    for rec in data:
        lst.append(rec[0])
    print(lst)

else:
    print('-'*100)
    print("Entered Category '%s' not found........" %inp)

con.close()
