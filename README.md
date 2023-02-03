<p align="center">
  <img src=https://i.ibb.co/0FQXjkb/pngegg-1.png width="30%" height="30%">
</p>

<p align="center">
  <a href="https://discord.com/users/528161316033265674">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
  <a href="https://t.me/nyas69">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/contributors/nyas1/library-mangement-python-mysql?color=dark-green&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/nyas1/library-mangement-python-mysql?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/nyas1/library-mangement-python-mysql?style=for-the-badge">
  <img src="https://img.shields.io/github/license/nyas1/library-mangement-python-mysql?style=for-the-badge">
</p>

<h1 align="center">📚LIBRARY MANAGEMENT SYSTEM📚</h1>

## 📋Table Of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [How To Run](https://github.com/nyas1/library-mangement-python-mysql/edit/main/README.md#%EF%B8%8Fhow-to-run)
  * [Configuration](https://github.com/nyas1/library-mangement-python-mysql/edit/main/README.md#%EF%B8%8Fconfiguration)
* [How To Use](#how-to-use)
* [License](#license)
* [Authors](#authors)

## 🔍About the Project 
This is a simple program for managing a library. I wrote this small code in my 12th class as a Computer Science Project🤓.  
It is a python script for creating a library management system using the MySQL database. The script first creates a connection to the MySQL server and checks if a database named 'library' exists. If it doesn't, it creates one. Then, it connects to the 'library' database and checks if the tables 'books', 'issue', and 'submit' exist. If any of them doesn't exist, it creates the table.

Then the script contains several functions to add books, issue books, submit books, delete entries in the books table and display entries in the books, issue, submit table. The script uses the Python mysql connector library to interact with the MySQL database.

The script is just a basic implementation of the library management system and can be improved and expanded upon based on the specific requirements.

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

## 🛫Getting Started

### 🧩Prerequisites
* Install [Python](https://www.python.org/) and [MySQL](https://www.mysql.com/) in your system
* Install mysql-connector-python using pip:
```
pip install mysql-connector-python
```

### 🏃‍♂️How to run
* Clone the repository
* Run the program LibraryManagement.py

### ⚙️Configuration
* You can configure the MySQL connection details in the following lines of code:
```
con=mysql.connect(host="localhost",user="root",passwd="admin",database="library")
```
  You need to replace the `host`, `user` and `passwd` with your MySQL connection details.

## 🤔How to use
* The program has seven functions: addbook(), issuebook(), submitbook(), delbook(), dispbook(), dispbook_issued(), dispbook_submitted()
* Call these functions to add new books, issue books, submit books and delete & display books and records from the library database.

## ⛔Limitations
* This program does not have any authentication mechanism. Hence, anyone who has access to the system can make changes to the library records.

## 🪪License
* Distributed under the MIT License. See [LICENSE](https://github.com/nyas1/library-mangement-python-mysql/blob/main/LICENSE.md) for more information.

## 👨‍💻Authors
* [Nyas](https://github.com/nyas1) - A computer science student
