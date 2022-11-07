import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='homeautomationdb')
mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print("1. add values")
    print("2.view values")
    print("3. search item by date")
    print("4.exit")
    choice=int(input("enter your choice:-"))
    if(choice==1):
        print("ADD VALUES")
        temperature	=input("enter temperature:::---")
        humadity=input("enter humadity:::---")
        moisture=input("enter moisture:::---")
        date= datetime.today().strftime('%Y-%m-%d')
        sql="INSERT INTO `senservalues`(`temperature`, `humadity`, `moisture`, `date`) VALUES  (%s,%s,%s,now())"
        data=(temperature,humadity, moisture)
        mycursor.execute(sql,data)
        mydb.commit()
        print("values entared successfully.......!")
    elif(choice==2):
        print("VIEW ALL VALUES")
    elif(choice==3):
        print("SEARCH VALUE BY DATE")
    elif(choice==4):
        break            