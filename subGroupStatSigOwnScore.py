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
    cursorCaliMale = connection.cursor(buffered=True)
    cursorCaliFemale = connection.cursor(buffered=True)
    cursorCaliDem = connection.cursor(buffered=True)
    cursorCaliRep = connection.cursor(buffered=True)
    cursorCaliInd = connection.cursor(buffered=True)

    cursorGeorgiaMale = connection.cursor(buffered=True)
    cursorGeorgiaFemale = connection.cursor(buffered=True)
    cursorGeorgiaDem = connection.cursor(buffered=True)
    cursorGeorgiaRep = connection.cursor(buffered=True)
    cursorGeorgiaInd = connection.cursor(buffered=True)

    cursorOhioMale = connection.cursor(buffered=True)
    cursorOhioFemale = connection.cursor(buffered=True)
    cursorOhioDem = connection.cursor(buffered=True)
    cursorOhioRep = connection.cursor(buffered=True)
    cursorOhioInd = connection.cursor(buffered=True)

    cursorNevadaMale = connection.cursor(buffered=True)
    cursorNevadaFemale = connection.cursor(buffered=True)
    cursorNevadaDem = connection.cursor(buffered=True)
    cursorNevadaRep = connection.cursor(buffered=True)
    cursorNevadaInd = connection.cursor(buffered=True)

    cursorLouisianaMale = connection.cursor(buffered=True)
    cursorLouisianaFemale = connection.cursor(buffered=True)
    cursorLouisianaDem = connection.cursor(buffered=True)
    cursorLouisianaRep = connection.cursor(buffered=True)
    cursorLouisianaInd = connection.cursor(buffered=True)




    caliMale = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' AND Gender = '1'"
    cursorCaliMale.execute(caliMale)
    caliMale_Score = cursorCaliMale.fetchall()
    caliFemale = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' AND Gender = '2'"
    cursorCaliFemale.execute(caliFemale)
    caliFemale_Score = cursorCaliFemale.fetchall()
    caliDem = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' AND Political_Leaning = '1'"
    cursorCaliDem.execute(caliDem)
    caliDem_Score = cursorCaliDem.fetchall()
    caliRep = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' AND Political_Leaning = '2'"
    cursorCaliRep.execute(caliRep)
    caliRep_Score = cursorCaliRep.fetchall()
    caliInd = f"SELECT Machine_Score_1 FROM results WHERE State = 'California' AND Political_Leaning = '3'"
    cursorCaliInd.execute(caliInd)
    caliInd_Score = cursorCaliInd.fetchall()

    geoMale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' AND Gender = '1'"
    cursorGeorgiaMale.execute(geoMale)
    geoMale_Score = cursorGeorgiaMale.fetchall()
    geoFemale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' AND Gender = '2'"
    cursorGeorgiaFemale.execute(geoFemale)
    geoFemale_Score = cursorGeorgiaFemale.fetchall()
    geoDem = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' AND Political_Leaning = '1'"
    cursorGeorgiaDem.execute(geoDem)
    geoDem_Score = cursorGeorgiaDem.fetchall()
    geoRep = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' AND Political_Leaning = '2'"
    cursorGeorgiaRep.execute(geoRep)
    geoRep_Score = cursorGeorgiaRep.fetchall()
    geoInd = f"SELECT Machine_Score_1 FROM results WHERE State = 'Georgia' AND Political_Leaning = '3'"
    cursorGeorgiaInd.execute(geoInd)
    geoInd_Score = cursorGeorgiaInd.fetchall()

    ohioMale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' AND Gender = '1'"
    cursorOhioMale.execute(ohioMale)
    ohioMale_Score = cursorOhioMale.fetchall()
    ohioFemale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' AND Gender = '2'"
    cursorOhioFemale.execute(ohioFemale)
    ohioFemale_Score = cursorOhioFemale.fetchall()
    ohioDem = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' AND Political_Leaning = '1'"
    cursorOhioDem.execute(ohioDem)
    ohioDem_Score = cursorOhioDem.fetchall()
    ohioRep = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' AND Political_Leaning = '2'"
    cursorOhioRep.execute(ohioRep)
    ohioRep_Score = cursorOhioRep.fetchall()
    ohioInd = f"SELECT Machine_Score_1 FROM results WHERE State = 'Ohio' AND Political_Leaning = '3'"
    cursorOhioInd.execute(ohioInd)
    ohioInd_Score = cursorOhioInd.fetchall()

    nevadaMale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada' AND Gender = '1'"
    cursorNevadaMale.execute(nevadaMale)
    nevadaMale_Score = cursorNevadaMale.fetchall()
    nevadaFemale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada' AND Gender = '2'"
    cursorNevadaFemale.execute(nevadaFemale)
    nevadaFemale_Score = cursorNevadaFemale.fetchall()
    nevadaDem = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada' AND Political_Leaning = '1'"
    cursorNevadaDem.execute(nevadaDem)
    nevadaDem_Score = cursorNevadaDem.fetchall()
    nevadaRep = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada' AND Political_Leaning = '2'"
    cursorNevadaRep.execute(nevadaRep)
    nevadaRep_Score = cursorNevadaRep.fetchall()
    nevadaInd = f"SELECT Machine_Score_1 FROM results WHERE State = 'Nevada' AND Political_Leaning = '3'"
    cursorNevadaInd.execute(nevadaInd)
    nevadaInd_Score = cursorNevadaInd.fetchall()

    louisianaMale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana' AND Gender = '1'"
    cursorLouisianaMale.execute(louisianaMale)
    louisianaMale_Score = cursorLouisianaMale.fetchall()
    louisianaFemale = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana' AND Gender = '2'"
    cursorLouisianaFemale.execute(louisianaFemale)
    louisianaFemale_Score = cursorLouisianaFemale.fetchall()
    louisianaDem = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana' AND Political_Leaning = '1'"
    cursorLouisianaDem.execute(louisianaDem)
    louisianaDem_Score = cursorLouisianaDem.fetchall()
    louisianaRep = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana' AND Political_Leaning = '2'"
    cursorLouisianaRep.execute(louisianaRep)
    louisianaRep_Score = cursorLouisianaRep.fetchall()
    louisianaInd = f"SELECT Machine_Score_1 FROM results WHERE State = 'Louisiana' AND Political_Leaning = '3'"
    cursorLouisianaInd.execute(louisianaInd)
    louisianaInd_Score = cursorLouisianaInd.fetchall()

    score_Cali_Male = np.array([value[0] for value in caliMale_Score if value[0] is not None])
    score_Cali_Female = np.array([value[0] for value in caliFemale_Score if value[0] is not None])
    score_Cali_Dem = np.array([value[0] for value in caliDem_Score if value[0] is not None])
    score_Cali_Rep = np.array([value[0] for value in caliRep_Score if value[0] is not None])
    score_Cali_Ind = np.array([value[0] for value in caliInd_Score if value[0] is not None])

    score_Geo_Male = np.array([value[0] for value in geoMale_Score if value[0] is not None])
    score_Geo_Female = np.array([value[0] for value in geoFemale_Score if value[0] is not None])
    score_Geo_Dem = np.array([value[0] for value in geoDem_Score if value[0] is not None])
    score_Geo_Rep = np.array([value[0] for value in geoRep_Score if value[0] is not None])
    score_Geo_Ind = np.array([value[0] for value in geoInd_Score if value[0] is not None])

    score_Ohio_Male = np.array([value[0] for value in ohioMale_Score if value[0] is not None])
    score_Ohio_Female = np.array([value[0] for value in ohioFemale_Score if value[0] is not None])
    score_Ohio_Dem = np.array([value[0] for value in ohioDem_Score if value[0] is not None])
    score_Ohio_Rep = np.array([value[0] for value in ohioRep_Score if value[0] is not None])
    score_Ohio_Ind = np.array([value[0] for value in ohioInd_Score if value[0] is not None])

    score_Nevada_Male = np.array([value[0] for value in nevadaMale_Score if value[0] is not None])
    score_Nevada_Female = np.array([value[0] for value in nevadaFemale_Score if value[0] is not None])
    score_Nevada_Dem = np.array([value[0] for value in nevadaDem_Score if value[0] is not None])
    score_Nevada_Rep = np.array([value[0] for value in nevadaRep_Score if value[0] is not None])
    score_Nevada_Ind = np.array([value[0] for value in nevadaInd_Score if value[0] is not None])

    score_Louisiana_Male = np.array([value[0] for value in louisianaMale_Score if value[0] is not None])
    score_Louisiana_Female = np.array([value[0] for value in louisianaFemale_Score if value[0] is not None])
    score_Louisiana_Dem = np.array([value[0] for value in louisianaDem_Score if value[0] is not None])
    score_Louisiana_Rep = np.array([value[0] for value in louisianaRep_Score if value[0] is not None])
    score_Louisiana_Ind = np.array([value[0] for value in louisianaInd_Score if value[0] is not None])

    score_BMD_Male = np.append(score_Cali_Male, score_Geo_Male)
    score_BMD_Female = np.append(score_Cali_Female, score_Geo_Female)
    score_BMD_Dem = np.append(score_Cali_Dem, score_Geo_Dem)
    score_BMD_Rep = np.append(score_Cali_Rep, score_Geo_Rep)
    score_BMD_Ind = np.append(score_Cali_Ind, score_Geo_Ind)

    score_DREw_Male = np.append(score_Ohio_Male, score_Nevada_Male)
    score_DREw_Female = np.append(score_Ohio_Female, score_Nevada_Female)
    score_DREw_Dem = np.append(score_Ohio_Dem, score_Nevada_Dem)
    score_DREw_Rep = np.append(score_Ohio_Rep, score_Nevada_Rep)
    score_DREw_Ind = np.append(score_Ohio_Ind, score_Nevada_Ind)

    
    #kruskal-Wallis-Test
    kruskal_wallis_Male_3_Machines = stats.kruskal(score_BMD_Male, score_DREw_Male, score_Louisiana_Male)
    print('Kruskal-Wallis Machines male statistic:', kruskal_wallis_Male_3_Machines.statistic, 'P-value:', kruskal_wallis_Male_3_Machines.pvalue)
    kruskal_wallis_Female_3_Machines = stats.kruskal(score_BMD_Female, score_DREw_Female, score_Louisiana_Female)
    print('Kruskal-Wallis Machines female statistic:', kruskal_wallis_Female_3_Machines.statistic, 'P-value:', kruskal_wallis_Female_3_Machines.pvalue)
    kruskal_wallis_Dem_3_Machines = stats.kruskal(score_BMD_Dem, score_DREw_Dem, score_Louisiana_Dem)
    print('Kruskal-Wallis Machines dems statistic:', kruskal_wallis_Dem_3_Machines.statistic, 'P-value:', kruskal_wallis_Dem_3_Machines.pvalue)
    kruskal_wallis_Rep_3_Machines = stats.kruskal(score_BMD_Rep, score_DREw_Rep, score_Louisiana_Rep)
    print('Kruskal-Wallis Machines reps statistic:', kruskal_wallis_Rep_3_Machines.statistic, 'P-value:', kruskal_wallis_Rep_3_Machines.pvalue)
    kruskal_wallis_Ind_3_Machines = stats.kruskal(score_BMD_Ind, score_DREw_Ind, score_Louisiana_Ind)
    print('Kruskal-Wallis Machines inds statistic:', kruskal_wallis_Ind_3_Machines.statistic, 'P-value:', kruskal_wallis_Ind_3_Machines.pvalue)

    kruskal_wallis_Male_States = stats.kruskal(score_Cali_Male, score_Geo_Male, score_Ohio_Male, score_Nevada_Male, score_Louisiana_Male)
    print('Kruskal-Wallis states male statistic:', kruskal_wallis_Male_States.statistic, 'P-value:', kruskal_wallis_Male_States.pvalue)
    kruskal_wallis_Female_States = stats.kruskal(score_Cali_Female, score_Geo_Female, score_Ohio_Female, score_Nevada_Female, score_Louisiana_Female)
    print('Kruskal-Wallis states female statistic:', kruskal_wallis_Female_States.statistic, 'P-value:', kruskal_wallis_Female_States.pvalue)
    kruskal_wallis_Dem_States = stats.kruskal(score_Cali_Dem, score_Geo_Dem, score_Ohio_Dem, score_Nevada_Dem, score_Louisiana_Dem)
    print('Kruskal-Wallis states dems statistic:', kruskal_wallis_Dem_States.statistic, 'P-value:', kruskal_wallis_Dem_States.pvalue)
    kruskal_wallis_Rep_States = stats.kruskal(score_Cali_Rep, score_Geo_Rep, score_Ohio_Rep, score_Nevada_Rep, score_Louisiana_Rep)
    print('Kruskal-Wallis states reps statistic:', kruskal_wallis_Rep_States.statistic, 'P-value:', kruskal_wallis_Rep_States.pvalue)
    kruskal_wallis_Ind_States = stats.kruskal(score_Cali_Ind, score_Geo_Ind, score_Ohio_Ind, score_Nevada_Ind, score_Louisiana_Ind)
    print('Kruskal-Wallis states inds statistic:', kruskal_wallis_Ind_States.statistic, 'P-value:', kruskal_wallis_Ind_States.pvalue)


    
    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ BMD
    mann_whitneyBMD_Male = stats.mannwhitneyu(score_Geo_Male, score_Cali_Male, alternative='two-sided')
    mann_whitneyGreaterBMD_Male = stats.mannwhitneyu(score_Geo_Male, score_Cali_Male, alternative='greater')
    mann_whitneyLessBMD_Male = stats.mannwhitneyu(score_Geo_Male, score_Cali_Male, alternative='less')

    print('Mann-Whitney-U BMD male statistic:', mann_whitneyBMD_Male.statistic, 'P-value:', mann_whitneyBMD_Male.pvalue)
    print('Mann-Whitney-U BMD male statistic greater:', mann_whitneyGreaterBMD_Male.statistic, 'P-value:', mann_whitneyGreaterBMD_Male.pvalue)
    print('Mann-Whitney-U BMD male statistic less:', mann_whitneyLessBMD_Male.statistic, 'P-value:', mann_whitneyLessBMD_Male.pvalue)

    mann_whitneyBMD_Female = stats.mannwhitneyu(score_Geo_Female, score_Cali_Female, alternative='two-sided')
    mann_whitneyGreaterBMD_Female = stats.mannwhitneyu(score_Geo_Female, score_Cali_Female, alternative='greater')
    mann_whitneyLessBMD_Female = stats.mannwhitneyu(score_Geo_Female, score_Cali_Female, alternative='less')

    print('Mann-Whitney-U BMD female statistic:', mann_whitneyBMD_Female.statistic, 'P-value:', mann_whitneyBMD_Female.pvalue)
    print('Mann-Whitney-U BMD female statistic greater:', mann_whitneyGreaterBMD_Female.statistic, 'P-value:', mann_whitneyGreaterBMD_Female.pvalue)
    print('Mann-Whitney-U BMD female statistic less:', mann_whitneyLessBMD_Female.statistic, 'P-value:', mann_whitneyLessBMD_Female.pvalue)

    mann_whitneyBMD_Dem = stats.mannwhitneyu(score_Geo_Dem, score_Cali_Dem, alternative='two-sided')
    mann_whitneyGreaterBMD_Dem = stats.mannwhitneyu(score_Geo_Dem, score_Cali_Dem, alternative='greater')
    mann_whitneyLessBMD_Dem = stats.mannwhitneyu(score_Geo_Dem, score_Cali_Dem, alternative='less')

    print('Mann-Whitney-U BMD dems statistic:', mann_whitneyBMD_Dem.statistic, 'P-value:', mann_whitneyBMD_Dem.pvalue)
    print('Mann-Whitney-U BMD dems statistic greater:', mann_whitneyGreaterBMD_Dem.statistic, 'P-value:', mann_whitneyGreaterBMD_Dem.pvalue)
    print('Mann-Whitney-U BMD dems statistic less:', mann_whitneyLessBMD_Dem.statistic, 'P-value:', mann_whitneyLessBMD_Dem.pvalue)

    mann_whitneyBMD_Rep = stats.mannwhitneyu(score_Geo_Rep, score_Cali_Rep, alternative='two-sided')
    mann_whitneyGreaterBMD_Rep = stats.mannwhitneyu(score_Geo_Rep, score_Cali_Rep, alternative='greater')
    mann_whitneyLessBMD_Rep = stats.mannwhitneyu(score_Geo_Rep, score_Cali_Rep, alternative='less')

    print('Mann-Whitney-U BMD reps statistic:', mann_whitneyBMD_Rep.statistic, 'P-value:', mann_whitneyBMD_Rep.pvalue)
    print('Mann-Whitney-U BMD reps statistic greater:', mann_whitneyGreaterBMD_Rep.statistic, 'P-value:', mann_whitneyGreaterBMD_Rep.pvalue)
    print('Mann-Whitney-U BMD reps statistic less:', mann_whitneyLessBMD_Rep.statistic, 'P-value:', mann_whitneyLessBMD_Rep.pvalue)

    mann_whitneyBMD_Ind = stats.mannwhitneyu(score_Geo_Ind, score_Cali_Ind, alternative='two-sided')
    mann_whitneyGreaterBMD_Ind = stats.mannwhitneyu(score_Geo_Ind, score_Cali_Ind, alternative='greater')
    mann_whitneyLessBMD_Ind = stats.mannwhitneyu(score_Geo_Ind, score_Cali_Ind, alternative='less')
    
    print('Mann-Whitney-U BMD inds statistic:', mann_whitneyBMD_Ind.statistic, 'P-value:', mann_whitneyBMD_Ind.pvalue)
    print('Mann-Whitney-U BMD inds statistic greater:', mann_whitneyGreaterBMD_Ind.statistic, 'P-value:', mann_whitneyGreaterBMD_Ind.pvalue)
    print('Mann-Whitney-U BMD inds statistic less:', mann_whitneyLessBMD_Ind.statistic, 'P-value:', mann_whitneyLessBMD_Ind.pvalue)


    # Mann-Whitney-U-Test ‘two-sided’, ‘less’, ‘greater’ DREw
    mann_whitneyDREw_Male = stats.mannwhitneyu(score_Nevada_Male, score_Ohio_Male, alternative='two-sided')
    mann_whitneyGreaterDREw_Male = stats.mannwhitneyu(score_Nevada_Male, score_Ohio_Male, alternative='greater')
    mann_whitneyLessDREw_Male = stats.mannwhitneyu(score_Nevada_Male, score_Ohio_Male, alternative='less')

    print('Mann-Whitney-U DREw male statistic:', mann_whitneyDREw_Male.statistic, 'P-value:', mann_whitneyDREw_Male.pvalue)
    print('Mann-Whitney-U DREw male statistic greater:', mann_whitneyGreaterDREw_Male.statistic, 'P-value:', mann_whitneyGreaterDREw_Male.pvalue)
    print('Mann-Whitney-U DREw male statistic less:', mann_whitneyLessDREw_Male.statistic, 'P-value:', mann_whitneyLessDREw_Male.pvalue)

    mann_whitneyDREw_Female = stats.mannwhitneyu(score_Nevada_Female, score_Ohio_Female, alternative='two-sided')
    mann_whitneyGreaterDREw_Female = stats.mannwhitneyu(score_Nevada_Female, score_Ohio_Female, alternative='greater')
    mann_whitneyLessDREw_Female = stats.mannwhitneyu(score_Nevada_Female, score_Ohio_Female, alternative='less')

    print('Mann-Whitney-U DREw female statistic:', mann_whitneyDREw_Female.statistic, 'P-value:', mann_whitneyDREw_Female.pvalue)
    print('Mann-Whitney-U DREw female statistic greater:', mann_whitneyGreaterDREw_Female.statistic, 'P-value:', mann_whitneyGreaterDREw_Female.pvalue)
    print('Mann-Whitney-U DREw female statistic less:', mann_whitneyLessDREw_Female.statistic, 'P-value:', mann_whitneyLessDREw_Female.pvalue)

    mann_whitneyDREw_Dem = stats.mannwhitneyu(score_Nevada_Dem, score_Ohio_Dem, alternative='two-sided')
    mann_whitneyGreaterDREw_Dem = stats.mannwhitneyu(score_Nevada_Dem, score_Ohio_Dem, alternative='greater')
    mann_whitneyLessDREw_Dem = stats.mannwhitneyu(score_Nevada_Dem, score_Ohio_Dem, alternative='less')

    print('Mann-Whitney-U DREw dems statistic:', mann_whitneyDREw_Dem.statistic, 'P-value:', mann_whitneyDREw_Dem.pvalue)
    print('Mann-Whitney-U DREw dems statistic greater:', mann_whitneyGreaterDREw_Dem.statistic, 'P-value:', mann_whitneyGreaterDREw_Dem.pvalue)
    print('Mann-Whitney-U DREw dems statistic less:', mann_whitneyLessDREw_Dem.statistic, 'P-value:', mann_whitneyLessDREw_Dem.pvalue)

    mann_whitneyDREw_Rep = stats.mannwhitneyu(score_Nevada_Rep, score_Ohio_Rep, alternative='two-sided')
    mann_whitneyGreaterDREw_Rep = stats.mannwhitneyu(score_Nevada_Rep, score_Ohio_Rep, alternative='greater')
    mann_whitneyLessDREw_Rep = stats.mannwhitneyu(score_Nevada_Rep, score_Ohio_Rep, alternative='less')

    print('Mann-Whitney-U DREw reps statistic:', mann_whitneyDREw_Rep.statistic, 'P-value:', mann_whitneyDREw_Rep.pvalue)
    print('Mann-Whitney-U DREw reps statistic greater:', mann_whitneyGreaterDREw_Rep.statistic, 'P-value:', mann_whitneyGreaterDREw_Rep.pvalue)
    print('Mann-Whitney-U DREw reps statistic less:', mann_whitneyLessDREw_Rep.statistic, 'P-value:', mann_whitneyLessDREw_Rep.pvalue)

    mann_whitneyDREw_Ind = stats.mannwhitneyu(score_Nevada_Ind, score_Ohio_Ind, alternative='two-sided')
    mann_whitneyGreaterDREw_Ind = stats.mannwhitneyu(score_Nevada_Ind, score_Ohio_Ind, alternative='greater')
    mann_whitneyLessDREw_Ind = stats.mannwhitneyu(score_Nevada_Ind, score_Ohio_Ind, alternative='less')

    print('Mann-Whitney-U DREw inds statistic:', mann_whitneyDREw_Ind.statistic, 'P-value:', mann_whitneyDREw_Ind.pvalue)
    print('Mann-Whitney-U DREw inds statistic greater:', mann_whitneyGreaterDREw_Ind.statistic, 'P-value:', mann_whitneyGreaterDREw_Ind.pvalue)
    print('Mann-Whitney-U DREw inds statistic less:', mann_whitneyLessDREw_Ind.statistic, 'P-value:', mann_whitneyLessDREw_Ind.pvalue)
    
    dunn = sp.posthoc_dunn([score_Cali_Dem, score_Geo_Dem, score_Ohio_Dem, score_Nevada_Dem, score_Louisiana_Dem], p_adjust='bonferroni')
    print(dunn)

finally:
    # Close the cursor and connection
    cursorCaliMale.close()
    cursorCaliFemale.close()
    cursorCaliDem.close()
    cursorCaliRep.close()
    cursorCaliInd.close()

    cursorGeorgiaMale.close()
    cursorGeorgiaFemale.close()
    cursorGeorgiaDem.close()
    cursorGeorgiaRep.close()
    cursorGeorgiaInd.close()

    cursorOhioMale.close()
    cursorOhioFemale.close()
    cursorOhioDem.close()
    cursorOhioRep.close()
    cursorOhioInd.close()

    cursorNevadaMale.close()
    cursorNevadaFemale.close()
    cursorNevadaDem.close()
    cursorNevadaRep.close()
    cursorNevadaInd.close()

    cursorLouisianaMale.close()
    cursorLouisianaFemale.close()
    cursorLouisianaDem.close()
    cursorLouisianaRep.close()
    cursorLouisianaInd.close()
    
    connection.close()