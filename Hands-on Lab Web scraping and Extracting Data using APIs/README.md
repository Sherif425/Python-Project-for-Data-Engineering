# Hands-on lab: Web scraping and Extracting Data using APIs


    ** Web scraping is used for extraction of relevant data from web pages. If you require some data from a web page in a public domain, web scraping makes the process of data extraction quite convenient. The use of web scraping, however, requires some basic knowledge of the structure of HTML pages. In this lab, you will learn the process of analyzing the HTML code of a web page and how to extract the required information from it using web scraping in Python.

    **Objectives
        By the end of this lab, you will be able to:

        - Use the requests and BeautifulSoup libraries to extract the contents of a web page

        - Analyze the HTML code of a webpage to find the relevant information

        - Extract the relevant information and save it in the required form

    ** Scenario
    
        Consider that you have been hired by a Multiplex management organization to extract the information of the top 50 movies with the best average rating from the web link shared below.

        https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films



    - The information required is Average Rank, Film, and Year.
    
    - You are required to write a Python script webscraping_movies.py that extracts the information and saves it to a CSV file top_50_films.csv. You are also required to save the same information to a database Movies.db under the table name Top_50.


# Initial steps


    #  You require the following libraries for this lab.

       - pandas library for data storage and manipulation.

       - BeautifulSoup library for interpreting the HTML document.

       - requests library to communicate with the web page.

       - sqlite3 for creating the database instance.

    While requests and sqlite3 come bundled with Python3, you need to install pandas and BeautifulSoup libraries to the IDE.

    - For this, run the following commands in a terminal window.


        python3.11 -m pip install pandas
        python3.11 -m pip install bs4


# Code setup

    To create a Python script, call the relevant libraries and the initializations as a first step.

    ## Importing Libraries
    
        - Import the following four libraries by adding lines of code noted below to your webscraping_movies.pyfile.
    

            import requests
            import sqlite3
            import pandas as pd
            from bs4 import BeautifulSoup

    ## Initialization of known entities
        
        You must declare a few entities at the beginning. For example, you know the required URL, the CSV name for saving the record, the database name, and the table name for storing the record. You also know the entities to be saved. Additionally, since you require only the top 50 results, you will require a loop counter initialized to 0. You may initialize all these by using the following code in webscraping_movies.py:


            url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
            db_name = 'Movies.db'
            table_name = 'Top_50'
            csv_path = '/home/project/top_50_films.csv'
            df = pd.DataFrame(columns=["Average Rank","Film","Year"])
            count = 0



        - Loading the webpage for Webscraping
            
            To access the required information from the web page, you first need to load the entire web page as an HTML document in python using the requests.get().text function and then parse the text in the HTML format using BeautifulSoup to enable extraction of relevant information.

            
        - Add the following code to webscraping_movies.py:

            html_page = requests.get(url).text
            data = BeautifulSoup(html_page, 'html.parser')



            Save your file using Ctrl+S.



            Now, create a new file by the name of webscraping_movies.py in the path /home/project/.

            You will write all of your code in this file.