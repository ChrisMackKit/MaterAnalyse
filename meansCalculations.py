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
    cursor2 = connection.cursor(buffered=True)
    cursor3 = connection.cursor(buffered=True)



    # Spalte mit berechneten Werten füllen
    geo = """
        SELECT Machine_Score_1 FROM results WHERE State = 'Georgia'
    """
    cursor.execute(geo)
    georgiaResults = cursor.fetchall()
    georgiaResults2 = np.array([value[0] for value in georgiaResults if value[0] is not None])
    georgiaResults3 = np.mean(georgiaResults2)

    cali = """
        SELECT Machine_Score_1 FROM results WHERE State = 'California'
    """
    cursor2.execute(cali)
    caliResults = cursor2.fetchall()
    caliResults2 = np.array([value[0] for value in caliResults if value[0] is not None])
    caliResults3 = np.mean(caliResults2)

    bmd = """
        SELECT Machine_Score_1 FROM results WHERE State = 'Nevada'
    """
    cursor.execute(bmd)
    nevadaResults = cursor.fetchall()
    nevadaResults2 = np.array([value[0] for value in nevadaResults if value[0] is not None])
    nevadaResults3 = np.mean(nevadaResults2)

    ohio = """
        SELECT Machine_Score_1 FROM results WHERE State = 'Ohio'
    """
    cursor2.execute(ohio)
    ohioResults = cursor2.fetchall()
    ohioResults2 = np.array([value[0] for value in ohioResults if value[0] is not None])
    ohioResults3 = np.mean(ohioResults2)

    loui = """
        SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana'
    """
    cursor.execute(loui)
    louiResults = cursor.fetchall()
    louiResults2 = np.array([value[0] for value in louiResults if value[0] is not None])
    louiResults3 = np.mean(louiResults2)



    print("Mean of Georgia:", georgiaResults3)
    print("Mean of California:", caliResults3)
    print("Mean of Nevada states:", nevadaResults3)
    print("Mean of Ohio:", ohioResults3)
    print("Mean of Louisiana:", louiResults3)

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
    cursor2.close()
    cursor3.close()
    connection.close()