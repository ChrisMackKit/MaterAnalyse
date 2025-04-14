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
    cursor4 = connection.cursor(buffered=True)
    cursor5 = connection.cursor(buffered=True)

 
    bmd = f"SELECT TVS_Score FROM results WHERE State = 'California'"
    cursor.execute(bmd)
    drewvvpat = f"SELECT TVS_Score FROM results WHERE State = 'Ohio'"
    cursor2.execute(drewvvpat)
    drewovvpat = f"SELECT TVS_Score FROM results WHERE State = 'Louisiana'"
    cursor3.execute(drewovvpat)
    drewNevada = f"SELECT TVS_Score FROM results WHERE State = 'Nevada'"
    cursor4.execute(drewNevada)
    bmdGeorgia = f"SELECT TVS_Score FROM results WHERE State = 'Georgia'"
    cursor5.execute(bmdGeorgia)
 
    tvs_scoreBMD = cursor.fetchall()
    scoreBMD = np.array([value[0] for value in tvs_scoreBMD if value[0] is not None])
    tvs_scoreDREw = cursor2.fetchall()
    scoreDREw = np.array([value[0] for value in tvs_scoreDREw if value[0] is not None])
    tvs_scoreDREwo = cursor3.fetchall()
    scoreDREwo = np.array([value[0] for value in tvs_scoreDREwo if value[0] is not None])
    tvs_scoreNevada = cursor4.fetchall()
    scoreNevada = np.array([value[0] for value in tvs_scoreNevada if value[0] is not None])
    tvs_scoreGeorgia = cursor5.fetchall()
    scoreGeorgia = np.array([value[0] for value in tvs_scoreGeorgia if value[0] is not None])

    # Kruskal-Wallis-Test
    kruskal_wallis = stats.kruskal(scoreBMD, scoreDREw, scoreDREwo, scoreNevada, scoreGeorgia)

    print('Kruskal-Wallis statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)

    # Post hoc test (Dunn's test)
    dunn = sp.posthoc_dunn([scoreBMD, scoreDREw, scoreDREwo, scoreNevada, scoreGeorgia], p_adjust='bonferroni')
    print(dunn)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’
    mann_whitney = stats.mannwhitneyu(scoreBMD, scoreDREw, alternative='two-sided')
    mann_whitneyGreater = stats.mannwhitneyu(scoreBMD, scoreDREw, alternative='greater')
    mann_whitneyLess = stats.mannwhitneyu(scoreBMD, scoreDREw, alternative='less')
    mann_whitney2 = stats.mannwhitneyu(scoreBMD, scoreDREwo, alternative='two-sided')
    mann_whitneyGreater2 = stats.mannwhitneyu(scoreBMD, scoreDREwo, alternative='greater')  
    mann_whitneyLess2 = stats.mannwhitneyu(scoreBMD, scoreDREwo, alternative='less')
    mann_whitney3 = stats.mannwhitneyu(scoreBMD, scoreNevada, alternative='two-sided')
    mann_whitneyGreater3 = stats.mannwhitneyu(scoreBMD, scoreNevada, alternative='greater')
    mann_whitneyLess3 = stats.mannwhitneyu(scoreBMD, scoreNevada, alternative='less')
    mann_whitney4 = stats.mannwhitneyu(scoreBMD, scoreGeorgia, alternative='two-sided')
    mann_whitneyGreater4 = stats.mannwhitneyu(scoreBMD, scoreGeorgia, alternative='greater')
    mann_whitneyLess4 = stats.mannwhitneyu(scoreBMD, scoreGeorgia, alternative='less')

    mann_whitney5 = stats.mannwhitneyu(scoreDREw, scoreDREwo, alternative='two-sided')
    mann_whitneyGreater5 = stats.mannwhitneyu(scoreDREw, scoreDREwo, alternative='greater')
    mann_whitneyLess5 = stats.mannwhitneyu(scoreDREw, scoreDREwo, alternative='less')
    mann_whitney6 = stats.mannwhitneyu(scoreDREw, scoreNevada, alternative='two-sided')
    mann_whitneyGreater6 = stats.mannwhitneyu(scoreDREw, scoreNevada, alternative='greater')
    mann_whitneyLess6 = stats.mannwhitneyu(scoreDREw, scoreNevada, alternative='less')
    mann_whitney7 = stats.mannwhitneyu(scoreDREw, scoreGeorgia, alternative='two-sided')
    mann_whitneyGreater7 = stats.mannwhitneyu(scoreDREw, scoreGeorgia, alternative='greater')
    mann_whitneyLess7 = stats.mannwhitneyu(scoreDREw, scoreGeorgia, alternative='less')

    mann_whitney8 = stats.mannwhitneyu(scoreDREwo, scoreNevada, alternative='two-sided')
    mann_whitneyGreater8 = stats.mannwhitneyu(scoreDREwo, scoreNevada, alternative='greater')
    mann_whitneyLess8 = stats.mannwhitneyu(scoreDREwo, scoreNevada, alternative='less')
    mann_whitney9 = stats.mannwhitneyu(scoreDREwo, scoreGeorgia, alternative='two-sided')
    mann_whitneyGreater9 = stats.mannwhitneyu(scoreDREwo, scoreGeorgia, alternative='greater')
    mann_whitneyLess9 = stats.mannwhitneyu(scoreDREwo, scoreGeorgia, alternative='less')

    mann_whitney10 = stats.mannwhitneyu(scoreNevada, scoreGeorgia, alternative='two-sided')
    mann_whitneyGreater10 = stats.mannwhitneyu(scoreNevada, scoreGeorgia, alternative='greater')
    mann_whitneyLess10 = stats.mannwhitneyu(scoreNevada, scoreGeorgia, alternative='less')

    print('Mann-Whitney-U BMD v DREw statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    print('Mann-Whitney-U BMD v DREw statistic greater:', mann_whitneyGreater.statistic, 'P-value:', mann_whitneyGreater.pvalue)
    print('Mann-Whitney-U BMD v DREw statistic less:', mann_whitneyLess.statistic, 'P-value:', mann_whitneyLess.pvalue)
    print('Mann-Whitney-U BMD v DREwo statistic:', mann_whitney2.statistic, 'P-value:', mann_whitney2.pvalue)
    print('Mann-Whitney-U BMD v DREwo statistic greater:', mann_whitneyGreater2.statistic, 'P-value:', mann_whitneyGreater2.pvalue)
    print('Mann-Whitney-U BMD v DREwo statistic less:', mann_whitneyLess2.statistic, 'P-value:', mann_whitneyLess2.pvalue)
    print('Mann-Whitney-U BMD v Nevada statistic:', mann_whitney3.statistic, 'P-value:', mann_whitney3.pvalue)
    print('Mann-Whitney-U BMD v Nevada statistic greater:', mann_whitneyGreater3.statistic, 'P-value:', mann_whitneyGreater3.pvalue)
    print('Mann-Whitney-U BMD v Nevada statistic less:', mann_whitneyLess3.statistic, 'P-value:', mann_whitneyLess3.pvalue)
    print('Mann-Whitney-U BMD v Georgia statistic:', mann_whitney4.statistic, 'P-value:', mann_whitney4.pvalue)
    print('Mann-Whitney-U BMD v Georgia statistic greater:', mann_whitneyGreater4.statistic, 'P-value:', mann_whitneyGreater4.pvalue)
    print('Mann-Whitney-U BMD v Georgia statistic less:', mann_whitneyLess4.statistic, 'P-value:', mann_whitneyLess4.pvalue)
    
    print('Mann-Whitney-U DREw v DREwo statistic:', mann_whitney5.statistic, 'P-value:', mann_whitney5.pvalue)
    print('Mann-Whitney-U DREw v DREwo statistic greater:', mann_whitneyGreater5.statistic, 'P-value:', mann_whitneyGreater5.pvalue)
    print('Mann-Whitney-U DREw v DREwo statistic less:', mann_whitneyLess5.statistic, 'P-value:', mann_whitneyLess5.pvalue)
    print('Mann-Whitney-U DREw v Nevada statistic:', mann_whitney6.statistic, 'P-value:', mann_whitney6.pvalue)
    print('Mann-Whitney-U DREw v Nevada statistic greater:', mann_whitneyGreater6.statistic, 'P-value:', mann_whitneyGreater6.pvalue)
    print('Mann-Whitney-U DREw v Nevada statistic less:', mann_whitneyLess6.statistic, 'P-value:', mann_whitneyLess6.pvalue)
    print('Mann-Whitney-U DREw v Georgia statistic:', mann_whitney7.statistic, 'P-value:', mann_whitney7.pvalue)
    print('Mann-Whitney-U DREw v Georgia statistic greater:', mann_whitneyGreater7.statistic, 'P-value:', mann_whitneyGreater7.pvalue)
    print('Mann-Whitney-U DREw v Georgia statistic less:', mann_whitneyLess7.statistic, 'P-value:', mann_whitneyLess7.pvalue)

    print('Mann-Whitney-U DREwo v Nevada statistic:', mann_whitney8.statistic, 'P-value:', mann_whitney8.pvalue)
    print('Mann-Whitney-U DREwo v Nevada statistic greater:', mann_whitneyGreater8.statistic, 'P-value:', mann_whitneyGreater8.pvalue)
    print('Mann-Whitney-U DREwo v Nevada statistic less:', mann_whitneyLess8.statistic, 'P-value:', mann_whitneyLess8.pvalue)
    print('Mann-Whitney-U DREwo v Georgia statistic:', mann_whitney9.statistic, 'P-value:', mann_whitney9.pvalue)
    print('Mann-Whitney-U DREwo v Georgia statistic greater:', mann_whitneyGreater9.statistic, 'P-value:', mann_whitneyGreater9.pvalue)
    print('Mann-Whitney-U DREwo v Georgia statistic less:', mann_whitneyLess9.statistic, 'P-value:', mann_whitneyLess9.pvalue)

    print('Mann-Whitney-U Nevada v Georgia statistic:', mann_whitney10.statistic, 'P-value:', mann_whitney10.pvalue)
    print('Mann-Whitney-U Nevada v Georgia statistic greater:', mann_whitneyGreater10.statistic, 'P-value:', mann_whitneyGreater10.pvalue)
    print('Mann-Whitney-U Nevada v Georgia statistic less:', mann_whitneyLess10.statistic, 'P-value:', mann_whitneyLess10.pvalue)





finally:
    # Close the cursor and connection
    cursor.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    cursor5.close()
    
    connection.close()