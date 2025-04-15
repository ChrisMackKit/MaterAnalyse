import getpass
import mysql.connector
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Prompt the user for the MySQL password
password = getpass.getpass("Enter your MySQL password: ")

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="trustinvoting"
)

try:
    # Create a cursor object to interact with the database
    cursor = connection.cursor(buffered=True)



    # Spalte mit berechneten Werten füllen
    sql_update = """
        ALTER TABLE results
        ADD Overall_Trust FLOAT;
        UPDATE results
        SET Overall_Trust = (Overall_Trust_Voting_Method + Overall_Trust_Voting_System_Trustworthy + Overall_Trust_No_Reason_To_Distrust + Overall_Trust_Overall_High) /4
    """


    cursor.execute(sql_update)

    # Änderungen speichern
    connection.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()