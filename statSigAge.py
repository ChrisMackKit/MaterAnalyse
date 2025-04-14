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
    cursor4 = connection.cursor(buffered=True)
    cursor5 = connection.cursor(buffered=True)
    cursor6 = connection.cursor(buffered=True)
    cursor7 = connection.cursor(buffered=True)

 
    age18 = f"SELECT TVS_Score FROM results WHERE Age = '1'"
    cursor.execute(age18)
    age30 = f"SELECT TVS_Score FROM results WHERE Age = '2'"
    cursor2.execute(age30)
    age40 = f"SELECT TVS_Score FROM results WHERE Age = '3'"
    cursor3.execute(age40)
    age50 = f"SELECT TVS_Score FROM results WHERE Age = '4'"
    cursor4.execute(age50)
    age60 = f"SELECT TVS_Score FROM results WHERE Age = '5'"
    cursor5.execute(age60)
    age70 = f"SELECT TVS_Score FROM results WHERE Age = '6'"
    cursor6.execute(age70)
    age80 = f"SELECT TVS_Score FROM results WHERE Age = '7'"
    cursor7.execute(age80)
 
    tvs_score18 = cursor.fetchall()
    score18 = np.array([value[0] for value in tvs_score18 if value[0] is not None])
    tvs_score30 = cursor2.fetchall()
    score30 = np.array([value[0] for value in tvs_score30 if value[0] is not None])
    tvs_score40 = cursor3.fetchall()
    score40 = np.array([value[0] for value in tvs_score40 if value[0] is not None])
    tvs_score50 = cursor4.fetchall()
    score50 = np.array([value[0] for value in tvs_score50 if value[0] is not None])
    tvs_score60 = cursor5.fetchall()
    score60 = np.array([value[0] for value in tvs_score60 if value[0] is not None])
    tvs_score70 = cursor6.fetchall()
    score70 = np.array([value[0] for value in tvs_score70 if value[0] is not None])
    tvs_score80 = cursor7.fetchall()
    score80 = np.array([value[0] for value in tvs_score80 if value[0] is not None])

    # Kruskal-Wallis-Test
    kruskal_wallis = stats.kruskal(score18, score30, score40, score50, score60, score70, score80)

    print('Kruskal-Wallis statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)




finally:
    # Close the cursor and connection
    cursor.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    cursor5.close()
    cursor6.close()
    cursor7.close()
    connection.close()