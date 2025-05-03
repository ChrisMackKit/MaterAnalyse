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
        ADD Reliability FLOAT;
        UPDATE results
        SET Reliability = (System_Reliability_Always_Works + System_Reliability_Dependable + System_Reliability_Never_Fails + System_Reliability_Reliable) /4;
    """
    cursor.execute(sql_update)
    # Änderungen speichern
    connection.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()