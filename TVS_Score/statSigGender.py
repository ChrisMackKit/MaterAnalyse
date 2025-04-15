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


    male = f"SELECT TVS_Score FROM results WHERE Gender = '1'"
    cursor.execute(male)
    female = f"SELECT TVS_Score FROM results WHERE Gender = '2'"
    cursor2.execute(female)

    tvs_scoreMale = cursor.fetchall()
    scoreMale = np.array([value[0] for value in tvs_scoreMale if value[0] is not None])
    tvs_scoreFemale = cursor2.fetchall()
    scoreFemale = np.array([value[0] for value in tvs_scoreFemale if value[0] is not None])
    sumMale = scoreMale.sum() / scoreMale.size
    sumFemale = scoreFemale.sum() / scoreFemale.size
    print('Summe Male:', sumMale, 'Summe Female:', sumFemale)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’
    mann_whitney = stats.mannwhitneyu(scoreMale, scoreFemale, alternative='two-sided')
    mann_whitneyGreater = stats.mannwhitneyu(scoreMale, scoreFemale, alternative='greater')
    mann_whitneyLess = stats.mannwhitneyu(scoreMale, scoreFemale, alternative='less')

    # Wilcoxon-Vorzeichen-Rang-Test. lists have to be same length
    #wilcoxon = stats.wilcoxon(scoreMale, scoreFemale, alternative='two-sided')
    #wilcoxonGreater = stats.wilcoxon(scoreMale, scoreFemale, alternative='greater')
    #wilcoxonLess = stats.wilcoxon(scoreMale, scoreFemale, alternative='less')

    # Spearman-Rang-Korrelation. lists have to be same length
    #spearman_corr = stats.spearmanr(scoreMale, scoreFemale, alternative='two-sided')
    #spearman_corrGreater = stats.spearmanr(scoreMale, scoreFemale, alternative='greater')
    #spearman_corrLess = stats.spearmanr(scoreMale, scoreFemale, alternative='less')

    print('Mann-Whitney-U statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    print('Mann-Whitney-U statistic greater:', mann_whitneyGreater.statistic, 'P-value:', mann_whitneyGreater.pvalue)
    print('Mann-Whitney-U statistic less:', mann_whitneyLess.statistic, 'P-value:', mann_whitneyLess.pvalue)
    #print('Wilcoxon statistic:', wilcoxon.statistic, 'P-value:', wilcoxon.pvalue)
    #print('Wilcoxon statistic greater:', wilcoxonGreater.statistic, 'P-value:', wilcoxonGreater.pvalue)
    #print('Wilcoxon statistic less:', wilcoxonLess.statistic, 'P-value:', wilcoxonLess.pvalue)
    #print('Spearman correlation:', spearman_corr.correlation, 'P-value:', spearman_corr.pvalue)
    #print('Spearman correlation greater:', spearman_corrGreater.correlation, 'P-value:', spearman_corrGreater.pvalue)
    #print('Spearman correlation less:', spearman_corrLess.correlation, 'P-value:', spearman_corrLess.pvalue)



finally:
    # Close the cursor and connection
    cursor.close()
    cursor2.close()
    
    connection.close()