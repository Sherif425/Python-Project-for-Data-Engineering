# Coursera-IBM-Python-Project-for-Data-Engineering
Coursera-IBM-Python Project for Data Engineering

In this practice project, you will use the skills acquired through the course and create a complete ETL pipeline for accessing data from a website and processing it to meet the requirements.

## Project Scenario
An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.

You can find the required data on this webpage.

The required information needs to be made accessible as a JSON file 'Countries_by_GDP.json' as well as a table 'Countries_by_GDP' in a database file 'World_Economies.db' with attributes 'Country' and 'GDP_USD_billion.'

Your boss wants you to demonstrate the success of this code by running a query on the database table to display only the entries with more than a 100 billion USD economy. Also, log the entire process of execution in a file named 'etl_project_log.txt'.

You must create a Python code 'etl_project_gdp.py' that performs all the required tasks.

### Hands-on Lab: Accessing Databases using Python Script
Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

In this lab, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.

- Objectives
  - In this lab you'll learn how to:

    -- Create a database using Python

    -- Load the data from a CSV file as a table to the database

    -- Run basic "queries" on the database to access the information

- Scenario
    Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :

| Header | Description|
| ------ | ---------- |
|ID	     |Employee ID |
|FNAME	 | First Name | 
|LNAME	 | Last Name  |
|CITY	   |City of residence|
|CCODE	 |Country code (2 letters)|

