import getpass
import mysql.connector
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Prompt the user for the MySQL password
password = getpass.getpass("Enter your MySQL password: ")
value = "Overall_Trust"

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="trustinvoting"
)

def commaChange(array):
    for i in array:
        i = i.replace(",", ".")


try:
    # Create a cursor object to interact with the database
    cursor = connection.cursor(buffered=True)

    def get_val():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {value}, DB_ID FROM new_values"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([(value[0], value[1]) for value in buff if value[0] is not None])
        cursor.close()
        return array

    # Spalte mit berechneten Werten füllen
    def update_new(array):
        array = np.array([(i[0].replace(",", "."), i[1]) for i in array])

        for i in array:
            cursor = connection.cursor(buffered=True)
            
            sql_update = f"""
                UPDATE new_values
                SET {value} = {i[0]} WHERE DB_ID = {i[1]};
            """
            cursor.execute(sql_update)
            # Änderungen speichern
            cursor.close()
        connection.commit()
    update_new(get_val())

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()

