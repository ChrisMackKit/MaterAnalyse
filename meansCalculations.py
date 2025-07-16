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
    geo = """
        SELECT count(*) FROM results WHERE State = 'california'
    """
    cursor.execute(geo)
    californiaResults = cursor.fetchall()
    print("Mean of California:", californiaResults)

    '''
    mann_whitney = stats.mannwhitneyu(nonSwingResults, swingResults, alternative='two-sided')
    print("Mann-Whitney U test statistic:", mann_whitney.pvalue)
    mann_whitney_less = stats.mannwhitneyu(nonSwingResults, swingResults, alternative='greater')
    print("Mann-Whitney U test statistic (greater):", mann_whitney_less.pvalue)'''
    '''
    kruskal_wallis = stats.kruskal(nonSwingResults, swingResults, y)
    print("Kruskal-Wallis test statistic:", kruskal_wallis.pvalue)'''

    # Änderungen speichern
    connection.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()