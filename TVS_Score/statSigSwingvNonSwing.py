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


    swing = f"SELECT TVS_Score FROM results WHERE State = 'Georgia' OR State = 'Nevada'"
    cursor.execute(swing)
    nonSwing = f"SELECT TVS_Score FROM results WHERE State = 'Ohio' OR State = 'Louisiana' OR State = 'California'"
    cursor2.execute(nonSwing)

    tvs_scoreSwing = cursor.fetchall()
    scoreSwing = np.array([value[0] for value in tvs_scoreSwing if value[0] is not None])
    tvs_scoreNonSwing = cursor2.fetchall()
    scoreNoSwing = np.array([value[0] for value in tvs_scoreNonSwing if value[0] is not None])
    sumSwing = scoreSwing.sum() / scoreSwing.size
    sumNoSwing = scoreNoSwing.sum() / scoreNoSwing.size
    print('Summe Male:', sumSwing, 'Summe Female:', sumNoSwing)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’
    mann_whitney = stats.mannwhitneyu(scoreSwing, scoreNoSwing, alternative='two-sided')
    mann_whitneyGreater = stats.mannwhitneyu(scoreSwing, scoreNoSwing, alternative='greater')
    mann_whitneyLess = stats.mannwhitneyu(scoreSwing, scoreNoSwing, alternative='less')

    print('Mann-Whitney-U statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    print('Mann-Whitney-U statistic greater:', mann_whitneyGreater.statistic, 'P-value:', mann_whitneyGreater.pvalue)
    print('Mann-Whitney-U statistic less:', mann_whitneyLess.statistic, 'P-value:', mann_whitneyLess.pvalue)



finally:
    # Close the cursor and connection
    cursor.close()
    cursor2.close()
    
    connection.close()