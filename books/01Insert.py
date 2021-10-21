import mysql.connector

con=mysql.connector.connect(host='bifgay9ntjz57cw7klhf-mysql.services.clever-cloud.com',user='ud7ww9wbjelo9otq',password='EMiSeYWsA4B0eCCkW3ei',database='bifgay9ntjz57cw7klhf')
curs=con.cursor()

try:
    bookcode=int(input("enter bookcode no= "))
    bookname= input("enter bookname name= ")
    category= input("enter category type= ")
    author= input("enter author name= ")
    publication= input("enter publication= ")
    edition= input("enter edition= ")
    price= float(input("enter amount= "))

    curs.execute("insert into books values (%d,'%s','%s','%s','%s','%s',%.2f)" %(bookcode,bookname,category,author,publication,edition,price))
    con.commit()
    print("Book added successfully")

except:
    print("Invalid details.....Book added unsucessful")

con.close()

