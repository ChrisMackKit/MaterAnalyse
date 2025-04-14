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

 
    bmd = f"SELECT TVS_Score FROM results WHERE State = 'California' OR State = 'Georgia'"
    cursor.execute(bmd)
    drewvvpat = f"SELECT TVS_Score FROM results WHERE State = 'Ohio' OR State = 'Nevada'"
    cursor2.execute(drewvvpat)
    drewovvpat = f"SELECT TVS_Score FROM results WHERE State = 'Louisiana'"
    cursor3.execute(drewovvpat)
 
    tvs_scoreBMD = cursor.fetchall()
    scoreBMD = np.array([value[0] for value in tvs_scoreBMD if value[0] is not None])
    tvs_scoreDREw = cursor2.fetchall()
    scoreDREw = np.array([value[0] for value in tvs_scoreDREw if value[0] is not None])
    tvs_scoreDREwo = cursor3.fetchall()
    scoreDREwo = np.array([value[0] for value in tvs_scoreDREwo if value[0] is not None])

    # Kruskal-Wallis-Test
    kruskal_wallis = stats.kruskal(scoreBMD, scoreDREw, scoreDREwo)

    print('Kruskal-Wallis statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)



finally:
    # Close the cursor and connection
    cursor.close()
    cursor2.close()
    cursor3.close()
    connection.close()