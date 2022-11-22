import mysql.connector
from datetime import datetime
import sys
from tabulate import tabulate
try:

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='homeautomationdb')
except mysql.connector.Error as e:  
    sys.exit("dbconnection failure")    
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
        try:
            sql="INSERT INTO `senservalues`(`temperature`, `humadity`, `moisture`, `date`) VALUES  (%s,%s,%s,now())"
            data=(temperature,humadity, moisture)
            mycursor.execute(sql,data)
            mydb.commit()
            print("values entared successfully.......!")
        except mysql.connector.Error as e:
            sys.exit("view date error")     
    elif(choice==2):
        print("VIEW ALL VALUES")
        try:
            sql="SELECT `temperature`, `humadity`, `moisture`, `date` FROM `senservalues`"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            for i in result:
                print(i) 
        except mysql.connector.Error as e:
            sys.exit("view date error")         

    elif(choice==3):
        print("SEARCH VALUE BY DATE")
        date=input("enter a date(yy-mm-dd):-")
        try:
            sql="SELECT `temperature`, `humadity`, `moisture` FROM `senservalues` WHERE `date`='"+date+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            #print(result)
            print(tabulate(result,headers=["temperature","humadity","moisture"],tablefmt="psql")) 
        except mysql.connector.Error as e:
            sys.exit("view date error") 
    elif(choice==4):
        break            