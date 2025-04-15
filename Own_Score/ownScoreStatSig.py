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



    BMD = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' OR State = 'California'"
    cursorBMD.execute(BMD)
    DREw = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' OR State = 'Nevada'"
    cursorDREw.execute(DREw)
    DREwo = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana'"
    cursorDREwo.execute(DREwo)
    Georgia = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia'"
    cursorGeorgia.execute(Georgia) 
    Ohio = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio'"
    cursorOhio.execute(Ohio)
    California = f"SELECT Machine_Score_1 FROM results WHERE State = 'California'"
    cursorCalifornia.execute(California)
    Nevada = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada'"
    cursorNevada.execute(Nevada)
    Louisiana = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana'"
    cursorLouisiana.execute(Louisiana)
    Male = f"SELECT Machine_Score_1 FROM results WHERE Gender = '1'"
    cursorMale.execute(Male)
    Female = f"SELECT Machine_Score_1 FROM results WHERE Gender = '2'"
    cursorFemale.execute(Female)
    Democrat = f"SELECT Machine_Score_1 FROM results WHERE Political_Leaning = '1'"
    cursorDemocrat.execute(Democrat)
    Republican = f"SELECT Machine_Score_1 FROM results WHERE Political_Leaning = '2'"
    cursorRepublican.execute(Republican)
    Independent = f"SELECT Machine_Score_1 FROM results WHERE Political_Leaning = '3'"
    cursorIndependent.execute(Independent)
    Swing = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' OR State = 'Nevada'"
    cursorSwing.execute(Swing)
    NoSwing = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' OR State = 'Ohio' OR State = 'Louisiana'"
    cursorNoSwing.execute(NoSwing)
    age18 = f"SELECT Machine_Score_1 FROM results WHERE Age = '1'"
    cursor18.execute(age18)
    age30 = f"SELECT Machine_Score_1 FROM results WHERE Age = '2'"
    cursor30.execute(age30)
    age40 = f"SELECT Machine_Score_1 FROM results WHERE Age = '3'"
    cursor40.execute(age40)
    age50 = f"SELECT Machine_Score_1 FROM results WHERE Age = '4'"
    cursor50.execute(age50)
    age60 = f"SELECT Machine_Score_1 FROM results WHERE Age = '5'"
    cursor60.execute(age60)
    age70 = f"SELECT Machine_Score_1 FROM results WHERE Age = '6'"
    cursor70.execute(age70)
    age80 = f"SELECT Machine_Score_1 FROM results WHERE Age = '7'"
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

    #dunn test political leaning
    dunn = sp.posthoc_dunn([overall_Trust_Democrat, overall_Trust_Republican, overall_Trust_Independent], p_adjust='bonferroni')
    print(dunn)

    print('Avg Overall Trust Democrat:', overall_Trust_Democrat.mean(), 'Avg Overall Trust Republican:', overall_Trust_Republican.mean(), 'Avg Overall Trust Independent:', overall_Trust_Independent.mean())

    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’
    mann_whitney = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Republican, alternative='two-sided')
    mann_whitneyGreater = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Republican, alternative='greater')
    mann_whitneyLess = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Republican, alternative='less')
    mann_whitney2 = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Independent, alternative='two-sided')
    mann_whitneyGreater2 = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Independent, alternative='greater')
    mann_whitneyLess2 = stats.mannwhitneyu(overall_Trust_Democrat, overall_Trust_Independent, alternative='less')
    mann_whitney3 = stats.mannwhitneyu(overall_Trust_Republican, overall_Trust_Independent, alternative='two-sided')
    mann_whitneyGreater3 = stats.mannwhitneyu(overall_Trust_Republican, overall_Trust_Independent, alternative='greater')
    mann_whitneyLess3 = stats.mannwhitneyu(overall_Trust_Republican, overall_Trust_Independent, alternative='less')

    print('Mann-Whitney-U Dem v Rep statistic:', mann_whitney.statistic, 'P-value:', mann_whitney.pvalue)
    print('Mann-Whitney-U Dem v Rep statistic greater:', mann_whitneyGreater.statistic, 'P-value:', mann_whitneyGreater.pvalue)
    print('Mann-Whitney-U Dem v Rep statistic less:', mann_whitneyLess.statistic, 'P-value:', mann_whitneyLess.pvalue)
    print('Mann-Whitney-U dem v ind statistic:', mann_whitney2.statistic, 'P-value:', mann_whitney2.pvalue)
    print('Mann-Whitney-U dem v ind statistic greater:', mann_whitneyGreater2.statistic, 'P-value:', mann_whitneyGreater2.pvalue)
    print('Mann-Whitney-U dem v ind statistic less:', mann_whitneyLess2.statistic, 'P-value:', mann_whitneyLess2.pvalue)
    print('Mann-Whitney-U rep v ind statistic:', mann_whitney3.statistic, 'P-value:', mann_whitney3.pvalue)
    print('Mann-Whitney-U rep v ind statistic greater:', mann_whitneyGreater3.statistic, 'P-value:', mann_whitneyGreater3.pvalue)
    print('Mann-Whitney-U rep v ind statistic less:', mann_whitneyLess3.statistic, 'P-value:', mann_whitneyLess3.pvalue)


    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ for every state
    mann_whitneyGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Ohio, alternative='two-sided')
    mann_whitneyGreaterGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Ohio, alternative='greater')
    mann_whitneyLessGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Ohio, alternative='less')

    mann_whitneyCalifornia = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Nevada, alternative='two-sided')
    mann_whitneyGreaterCalifornia = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Nevada, alternative='greater')
    mann_whitneyLessCalifornia = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Nevada, alternative='less')

    mann_whitneyOhio = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_Louisiana, alternative='two-sided')
    mann_whitneyGreaterOhio = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_Louisiana, alternative='greater')
    mann_whitneyLessOhio = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_Louisiana, alternative='less')

    mann_whitneyNevada = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Louisiana, alternative='two-sided')
    mann_whitneyGreaterNevada = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Louisiana, alternative='greater')
    mann_whitneyLessNevada = stats.mannwhitneyu(overall_Trust_Nevada, overall_Trust_Louisiana, alternative='less')

    mann_whitneyLouisiana = stats.mannwhitneyu(overall_Trust_Louisiana, overall_Trust_Georgia, alternative='two-sided')
    mann_whitneyGreaterLouisiana = stats.mannwhitneyu(overall_Trust_Louisiana, overall_Trust_Georgia, alternative='greater')
    mann_whitneyLessLouisiana = stats.mannwhitneyu(overall_Trust_Louisiana, overall_Trust_Georgia, alternative='less')

    mann_whitneyNevadaGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Nevada, alternative='two-sided')
    mann_whitneyGreaterNevadaGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Nevada, alternative='greater')
    mann_whitneyLessNevadaGeorgia = stats.mannwhitneyu(overall_Trust_Georgia, overall_Trust_Nevada, alternative='less')

    mann_whitneyCaliforniaLouisiana = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Louisiana, alternative='two-sided')
    mann_whitneyGreaterCaliforniaLouisiana = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Louisiana, alternative='greater')
    mann_whitneyLessCaliforniaLouisiana = stats.mannwhitneyu(overall_Trust_California, overall_Trust_Louisiana, alternative='less')

    mann_whitneyOhioCalifornia = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_California, alternative='two-sided')
    mann_whitneyGreaterOhioCalifornia = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_California, alternative='greater')
    mann_whitneyLessOhioCalifornia = stats.mannwhitneyu(overall_Trust_Ohio, overall_Trust_California, alternative='less')

    print('Mann-Whitney-U Georgia v Ohio statistic:', mann_whitneyGeorgia.statistic, 'P-value:', mann_whitneyGeorgia.pvalue)
    print('Mann-Whitney-U Georgia v Ohio statistic greater:', mann_whitneyGreaterGeorgia.statistic, 'P-value:', mann_whitneyGreaterGeorgia.pvalue)
    print('Mann-Whitney-U Georgia v Ohio statistic less:', mann_whitneyLessGeorgia.statistic, 'P-value:', mann_whitneyLessGeorgia.pvalue)
    print('Mann-Whitney-U California v Nevada statistic:', mann_whitneyCalifornia.statistic, 'P-value:', mann_whitneyCalifornia.pvalue)
    print('Mann-Whitney-U California v Nevada statistic greater:', mann_whitneyGreaterCalifornia.statistic, 'P-value:', mann_whitneyGreaterCalifornia.pvalue)
    print('Mann-Whitney-U California v Nevada statistic less:', mann_whitneyLessCalifornia.statistic, 'P-value:', mann_whitneyLessCalifornia.pvalue)
    print('Mann-Whitney-U Ohio v Louisiana statistic:', mann_whitneyOhio.statistic, 'P-value:', mann_whitneyOhio.pvalue)
    print('Mann-Whitney-U Ohio v Louisiana statistic greater:', mann_whitneyGreaterOhio.statistic, 'P-value:', mann_whitneyGreaterOhio.pvalue)
    print('Mann-Whitney-U Ohio v Louisiana statistic less:', mann_whitneyLessOhio.statistic, 'P-value:', mann_whitneyLessOhio.pvalue)
    print('Mann-Whitney-U Nevada v Louisiana statistic:', mann_whitneyNevada.statistic, 'P-value:', mann_whitneyNevada.pvalue)
    print('Mann-Whitney-U Nevada v Louisiana statistic greater:', mann_whitneyGreaterNevada.statistic, 'P-value:', mann_whitneyGreaterNevada.pvalue)
    print('Mann-Whitney-U Nevada v Louisiana statistic less:', mann_whitneyLessNevada.statistic, 'P-value:', mann_whitneyLessNevada.pvalue)
    print('Mann-Whitney-U Louisiana v Georgia statistic:', mann_whitneyLouisiana.statistic, 'P-value:', mann_whitneyLouisiana.pvalue)
    print('Mann-Whitney-U Louisiana v Georgia statistic greater:', mann_whitneyGreaterLouisiana.statistic, 'P-value:', mann_whitneyGreaterLouisiana.pvalue)
    print('Mann-Whitney-U Louisiana v Georgia statistic less:', mann_whitneyLessLouisiana.statistic, 'P-value:', mann_whitneyLessLouisiana.pvalue)
    print('Mann-Whitney-U Nevada v Georgia statistic:', mann_whitneyNevadaGeorgia.statistic, 'P-value:', mann_whitneyNevadaGeorgia.pvalue)
    print('Mann-Whitney-U Nevada v Georgia statistic greater:', mann_whitneyGreaterNevadaGeorgia.statistic, 'P-value:', mann_whitneyGreaterNevadaGeorgia.pvalue)
    print('Mann-Whitney-U Nevada v Georgia statistic less:', mann_whitneyLessNevadaGeorgia.statistic, 'P-value:', mann_whitneyLessNevadaGeorgia.pvalue)
    print('Mann-Whitney-U California v Louisiana statistic:', mann_whitneyCaliforniaLouisiana.statistic, 'P-value:', mann_whitneyCaliforniaLouisiana.pvalue)
    print('Mann-Whitney-U California v Louisiana statistic greater:', mann_whitneyGreaterCaliforniaLouisiana.statistic, 'P-value:', mann_whitneyGreaterCaliforniaLouisiana.pvalue)
    print('Mann-Whitney-U California v Louisiana statistic less:', mann_whitneyLessCaliforniaLouisiana.statistic, 'P-value:', mann_whitneyLessCaliforniaLouisiana.pvalue)
    print('Mann-Whitney-U Ohio v California statistic:', mann_whitneyOhioCalifornia.statistic, 'P-value:', mann_whitneyOhioCalifornia.pvalue)
    print('Mann-Whitney-U Ohio v California statistic greater:', mann_whitneyGreaterOhioCalifornia.statistic, 'P-value:', mann_whitneyGreaterOhioCalifornia.pvalue)
    print('Mann-Whitney-U Ohio v California statistic less:', mann_whitneyLessOhioCalifornia.statistic, 'P-value:', mann_whitneyLessOhioCalifornia.pvalue)
    
    
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