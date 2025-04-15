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
        ADD Machine_Score_1 FLOAT;
        UPDATE results
        SET Machine_Score_1 = Overall_Trust + Cast_Ballot + Transparency + Sys_Security + Usability + Accurately_Counted + Accuracy
    """
    cursor.execute(sql_update)
    # Änderungen speichern
    connection.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()