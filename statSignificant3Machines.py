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


    '''    
    bmd = f"SELECT TVS_Score FROM results WHERE State = 'California' OR State = 'Georgia'"
    cursor.execute(bmd)
    drewvvpat = f"SELECT TVS_Score FROM results WHERE State = 'Ohio' OR State = 'Nevada'"
    cursor2.execute(drewvvpat)
    drewovvpat = f"SELECT TVS_Score FROM results WHERE State = 'Louisiana'"
    cursor3.execute(drewovvpat)'''

    dem = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '1'"
    cursor.execute(dem)
    rep = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '2'"
    cursor2.execute(rep)
    ind = f"SELECT TVS_Score FROM results WHERE Political_Leaning = '3'"
    cursor3.execute(ind)
    '''
    tvs_scoreBMD = cursor.fetchall()
    scoreBMD = np.array([value[0] for value in tvs_scoreBMD if value[0] is not None])
    tvs_scoreDREw = cursor2.fetchall()
    scoreDREw = np.array([value[0] for value in tvs_scoreDREw if value[0] is not None])
    tvs_scoreDREwo = cursor3.fetchall()
    scoreDREwo = np.array([value[0] for value in tvs_scoreDREwo if value[0] is not None])'''
    
    tvs_scoreDem = cursor.fetchall()
    scoreDem = np.array([value[0] for value in tvs_scoreDem if value[0] is not None])
    tvs_scoreRep = cursor2.fetchall()
    scoreRep = np.array([value[0] for value in tvs_scoreRep if value[0] is not None])
    tvs_scoreInd = cursor3.fetchall()
    scoreInd = np.array([value[0] for value in tvs_scoreInd if value[0] is not None])

    ergebnisse = {}

    # Mann-Whitney-U-Test
    #mann_whitney = stats.mannwhitneyu(liste1, liste2)

    # Wilcoxon-Vorzeichen-Rang-Test
    #wilcoxon = stats.wilcoxon(liste1, liste2)

    # Kruskal-Wallis-Test
    kruskal_wallis = stats.kruskal(scoreDem, scoreRep, scoreInd)

    # Spearman-Rang-Korrelation
    #spearman_corr = stats.spearmanr(liste1, liste2)

    #print('Mann-Whitney-U statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    #print('Wilcoxon statistic:', wilcoxon.statistic, 'P-value:', wilcoxon.pvalue)
    print('Kruskal-Wallis statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)
    #print('Spearman correlation:', spearman_corr.correlation, 'P-value:', spearman_corr.pvalue)



finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()