#!/usr/bin/env python
# coding: utf-8

#CREATING MYSQL TABLES
import mysql.connector as mysql

con=mysql.connect(host="localhost",user="root",passwd="admin")
cursor=con.cursor()

#Check if the "library" database exists and create if it doesn't
database_check = "SHOW DATABASES LIKE 'library'"
cursor.execute(database_check)
result = cursor.fetchone()
if not result:
    cursor.execute("CREATE DATABASE library")

#Connect to the "library" database
con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
cursor=con.cursor()

#Check if the "books" table exists and create if it doesn't
table_check="SHOW TABLES LIKE 'books'"
cursor.execute(table_check)
result=cursor.fetchone()
if not result:
    cursor.execute('''
        CREATE TABLE books (
            ID INT PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL,
            AUTHOR VARCHAR(255) NOT NULL,
            TOTAL_COPIES INT NOT NULL,
            YEAR INT NOT NULL
        );
    ''')
    print("Created Table books Successfully!")

#Check if the "issue" table exists and create if it doesn't
table_check="SHOW TABLES LIKE 'issue'"
cursor.execute(table_check)
result=cursor.fetchone()
if not result:
    cursor.execute('''
        CREATE TABLE issue (
            NAME VARCHAR(255) NOT NULL,
            REG_NO INT NOT NULL PRIMARY KEY,
            ID INT NOT NULL,
            DATE DATE NOT NULL
        );
    ''')
    print("Created Table issue Successfully!")

#Check if the "submit" table exists and create if it doesn't
table_check="SHOW TABLES LIKE 'submit'"
cursor.execute(table_check)
result=cursor.fetchone()
if not result:
    cursor.execute('''
        CREATE TABLE submit (
            NAME VARCHAR(255) NOT NULL,
            REG_NO INT NOT NULL PRIMARY KEY,
            ID INT NOT NULL,
            DATE DATE NOT NULL
        );
    ''')
    print("Created Table submit Successfully!")
    
con.commit()
con.close()

#MAIN PROGRAM
import mysql.connector as mysql

#For adding new books
def addbook(): 
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    id=int(input("Enter Book ID:"))
    bn=input("Enter Book Name:")
    a=input("Enter Author Name:")
    t=int(input("Total Books:"))
    s=int(input("Enter Year:"))
    data=(id,bn,a,t,s)
    sql="insert into books values(%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Book Added Successfully!")

#For issueing books
def issuebook(): 
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    n=input("Enter Name:")
    r=int(input("Enter Reg No:"))
    id=int(input("Enter Book ID:"))
    d=input("Enter Date:")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,id,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book issued by: ",n)

#For submitting books    
def submitbook(): 
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    n=input("Enter Name:")
    r=int(input("Enter Reg No:"))
    id=int(input("Enter Book ID:"))
    d=input("Enter Date:")
    a="insert into submit values(%s,%s,%s,%s)"
    data=(n,r,id,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book Submitted from: ",n)
    
#For deleting entries
def delbook():
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    ac=input("Enter Book Code:")
    a="select * from books where id=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
        a="delete from books where id=%s"
        c.execute(a,data)
        con.commit()
        print("deleted successfully")
    else:
        print("no such book available")
    con.close()
    
#For displaying all entries
def dispbook(): 
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    if not myresult:
        print("No books found in the table.")
    else:
        for i in myresult:
            print("Book ID:",i[0])
            print("Book Name:",i[1])
            print("Author Name:",i[2])
            print("Total Books:",i[3])
            print("Year:",i[4])
            print(">>---------------------------------------------------------------<<")
            
#For displaying issued books
def dispbook_issued():
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    a="select * from issue;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Name:",i[0])
        print("Reg No.:",i[1])
        print("Book ID:",i[2])
        print("Date:",i[3])
        print(">>---------------------------------------------------------------<<")
        
#For displaying submitted (returned) books
def dispbook_submitted():
    con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
    a="select * from submit;" 
    c=con.cursor() 
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Name:",i[0])
        print("Reg No.:",i[1])
        print("Book ID:",i[2])
        print("Date:",i[3])
        print(">>---------------------------------------------------------------<<")
        
#Main function for accessing menu  
def main():
    while True:
        print(""">>>  L I B R A R Y   M A N A G E R   P R O G R A M  <<<
        
>> M A I N  M E N U <<

1.ADD BOOK 
2.ISSUE BOOK
3.SUBMIT BOOK
4.DELETE BOOK 
5.DISPLAY BOOKS
6.DISPLAY ISSUED BOOKS
7.DISPLAY SUBMITTED BOOKS
8.EXIT""")
        choice=input("Enter Task No:")
        print (">>---------------------------------------------------------------<<")
        if(choice=='1'):
            addbook()
        elif(choice=='2'):
            issuebook()
        elif(choice=='3'):
            submitbook()
        elif(choice=='4'):
            delbook()
        elif(choice=='5'):
            dispbook()
        elif(choice=='6'):
            dispbook_issued()
        elif(choice=='7'):
            dispbook_submitted()     
        elif(choice=='8'):
            print("Exiting program.")
            exit()
        else:
            print("Wrong choice...")
        cont=input("Do you want to continue? (y/n)")
        if cont.lower()=="n":
            print("Thank You For Using Library Manager. Exiting Program..")
            break
main()
