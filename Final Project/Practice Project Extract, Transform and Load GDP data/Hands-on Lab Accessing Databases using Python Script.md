# Hands-on Lab: Accessing Databases using Python Script

Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

In this lab, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.

## Objectives

In this lab you'll learn how to:

    -> Create a database using Python

    -> Load the data from a CSV file as a table to the database

    -> Run basic "queries" on the database to access the information

## Scenario

Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :

| Header | Description              |
| ------ | ------------------------ |
| ID     | Employee ID              |
| FNAME  | First Name               |
| LNAME  | Last Name                |
| CITY   | City of residence        |
| CCODE  | Country code (2 letters) |
|        |                          |

## Setting Up

    Usually, the database for storing data would be created on a server to which the other team members would have access. For the purpose of this lab, we are going to create the database on a dummy server using SQLite3 library.

    Note: SQLite3 is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. SQLite3 comes bundled with Python and does not require installation.

## Initial steps

    For this lab, you will need a Python file in the project folder. You can name it db_code.py. The process to create the file is shown in the images below.


    Run the following command in the terminal.

        ->> wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv

    The file INSTRUCTOR.csv should now be available in the location /home/project/. You can check its contents by clicking it from the Explorer menu.

    Further, to read the CSV and interact with the database, you'll need the pandas library. This library will first have to be installed in the Cloud IDE framework. For this, run the below mentioned statement in a terminal window.

        ->> python3.11 -m pip install pandas

