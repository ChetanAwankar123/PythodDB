import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

cod=int(input("enter Books Code: "))
curs.execute('select bookname,category,author,publication,edition,price from books where bookcode=%d'%cod)
data=curs.fetchone()

print("-"*50)
try:
    print('Bookname    :',data[0])
    print('category    :',data[1])
    print('author      :',data[2])
    print('publication :',data[3])
    print('edition     :',data[4])
    print('price       :',data[5])

except:
    print('Record not found.........')

con.close()