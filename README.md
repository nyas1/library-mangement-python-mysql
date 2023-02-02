<p align="center">
  <img src=https://i.ibb.co/0FQXjkb/pngegg-1.png width="20%" height="20%">
</p> 

<h1 align="center">📚LIBRARY MANAGEMENT SYSTEM📚</h1>
 
This is a simple program for managing a library. It includes adding new books to the library, issuing books to members, submitting books by members and deleting books from the library. I wrote this small code in my 12th class as a Computer Science Project🤓.

## 💡Features

* Adds new books to the library
* Issues books to members
* Submits books by members
* Deletes books from the library
* Displays all the books of library
* Displays record of issued and submitted books

## 💻Technologies Used

* 🐍 Python
* 💾 MySQL
* 🔌 mysql-connector-python

## 🧩Prerequisites

* Install python and MySQL in your system
* Install mysql-connector-python using pip:
```
pip install mysql-connector-python
```

## 🏃‍♂️How to run

* Clone the repository
* Run the program LibraryManagement.py

## ⚙️Configuration

* You can configure the MySQL connection details in the following lines of code:
```
con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
```
  You need to replace the `host`, `user` and `passwd` with your MySQL connection details.

## 🤔How to use
* The program has seven functions: addbook(), issuebook(), submitbook(), delbook(), dispbook(), dispbook_issued(), dispbook_submitted()
* Call these functions to add new books, issue books, submit books and delete & display books from the library.

## ⛔Limitations

* This program does not have any authentication mechanism. Hence, anyone who has access to the system can make changes to the library records.
