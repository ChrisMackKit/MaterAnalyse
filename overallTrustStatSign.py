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
    cursorBMD = connection.cursor(buffered=True)
    cursorDREw = connection.cursor(buffered=True)
    cursorDREwo = connection.cursor(buffered=True)
    cursorGeorgia = connection.cursor(buffered=True)
    cursorOhio = connection.cursor(buffered=True)
    cursorCalifornia = connection.cursor(buffered=True)
    cursorNevada = connection.cursor(buffered=True)
    cursorLouisiana = connection.cursor(buffered=True)
    cursorMale = connection.cursor(buffered=True)
    cursorFemale = connection.cursor(buffered=True)
    cursorDemocrat = connection.cursor(buffered=True)
    cursorRepublican = connection.cursor(buffered=True)
    cursorIndependent = connection.cursor(buffered=True)
    cursorSwing = connection.cursor(buffered=True)
    cursorNoSwing = connection.cursor(buffered=True)
    cursor18 = connection.cursor(buffered=True)
    cursor30 = connection.cursor(buffered=True)
    cursor40 = connection.cursor(buffered=True)
    cursor50 = connection.cursor(buffered=True)
    cursor60 = connection.cursor(buffered=True)
    cursor70 = connection.cursor(buffered=True)
    cursor80 = connection.cursor(buffered=True)



    BMD = f"SELECT Overall_Trust FROM results WHERE State = 'Georgia' OR State = 'California'"
    cursorBMD.execute(BMD)
    DREw = f"SELECT Overall_Trust FROM results WHERE State = 'Ohio' OR State = 'Nevada'"
    cursorDREw.execute(DREw)
    DREwo = f"SELECT Overall_Trust FROM results WHERE State = 'Louisiana'"
    cursorDREwo.execute(DREwo)
    Georgia = f"SELECT Overall_Trust FROM results WHERE State = 'Georgia'"
    cursorGeorgia.execute(Georgia) 
    Ohio = f"SELECT Overall_Trust FROM results WHERE State = 'Ohio'"
    cursorOhio.execute(Ohio)
    California = f"SELECT Overall_Trust FROM results WHERE State = 'California'"
    cursorCalifornia.execute(California)
    Nevada = f"SELECT Overall_Trust FROM results WHERE State = 'Nevada'"
    cursorNevada.execute(Nevada)
    Louisiana = f"SELECT Overall_Trust FROM results WHERE State = 'Louisiana'"
    cursorLouisiana.execute(Louisiana)
    Male = f"SELECT Overall_Trust FROM results WHERE Gender = '1'"
    cursorMale.execute(Male)
    Female = f"SELECT Overall_Trust FROM results WHERE Gender = '2'"
    cursorFemale.execute(Female)
    Democrat = f"SELECT Overall_Trust FROM results WHERE Political_Leaning = 'Democrat'"
    cursorDemocrat.execute(Democrat)
    Republican = f"SELECT Overall_Trust FROM results WHERE Political_Leaning = 'Republican'"
    cursorRepublican.execute(Republican)
    Independent = f"SELECT Overall_Trust FROM results WHERE Political_Leaning = 'Independent'"
    cursorIndependent.execute(Independent)
    Swing = f"SELECT Overall_Trust FROM results WHERE State = 'Georgia' OR State = 'Nevada'"
    cursorSwing.execute(Swing)
    NoSwing = f"SELECT Overall_Trust FROM results WHERE State = 'California' OR State = 'Ohio' OR State = 'Louisiana'"
    cursorNoSwing.execute(NoSwing)
    age18 = f"SELECT Overall_Trust FROM results WHERE Age = '1'"
    cursor18.execute(age18)
    age30 = f"SELECT Overall_Trust FROM results WHERE Age = '2'"
    cursor30.execute(age30)
    age40 = f"SELECT Overall_Trust FROM results WHERE Age = '3'"
    cursor40.execute(age40)
    age50 = f"SELECT Overall_Trust FROM results WHERE Age = '4'"
    cursor50.execute(age50)
    age60 = f"SELECT Overall_Trust FROM results WHERE Age = '5'"
    cursor60.execute(age60)
    age70 = f"SELECT Overall_Trust FROM results WHERE Age = '6'"
    cursor70.execute(age70)
    age80 = f"SELECT Overall_Trust FROM results WHERE Age = '7'"
    cursor80.execute(age80)


    overallTrustBMD = cursorBMD.fetchall()
    overall_Trust_BMD = np.array([value[0] for value in overallTrustBMD if value[0] is not None])
    overallTrustDREw = cursorDREw.fetchall()
    overall_Trust_DREw = np.array([value[0] for value in overallTrustDREw if value[0] is not None])
    overallTrustDREwo = cursorDREwo.fetchall()
    overall_Trust_DREwo = np.array([value[0] for value in overallTrustDREwo if value[0] is not None])
    overallTrustGeorgia = cursorGeorgia.fetchall()
    overall_Trust_Georgia = np.array([value[0] for value in overallTrustGeorgia if value[0] is not None])
    overallTrustOhio = cursorOhio.fetchall()
    overall_Trust_Ohio = np.array([value[0] for value in overallTrustOhio if value[0] is not None])
    overallTrustCalifornia = cursorCalifornia.fetchall()
    overall_Trust_California = np.array([value[0] for value in overallTrustCalifornia if value[0] is not None])
    overallTrustNevada = cursorNevada.fetchall()
    overall_Trust_Nevada = np.array([value[0] for value in overallTrustNevada if value[0] is not None])
    overallTrustLouisiana = cursorLouisiana.fetchall()
    overall_Trust_Louisiana = np.array([value[0] for value in overallTrustLouisiana if value[0] is not None])
    overallTrustMale = cursorMale.fetchall()
    overall_Trust_Male = np.array([value[0] for value in overallTrustMale if value[0] is not None])
    overallTrustFemale = cursorFemale.fetchall()
    overall_Trust_Female = np.array([value[0] for value in overallTrustFemale if value[0] is not None])
    overallTrustDemocrat = cursorDemocrat.fetchall()
    overall_Trust_Democrat = np.array([value[0] for value in overallTrustDemocrat if value[0] is not None])
    overallTrustRepublican = cursorRepublican.fetchall()
    overall_Trust_Republican = np.array([value[0] for value in overallTrustRepublican if value[0] is not None])
    overallTrustIndependent = cursorIndependent.fetchall()
    overall_Trust_Independent = np.array([value[0] for value in overallTrustIndependent if value[0] is not None])
    overallTrustSwing = cursorSwing.fetchall()
    overall_Trust_Swing = np.array([value[0] for value in overallTrustSwing if value[0] is not None])
    overallTrustNoSwing = cursorNoSwing.fetchall()
    overall_Trust_NoSwing = np.array([value[0] for value in overallTrustNoSwing if value[0] is not None])
    overallTrustAge18 = cursor18.fetchall()
    overall_Trust_Age18 = np.array([value[0] for value in overallTrustAge18 if value[0] is not None])
    overallTrustAge30 = cursor30.fetchall()
    overall_Trust_Age30 = np.array([value[0] for value in overallTrustAge30 if value[0] is not None])
    overallTrustAge40 = cursor40.fetchall()
    overall_Trust_Age40 = np.array([value[0] for value in overallTrustAge40 if value[0] is not None])
    overallTrustAge50 = cursor50.fetchall()
    overall_Trust_Age50 = np.array([value[0] for value in overallTrustAge50 if value[0] is not None])
    overallTrustAge60 = cursor60.fetchall()
    overall_Trust_Age60 = np.array([value[0] for value in overallTrustAge60 if value[0] is not None])
    overallTrustAge70 = cursor70.fetchall()
    overall_Trust_Age70 = np.array([value[0] for value in overallTrustAge70 if value[0] is not None])
    overallTrustAge80 = cursor80.fetchall()
    overall_Trust_Age80 = np.array([value[0] for value in overallTrustAge80 if value[0] is not None])

    #kruskal-Wallis-Test
    # BMD, DREw, DREwo
    # overall_Trust_BMD, overall_Trust_DREw, overall_Trust_DREwo
    # Georgia, Ohio, California, Nevada, Louisiana
    kruskal_wallis = stats.kruskal(overall_Trust_BMD, overall_Trust_DREw, overall_Trust_DREwo)
    print('Kruskal-Wallis Machines statistic:', kruskal_wallis.statistic, 'P-value:', kruskal_wallis.pvalue)
    kruskal_wallisPoliticalLeaning = stats.kruskal(overall_Trust_Democrat, overall_Trust_Republican, overall_Trust_Independent)
    print('Kruskal-Wallis Political Leaning statistic:', kruskal_wallisPoliticalLeaning.statistic, 'P-value:', kruskal_wallisPoliticalLeaning.pvalue)
    kruskal_wallisStates = stats.kruskal(overall_Trust_Georgia, overall_Trust_Ohio, overall_Trust_California, overall_Trust_Nevada, overall_Trust_Louisiana)
    print('Kruskal-Wallis States statistic:', kruskal_wallisStates.statistic, 'P-value:', kruskal_wallisStates.pvalue)
    kruskal_wallisAge = stats.kruskal(overall_Trust_Age18, overall_Trust_Age30, overall_Trust_Age40, overall_Trust_Age50, overall_Trust_Age60, overall_Trust_Age70, overall_Trust_Age80)
    print('Kruskal-Wallis Age statistic:', kruskal_wallisAge.statistic, 'P-value:', kruskal_wallisAge.pvalue)
    kruskal_wallisNonSwing = stats.kruskal(overall_Trust_California, overall_Trust_Ohio, overall_Trust_Louisiana)
    print('Kruskal-Wallis Non-Swing statistic:', kruskal_wallisNonSwing.statistic, 'P-value:', kruskal_wallisNonSwing.pvalue)
    
    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ BMD
    mann_whitneyBMD = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_California, alternative='two-sided')
    mann_whitneyGreaterBMD = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_California, alternative='greater')
    mann_whitneyLessBMD = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_California, alternative='less')

    print('Mann-Whitney-U BMD statistic:', mann_whitneyBMD.statistic, 'P-value:', mann_whitneyBMD.pvalue)
    print('Mann-Whitney-U BMD statistic greater:', mann_whitneyGreaterBMD.statistic, 'P-value:', mann_whitneyGreaterBMD.pvalue)
    print('Mann-Whitney-U BMD statistic less:', mann_whitneyLessBMD.statistic, 'P-value:', mann_whitneyLessBMD.pvalue)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ DREw
    mann_whitneyDREw = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Ohio, alternative='two-sided')
    mann_whitneyGreaterDREw = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Ohio, alternative='greater')
    mann_whitneyLessDREw = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Ohio, alternative='less')

    print('Mann-Whitney-U DREw statistic:', mann_whitneyDREw.statistic, 'P-value:', mann_whitneyDREw.pvalue)
    print('Mann-Whitney-U DREw statistic greater:', mann_whitneyGreaterDREw.statistic, 'P-value:', mann_whitneyGreaterDREw.pvalue)
    print('Mann-Whitney-U DREw statistic less:', mann_whitneyLessDREw.statistic, 'P-value:', mann_whitneyLessDREw.pvalue)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ Gender
    mann_whitneyGender = stats.mannwhitneyu(overall_Trust_Male, overall_Trust_Female, alternative='two-sided')
    mann_whitneyGreaterGender = stats.mannwhitneyu(overall_Trust_Male, overall_Trust_Female, alternative='greater')
    mann_whitneyLessGender = stats.mannwhitneyu(overall_Trust_Male, overall_Trust_Female, alternative='less')

    print('Mann-Whitney-U Gender statistic:', mann_whitneyGender.statistic, 'P-value:', mann_whitneyGender.pvalue)
    print('Mann-Whitney-U Gender statistic greater:', mann_whitneyGreaterGender.statistic, 'P-value:', mann_whitneyGreaterGender.pvalue)
    print('Mann-Whitney-U Gender statistic less:', mann_whitneyLessGender.statistic, 'P-value:', mann_whitneyLessGender.pvalue)

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ Swing vs NoSwing
    mann_whitneySwing = stats.mannwhitneyu(overall_Trust_Swing, overall_Trust_NoSwing, alternative='two-sided')
    mann_whitneyGreaterSwing = stats.mannwhitneyu(overall_Trust_Swing, overall_Trust_NoSwing, alternative='greater')
    mann_whitneyLessSwing = stats.mannwhitneyu(overall_Trust_Swing, overall_Trust_NoSwing, alternative='less')

    print('Mann-Whitney-U Swing NoSwing statistic:', mann_whitneySwing.statistic, 'P-value:', mann_whitneySwing.pvalue)
    print('Mann-Whitney-U Swing NoSwing statistic greater:', mann_whitneyGreaterSwing.statistic, 'P-value:', mann_whitneyGreaterSwing.pvalue)
    print('Mann-Whitney-U Swing NoSwing statistic less:', mann_whitneyLessSwing.statistic, 'P-value:', mann_whitneyLessSwing.pvalue)


finally:
    # Close the cursor and connection
    cursorBMD.close()
    cursorDREw.close()
    cursorDREwo.close()
    cursorGeorgia.close()
    cursorOhio.close()
    cursorCalifornia.close()
    cursorNevada.close()
    cursorLouisiana.close()
    cursorMale.close()
    cursorFemale.close()
    cursorDemocrat.close()
    cursorRepublican.close()
    cursorIndependent.close()
    cursorSwing.close()
    cursorNoSwing.close()
    cursor18.close()
    cursor30.close()
    cursor40.close()
    cursor50.close()
    cursor60.close()
    cursor70.close()
    cursor80.close()
    connection.close()