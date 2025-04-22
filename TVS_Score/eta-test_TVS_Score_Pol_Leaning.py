import getpass
import mysql.connector
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pingouin as pg

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

 
    bmd = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '1'"
    cursor.execute(bmd)
    drewvvpat = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '2'"
    cursor2.execute(drewvvpat)
    drewovvpat = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '3'"
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

#Kruskal Value
h = kruskal_wallis.statistic
k = 3
n = scoreBMD.size + scoreDREw.size + scoreDREwo.size


eta_outcome = (h-k+1)/(n-k)
eta_alt = h/(n-1)
eta_outcome = eta_outcome * 100
eta_alt = eta_alt * 100
print(eta_outcome)
print(eta_alt)