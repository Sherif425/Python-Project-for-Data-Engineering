# Hands-on Lab: Accessing Databases using Python Script


    Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

    In this lab, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.

## Objectives
        In this lab you'll learn how to:

            - Create a database using Python

            - Load the data from a CSV file as a table to the database

            - Run basic "queries" on the database to access the information

## Scenario
    Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :

        Header	Description
        ID	Employee ID
        FNAME	First Name
        LNAME	Last Name
        CITY	City of residence
        CCODE	Country code (2 letters)

## Setting Up
    Usually, the database for storing data would be created on a server to which the other team members would have access. For the purpose of this lab, we are going to create the database on a dummy server using SQLite3 library.

    Note: SQLite3 is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. SQLite3 comes bundled with Python and does not require installation.

## Initial steps
    For this lab, you will need a Python file in the project folder. You can name it db_code.py. The process to create the file is shown in the images below.

    In the File menu, click the option New File.
    File menu with New File highlighted.
    This should open an Untitled file in the editor tab.

    New untitled file.
    Use Ctlr+S to save the file. 

    The Save As interface would pop up. Navigate to the path /home/project/ as shown in the image below and name the file db_code.py. 
    

    File path highlighted in left pane with file title and Save button highlighted.
    You also need the CSV data to be available in the same location /home/project/. For this, open a new terminal from the Terminal tab in the menu as shown below.

    Terminal menu with New Terminal highlighted.
    Run the following command in the terminal. Make sure the current directory in the terminal window is /home/project/.

        wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv


## Python Scripting: Create and Load the table
    
    To create a table in the database, you first need to have the attributes of the required table. Attributes are columns of the table. Along with their names, the knowledge of their data types are also required. The attributes for the required tables in this lab were shared in the Lab Scenario.

    - Add the following statements to db_code.py to feed the required table name and attribute details for the table.


        table_name = 'INSTRUCTOR'
        attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']


        Note: This information can be updated for the case of any other kind of table.

    Save the file using Ctrl+S.

    - Reading the CSV file
    
    Now, to read the CSV using Pandas, you use the read_csv() function. Since this CSV does not contain headers, you can use the keys of the attribute_dict dictionary as a list to assign headers to the data. For this, add the commands below to db_code.py.

        file_path = '/home/project/INSTRUCTOR.csv'
        df = pd.read_csv(file_path, names = attribute_list)

    - Loading the data to a table
    
    The pandas library provides easy loading of its dataframes directly to the database. For this, you may use the to_sql() method of the dataframe object.

    However, while you load the data for creating the table, you need to be careful if a table with the same name already exists in the database. If so, and it isn't required anymore, the tables should be replaced with the one you are loading here. You may also need to append some information to an existing table. For this purpose, to_sql() function uses the argument if_exists. The possible usage of if_exists is tabulated below.

    - Argument usage	Description
        if_exists = 'fail'	Default. The command doesn't work if a table with the same name exists in the database.
        if_exists = 'replace'	The command replaces the existing table in the database with the same name.
        if_exists = 'append'	The command appends the new data to the existing table with the same name.

    As you need to create a fresh table upon execution, add the following commands to the code. The print command is optional, but helps identify the completion of the steps of code until this point.


        df.to_sql(table_name, conn, if_exists = 'replace', index =False)
        print('Table is ready')

        Save the file using Ctrl+S.

    The file INSTRUCTOR.csv should now be available in the location /home/project/. You can check its contents by clicking it from the Explorer menu.

    Terminal file panel with the INSTRUCTOR.csv file highlighted.

    Further, to read the CSV and interact with the database, you'll need the pandas library. This library will first have to be installed in the Cloud IDE framework. For this, run the below mentioned statement in a terminal window.
    