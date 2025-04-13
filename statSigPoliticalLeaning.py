import getpass
import mysql.connector
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scikit_posthocs as sp

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

    dem = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '1'"
    cursor.execute(dem)
    rep = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '2'"
    cursor2.execute(rep)
    ind = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '3'"
    cursor3.execute(ind)

    tvs_scoreDem = cursor.fetchall()
    scoreDem = np.array([value[0] for value in tvs_scoreDem if value[0] is not None])
    tvs_scoreRep = cursor2.fetchall()
    scoreRep = np.array([value[0] for value in tvs_scoreRep if value[0] is not None])
    tvs_scoreInd = cursor3.fetchall()
    scoreInd = np.array([value[0] for value in tvs_scoreInd if value[0] is not None])


    kruskal_wallis = stats.kruskal(scoreDem, scoreRep, scoreInd)

    print('Kruskal-Wallis statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)

    #post hob test mit Dunn Test
    dunn = sp.posthoc_dunn([scoreDem, scoreRep, scoreInd], p_adjust='bonferroni')
    print(dunn)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’
    mann_whitney = stats.mannwhitneyu(scoreDem, scoreRep, alternative='two-sided')
    mann_whitneyGreater = stats.mannwhitneyu(scoreDem, scoreRep, alternative='greater')
    mann_whitneyLess = stats.mannwhitneyu(scoreDem, scoreRep, alternative='less')
    mann_whitney2 = stats.mannwhitneyu(scoreDem, scoreInd, alternative='two-sided')
    mann_whitneyGreater2 = stats.mannwhitneyu(scoreDem, scoreInd, alternative='greater')
    mann_whitneyLess2 = stats.mannwhitneyu(scoreDem, scoreInd, alternative='less')
    mann_whitney3 = stats.mannwhitneyu(scoreRep, scoreInd, alternative='two-sided')
    mann_whitneyGreater3 = stats.mannwhitneyu(scoreRep, scoreInd, alternative='greater')
    mann_whitneyLess3 = stats.mannwhitneyu(scoreRep, scoreInd, alternative='less')

    print('Mann-Whitney-U Dem v Rep statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    print('Mann-Whitney-U Dem v Rep statistic greater:', mann_whitneyGreater.statistic, 'P-value:', mann_whitneyGreater.pvalue)
    print('Mann-Whitney-U Dem v Rep statistic less:', mann_whitneyLess.statistic, 'P-value:', mann_whitneyLess.pvalue)
    print('Mann-Whitney-U dem v ind statistic:', mann_whitney2.statistic, 'P-value:', mann_whitney2.pvalue)
    print('Mann-Whitney-U dem v ind statistic greater:', mann_whitneyGreater2.statistic, 'P-value:', mann_whitneyGreater2.pvalue)
    print('Mann-Whitney-U dem v ind statistic less:', mann_whitneyLess2.statistic, 'P-value:', mann_whitneyLess2.pvalue)
    print('Mann-Whitney-U rep v ind statistic:', mann_whitney3.statistic, 'P-value:', mann_whitney3.pvalue)
    print('Mann-Whitney-U rep v ind statistic greater:', mann_whitneyGreater3.statistic, 'P-value:', mann_whitneyGreater3.pvalue)
    print('Mann-Whitney-U rep v ind statistic less:', mann_whitneyLess3.statistic, 'P-value:', mann_whitneyLess3.pvalue)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()