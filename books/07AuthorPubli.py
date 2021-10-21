import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

ath= input('Enter name of Author :')
publi= input('Enter Publication  :')
lst=[]

try:
    curs.execute("select bookname from books where author='%s' and publication='%s'" %(ath,publi))
    data=curs.fetchall()

    for rec in data:
        lst.append(rec[0])

    print(lst)
except:
    print("No Records of Author or Publisher is found..........")


con.close()