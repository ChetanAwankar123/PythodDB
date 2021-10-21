import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

curs.execute('select * from books')
data=curs.fetchall()
lst=[]

for rec in data:
    lst.append(rec[1])

print(lst)

con.close()