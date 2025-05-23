import getpass
import mysql.connector
import numpy as np
from scipy import stats
import tkinter as tk
import matplotlib.pyplot as plt
import statsmodels.api as sm
#import statsmodels.stats as st
import tkinter.scrolledtext as scrolledtext
import scikit_posthocs as sp
import trust_notrust as tn
import codingFunction as cf
import drawDiagrams as dd
import filterIQR15 as fi
import normalDist as nd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
import pandas as pd

# Prompt the user for the MySQL password
password = getpass.getpass("Enter your MySQL password: ")
group_for_mult_group_test_1 = np.array([])
group_for_mult_group_test_2 = np.array([])
group_for_mult_group_test_3 = np.array([])
group_for_mult_group_test_4 = np.array([])
group_for_mult_group_test_5 = np.array([])

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="trustinvoting"
)

stat_value = 'Machine_Score_1'

try:


    # Spalte mit berechneten Werten füllen
    def get_all_values():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array

    def get_state_values(state):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = '{state}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_state_values_gender(state, gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = '{state}' AND Gender = '{gender}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_state_values_PL(state, pl):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = '{state}' AND Political_Leaning = '{pl}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_state_values_swing():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = 'Georgia' OR State = 'Nevada'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_state_values_NoSwing():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = 'Ohio' OR State = 'Louisiana' OR State = 'California'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_Swing_values_gender(gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'Georgia' OR State = 'Nevada') And Gender = '{gender}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_NoSwing_values_gender(gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'California' OR State = 'Ohio' OR State = 'Louisiana') And Gender = '{gender}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_Swing_values_PL(pl1):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = 'Georgia' OR State = 'Nevada' And Political_Leaning = '{pl1}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_NoSwing_values_PL(pl1):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'California' OR State = 'Ohio' OR State = 'Louisiana') And Political_Leaning = '{pl1}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array

    def get_BMD_values_gender(gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'Georgia' OR State = 'California') And Gender = '{gender}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_BMD_values_PL(pl1):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'California' OR State = 'Georgia') And Political_Leaning = '{pl1}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_DREw_values_gender(gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'Ohio' OR State = 'Nevada') And Gender = '{gender}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_DREw_values_PL(pl1):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE (State = 'Ohio' OR State = 'Nevada') And Political_Leaning = '{pl1}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array
    
    def get_gender(gender):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE Gender = '{gender}'"
        cursor.execute(query)
        buffer = cursor.fetchall()
        array = np.array([value[0] for value in buffer if value[0] is not None])
        cursor.close()
        return array
    
    def get_gender_PL(gender, PL):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE Gender = '{gender}' AND Political_Leaning = '{PL}'"
        cursor.execute(query)
        buffer = cursor.fetchall()
        array = np.array([value[0] for value in buffer if value[0] is not None])
        cursor.close()
        return array

    
    def kruskal_get_PL(pl):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE Political_Leaning = '{pl}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()       
        return group1
    
    def kruskal_get_Age(age):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE Age = '{age}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()       
        return group1
    
    def get_BMD():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = 'Georgia' OR State = 'California'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()       
        return group1
    
    def get_DREw():
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE State = 'Nevada' OR State = 'Ohio'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()       
        return group1

    def kruskal_Age():
        kruskal_wallis = stats.kruskal(kruskal_get_Age(1), kruskal_get_Age(2), kruskal_get_Age(3), kruskal_get_Age(4), kruskal_get_Age(5), kruskal_get_Age(6))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([kruskal_get_Age(1), kruskal_get_Age(2), kruskal_get_Age(3), kruskal_get_Age(4), kruskal_get_Age(5), kruskal_get_Age(6)], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")


    def kruskal_5():
        kruskal_wallis = stats.kruskal(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5)
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def kruskal_3():
        kruskal_wallis = stats.kruskal(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3)
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")



    def cal_mean_standard(group):
        mean1 = np.mean(group)
        modus1 = stats.mode(group, axis=None, keepdims=False)
        median1 = np.median(group)
        value_label_mean.config(text=f"Mean Non Swing State: {mean1}")
        value_label_modus.config(text=f"Modus Non Swing State: {modus1.mode}")
        value_label_median.config(text=f"Median Swing State: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_standard_Logic():
        field1 = input_field_state1.get()
        field2 = input_field_state2.get()
        if field2 == "":
            if field1 == 'bmd':
                group = get_BMD()
            elif field1 == 'overall':
                group = get_all_values()
            elif field1 == 'drew':
                group = get_DREw()
            elif field1 == 'swing':
                group = get_state_values_swing()
            elif field1 == 'noswing':
                group = get_state_values_NoSwing()
            elif field1 == 'male':
                group = get_gender('1')
            elif field1 == 'female':
                group = get_gender('2')
            elif field1 == 'democrat':
                group = kruskal_get_PL('1')
            elif field1 == 'republican':
                group = kruskal_get_PL('2')
            elif field1 == 'independent':
                group = kruskal_get_PL('3')
            else:
                group = get_state_values(field1)
        
        match field1:
            case 'swing':
                if field2 == 'male':
                    group = get_Swing_values_gender('1')
                elif field2 == 'female':
                    group = get_Swing_values_gender('2')
                elif field2 == 'democrat':
                    group = get_Swing_values_PL('1')
                elif field2 == 'independent':
                    group = get_Swing_values_PL('3')
                elif field2 == 'republican':
                    group = get_Swing_values_PL('2')
                else:
                    pass
            case 'noswing':
                if field2 == 'male':
                    group = get_NoSwing_values_gender('1')
                elif field2 == 'female':
                    group = get_NoSwing_values_gender('2')
                elif field2 == 'democrat':
                    group = get_NoSwing_values_PL('1')
                elif field2 == 'independent':
                    group = get_NoSwing_values_PL('3')
                elif field2 == 'republican':
                    group = get_NoSwing_values_PL('2')
                else:
                    pass
            case 'bmd':
                if field2 == 'male':
                    group = get_BMD_values_gender('1')
                elif field2 == 'female':
                    group = get_BMD_values_gender('2')
                elif field2 == 'democrat':
                    group = get_BMD_values_PL('1')
                elif field2 == 'independent':
                    group = get_BMD_values_PL('3')
                elif field2 == 'republican':
                    group = get_BMD_values_PL('2')
                else:
                    pass
            case 'drew':
                if field2 == 'male':
                    group = get_DREw_values_gender('1')
                elif field2 == 'female':
                    group = get_DREw_values_gender('2')
                elif field2 == 'democrat':
                    group = get_DREw_values_PL('1')
                elif field2 == 'independent':
                    group = get_DREw_values_PL('3')
                elif field2 == 'republican':
                    group = get_DREw_values_PL('2')
                else:
                    pass
            case 'democrat':
                if field2 == 'male':
                    group = get_gender_PL('1', '1')
                elif field2 == 'female':
                    group = get_gender_PL('2', '1')
            case 'republican':
                if field2 == 'male':
                    group = get_gender_PL('1', '2')
                elif field2 == 'female':
                    group = get_gender_PL('2', '2')
            case 'independent':
                if field2 == 'male':
                    group = get_gender_PL('1', '3')
                elif field2 == 'female':
                    group = get_gender_PL('2', '3')
            case _:
                if field2 == 'male':
                    group = get_state_values_gender(field1 ,'1')
                elif field2 == 'female':
                    group = get_state_values_gender(field1, '2')
                elif field2 == 'democrat':
                    group = get_state_values_PL(field1, '1')
                elif field2 == 'independent':
                    group = get_state_values_PL(field1, '3')
                elif field2 == 'republican':
                    group = get_state_values_PL(field1, '2')
                else:
                    pass
        return group
        
    
    def cal_mean_standard_Logic():
        group = cal_standard_Logic()
        field1 = input_field_state1.get()
        field2 = input_field_state2.get()
        mean1 = np.mean(group)
        modus1 = stats.mode(group, axis=None, keepdims=False)
        median1 = np.median(group)
        value_label_mean.config(text=f"Mean {field2}, {field1}: {mean1}")
        value_label_modus.config(text=f"Modus {field2}, {field1}: {modus1.mode}")
        value_label_median.config(text=f"Median {field2}, {field1}: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_MWU_standard_logic():
        group1 = group_for_mult_group_test_1
        group2 = group_for_mult_group_test_2
        mann_whitneyBMD = stats.mannwhitneyu(group1, group2, alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(group1, group2, alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(group1, group2, alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def set_group(number):
        global group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5
        if number == 1:
            group_for_mult_group_test_1 = cal_standard_Logic()
        elif number == 2:
            group_for_mult_group_test_2 = cal_standard_Logic()
        elif number == 3:
            group_for_mult_group_test_3 = cal_standard_Logic()
        elif number == 4:
            group_for_mult_group_test_4 = cal_standard_Logic()
        elif number == 5:
            group_for_mult_group_test_5 = cal_standard_Logic()

    def cal_chi_square():
        chi, pvalue = tn.chi_squared_test(group_for_mult_group_test_1, group_for_mult_group_test_2)
        
        value_label_2t.config(text=f"Chi-Square Value: {chi}")
        value_label_gr.config(text=f"Chi-Square p-value: {pvalue}")
        value_label_le.config(text=f"Mann-Whitney-U Less: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def cal_chi_square_3():
        chi, pvalue = tn.chi_squared_test_3(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3)
        
        value_label_2t.config(text=f"Chi-Square Value: {chi}")
        value_label_gr.config(text=f"Chi-Square p-value: {pvalue}")
        value_label_le.config(text=f"Mann-Whitney-U Less: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def cal_chi_square_5():
        chi, pvalue = tn.chi_squared_test_5(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5)
        
        value_label_2t.config(text=f"Chi-Square Value: {chi}")
        value_label_gr.config(text=f"Chi-Square p-value: {pvalue}")
        value_label_le.config(text=f"Mann-Whitney-U Less: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def get_trust_percent():
        trsut_p, noTrust_p, not_sure_p, trust, no_trust, not_sure = tn.trust_percent(group_for_mult_group_test_1)
        value_label_2t.config(text=f"Trust: {trsut_p}%")
        value_label_gr.config(text=f"No Trust: {noTrust_p}%")
        value_label_le.config(text=f"Not Sure: {not_sure_p}%")
        value_label_Kr.config(text=f"Trust: {trust}")
        value_label_dunn.config(text=f"No Trust: {no_trust}")
        value_label_modus.config(text=f"Not Sure: {not_sure}")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def coding_fact_number():
        listOfFactCodes = group_for_mult_group_test_1
        fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest = cf.fact_coding_count(listOfFactCodes)
        value_label_2t.config(text=f"machine fact: {machine_fact}")
        value_label_gr.config(text=f"election fact: {election_fact}")
        value_label_le.config(text=f"machine feeling: {election_feeling}")
        value_label_Kr.config(text=f"election feeling: {machine_feeling}")
        value_label_dunn.config(text=f"fake: {fake}")
        value_label_modus.config(text=f"")
        value_label_median.config(text=f"rest: {rest}")
        value_label_mean.config(text=f"misc: {misc}")

    def coding_fact_number_perc():
        listOfFactCodes = group_for_mult_group_test_1
        amount = listOfFactCodes.size
        fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest = cf.fact_coding_percent(cf.fact_coding_count(listOfFactCodes)[0], cf.fact_coding_count(listOfFactCodes)[1], cf.fact_coding_count(listOfFactCodes)[2], cf.fact_coding_count(listOfFactCodes)[3], cf.fact_coding_count(listOfFactCodes)[4], cf.fact_coding_count(listOfFactCodes)[5], cf.fact_coding_count(listOfFactCodes)[6], amount)
        value_label_2t.config(text=f"machine fact: {round(machine_fact,3)}%")
        value_label_gr.config(text=f"election fact: {round(election_fact,3)}%")
        value_label_le.config(text=f"machine feeling: {round(election_feeling,3)}%")
        value_label_Kr.config(text=f"election feeling: {round(machine_feeling,3)}%")
        value_label_dunn.config(text=f"fake: {round(fake,3)}%")
        value_label_modus.config(text=f"")
        value_label_median.config(text=f"rest: {round(rest,3)}%")
        value_label_mean.config(text=f"misc: {round(misc,3)}%")

    def coding_number():
        listOfFactCodes = group_for_mult_group_test_1
        neutral, name, llm, hacking_pos, hacking_neg, news, error_pos, error_neg, tested, usability, secret_pos, secret_neg, government, dominion, verifiable_pos, verifiable_neg, believe, detection, transparent, rest = cf.coding_count(listOfFactCodes)
        value_label_2t.config(text=f"neutral: {neutral}, name: {name}, LLM: {llm}")
        value_label_gr.config(text=f"hacking_pos: {hacking_pos}, news: {news}, error_pos: {error_pos}")
        value_label_le.config(text=f"tested: {tested}, usability: {usability}, secret_pos: {secret_pos}")
        value_label_Kr.config(text=f"government: {government}, dominion: {dominion}, verifiable_pos: {verifiable_pos}")
        value_label_dunn.config(text=f"believe: {believe}, detection: {detection}, transparent: {transparent}")
        value_label_modus.config(text=f"hacking_neg: {hacking_neg}, error_neg: {error_neg}, secret_neg: {secret_neg}")
        value_label_median.config(text=f"verifiable_neg: {verifiable_neg}, rest: {rest}")
        value_label_median.config(text=f"")
        value_label_mean.config(text=f"verifiable_neg: {verifiable_neg}, rest: {rest}")

    def coding_number_perc():
        listOfFactCodes = group_for_mult_group_test_1
        amount = listOfFactCodes.size
        neutral, name, llm, hacking_pos, hacking_neg, news, error_pos, error_neg, tested, usability, secret_pos, secret_neg, government, dominion, verifiable_pos, verifiable_neg, believe, detection, transparent, rest = cf.coding_count_p(cf.coding_count(listOfFactCodes)[0], cf.coding_count(listOfFactCodes)[1], cf.coding_count(listOfFactCodes)[2], cf.coding_count(listOfFactCodes)[3], cf.coding_count(listOfFactCodes)[4], cf.coding_count(listOfFactCodes)[5], cf.coding_count(listOfFactCodes)[6], cf.coding_count(listOfFactCodes)[7], cf.coding_count(listOfFactCodes)[8], cf.coding_count(listOfFactCodes)[9], cf.coding_count(listOfFactCodes)[10], cf.coding_count(listOfFactCodes)[11], cf.coding_count(listOfFactCodes)[12], cf.coding_count(listOfFactCodes)[13], cf.coding_count(listOfFactCodes)[14], cf.coding_count(listOfFactCodes)[15], amount)
        value_label_2t.config(text=f"neutral: {round(neutral, 3)}%, name: {round(name, 3)}%, LLM: {round(llm, 3)}%")
        value_label_gr.config(text=f"hacking_pos: {round(hacking_pos, 3)}%, news: {round(news, 3)}%, error_pos: {round(error_pos, 3)}%")
        value_label_le.config(text=f"tested: {round(tested, 3)}%, usability: {round(usability, 3)}%, secret_pos: {round(secret_pos, 3)}%")
        value_label_Kr.config(text=f"government: {round(government, 3)}%, dominion: {round(dominion, 3)}%, verifiable_pos: {round(verifiable_pos, 3)}%")
        value_label_dunn.config(text=f"believe: {round(believe, 3)}%, detection: {round(detection, 3)}%, transparent: {round(transparent, 3)}%")
        value_label_modus.config(text=f"hacking_neg: {round(hacking_neg, 3)}%, error_neg: {round(error_neg, 3)}%, secret_neg: {round(secret_neg, 3)}%")
        value_label_median.config(text=f"verifiable_neg: {round(verifiable_neg, 3)}%; rest: {round(rest, 3)}%")
        value_label_mean.config(text=f"")

    def draw_pie_trust():
        dd.drawPie_trust(group_for_mult_group_test_1)

    def draw_pie_fact_code():
        dd.drawPie_fact_code(group_for_mult_group_test_1)

    def draw_bars_2():
        dd.drawStockBar_trust_2(group_for_mult_group_test_1, group_for_mult_group_test_2)
    
    def draw_bars_3():
        dd.drawStockBar_trust_3(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3)

    def draw_bars_5():
        dd.drawStockBar_trust_5(group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5)

    def filter_data():
        global group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5
        if group_for_mult_group_test_1.size != 0:
            group_for_mult_group_test_1 = fi.filter_outliers_iqr(group_for_mult_group_test_1)
        if group_for_mult_group_test_2.size != 0:
            group_for_mult_group_test_2 = fi.filter_outliers_iqr(group_for_mult_group_test_2)
        if group_for_mult_group_test_3.size != 0:
            group_for_mult_group_test_3 = fi.filter_outliers_iqr(group_for_mult_group_test_3)
        if group_for_mult_group_test_4.size != 0:
            group_for_mult_group_test_4 = fi.filter_outliers_iqr(group_for_mult_group_test_4)
        if group_for_mult_group_test_5.size != 0:
            group_for_mult_group_test_5 = fi.filter_outliers_iqr(group_for_mult_group_test_5)
            

    #d ist array mit den Werten für die Boxplot-Darstellung, also Array von Arrays
    def draw_boxplot(nu):
        number = int(nu)
        if number == 1:
            d = [group_for_mult_group_test_1]
        elif number == 2:
            d = [group_for_mult_group_test_1, group_for_mult_group_test_2]
        elif number == 3:
            d = [group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3]
        elif number == 4:
            d = [group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4]
        elif number == 5:
            d = [group_for_mult_group_test_1, group_for_mult_group_test_2, group_for_mult_group_test_3, group_for_mult_group_test_4, group_for_mult_group_test_5]
        else:
            d = [group_for_mult_group_test_1]

        if stat_value == "TVS_Score":
            label_name = "TVS Score"
        elif stat_value == "Overall_Trust":
            label_name = "Overall Trust"
        elif stat_value == "Machine_Score_1":
            label_name = "Own Score"
        else:
            label_name = ""     
        
        labeling_boxes = [f"Group {i+1}" for i in range(number)]
        print(group_for_mult_group_test_1, group_for_mult_group_test_2)
        plt.figure(figsize =(10, 7))
        plt.boxplot(d, labels = labeling_boxes)
        plt.ylabel(label_name)
        plt.title(f"Boxplot of for {label_name}")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    def normal_distribution():
        shaprio, ks_test = nd.normal_distribution_analysis(group_for_mult_group_test_1, input_title_Histogram.get())
        value_label_2t.config(text=f"Shapiro: {shaprio.pvalue}")
        value_label_gr.config(text=f"ks test: {ks_test.pvalue}")
        value_label_Kr.config(text=f"")
        value_label_dunn.config(text=f"")
        value_label_modus.config(text=f"")
        value_label_median.config(text=f"")
        value_label_mean.config(text=f"")

    def tuekey(number):
        print('in funktion')
        gruppen_werte = []
        gruppen_werte.append(group_for_mult_group_test_1)
        gruppen_werte.append(group_for_mult_group_test_2)
        gruppen_werte.append(group_for_mult_group_test_3)
        if number == 5:
            gruppen_werte.append(group_for_mult_group_test_4)
            gruppen_werte.append(group_for_mult_group_test_5)
        data = []
        gruppen_namen = []
        for i, gruppe in enumerate(gruppen_werte):
            data.extend(gruppe)
            gruppen_namen.extend([f'Gruppe {i+1}'] * len(gruppe))

        df = pd.DataFrame({'Werte': data, 'Gruppe': gruppen_namen})
        if gruppen_werte[0].size != 0:
            print('in IF')
            tukey_result = pairwise_tukeyhsd(df['Werte'], df['Gruppe'], alpha=0.05) # alpha ist das Signifikanzniveau
            result = pd.DataFrame(data=tukey_result._results_table.data[1:], columns=tukey_result._results_table.data[0])
            print(result)
            return result
        else:
            print('empty')

    # Create the main window
    root = tk.Tk()
    root.title("Stats for Trust in Voting")

    # Create labels to display the values
    value_label_2t = tk.Label(root, text="Mann-Whitney-U 2 Tail: ")
    value_label_2t.pack()

    value_label_gr = tk.Label(root, text="Mann-Whitney-U Greater: ")
    value_label_gr.pack()

    value_label_le = tk.Label(root, text="Mann-Whitney-U Less: ")
    value_label_le.pack()

    value_label_Kr = tk.Label(root, text="Kruskal-Wallis: ")
    value_label_Kr.pack()

    value_label_dunn = tk.Label(root, text="Dunn-Test: ")
    value_label_dunn.pack()

    value_label_mean = tk.Label(root, text="Mean: ")
    value_label_mean.pack()
    value_label_median = tk.Label(root, text="Median: ")
    value_label_median.pack()
    value_label_modus = tk.Label(root, text="Modus: ")
    value_label_modus.pack()

    # Feste Fenstergröße einstellen
    root.geometry("900x700")  # Breite x Höhe

    # Create an input field
    input_field_state1 = tk.Entry(root, width=30)
    input_field_state1.pack(pady=10)
    input_field_state2 = tk.Entry(root, width=30)
    input_field_state2.pack(pady=10)

    # Create the 'Save' button

    kruskalAge_button = tk.Button(root, text="Kruskal-Mann Age", command=kruskal_Age)
    kruskalAge_button.pack()
    kruskalAge_button.place(x=30, y=400)

    group_kruskal_button5 = tk.Button(root, text="Kruskal 5 group", command=kruskal_5)
    group_kruskal_button5.pack()
    group_kruskal_button5.place(x=150, y=400)

    group_kruskal_button3 = tk.Button(root, text="Kruskal 3 group", command=kruskal_3)
    group_kruskal_button3.pack()
    group_kruskal_button3.place(x=300, y=400)


    mean_button_subgroup = tk.Button(root, text="Mean/Median/Modus Subgroups", command=cal_mean_standard_Logic)
    mean_button_subgroup.pack()
    mean_button_subgroup.place(x=30, y=450)

    set_group1 = tk.Button(root, text="set group 1", command=lambda: set_group(1))
    set_group1.pack()
    set_group1.place(x=230, y=450)

    set_group2 = tk.Button(root, text="set group 2", command=lambda: set_group(2))
    set_group2.pack()
    set_group2.place(x=330, y=450)

    set_group3 = tk.Button(root, text="set group 3", command=lambda: set_group(3))
    set_group3.pack()
    set_group3.place(x=430, y=450)

    set_group4 = tk.Button(root, text="set group 4", command=lambda: set_group(4))
    set_group4.pack()
    set_group4.place(x=530, y=450)

    set_group5 = tk.Button(root, text="set group 5", command=lambda: set_group(5))
    set_group5.pack()
    set_group5.place(x=630, y=450)

    mean_button_set_group2 = tk.Button(root, text="Mann Whitney set groups", command=cal_MWU_standard_logic)
    mean_button_set_group2.pack()
    mean_button_set_group2.place(x=400, y=400)

    draw_boxplot_button = tk.Button(root, text="Draw Boxplot Subgroups", command=lambda: draw_boxplot(input_field_state1.get()))
    draw_boxplot_button.pack()
    draw_boxplot_button.place(x=600, y=300)

    chi_square_button = tk.Button(root, text="Chi Square for 2 groups", command=cal_chi_square)
    chi_square_button.pack()
    chi_square_button.place(x=30, y=350)

    chi_square_3_button = tk.Button(root, text="Chi Square for 3 groups", command=cal_chi_square_3)
    chi_square_3_button.pack()
    chi_square_3_button.place(x=180, y=350)

    chi_square_3_button = tk.Button(root, text="Chi Square for 5 groups", command=cal_chi_square_5)
    chi_square_3_button.pack()
    chi_square_3_button.place(x=330, y=350)

    trust_percent_button = tk.Button(root, text="Trust Percent", command=get_trust_percent)
    trust_percent_button.pack()
    trust_percent_button.place(x=480, y=350)

    code_fact_button = tk.Button(root, text="Fact Codes", command=coding_fact_number)
    code_fact_button.pack()
    code_fact_button.place(x=600, y=180)

    code_fact_percent_button = tk.Button(root, text="Fact Code %", command=coding_fact_number_perc)
    code_fact_percent_button.pack()
    code_fact_percent_button.place(x=600, y=150)

    code__button = tk.Button(root, text="Codes", command=coding_number)
    code__button.pack()
    code__button.place(x=600, y=240)

    code_percent_button = tk.Button(root, text="Code %", command=coding_number_perc)
    code_percent_button.pack()
    code_percent_button.place(x=600, y=210)

    draw_pie_fact_button = tk.Button(root, text="Draw Pie Chart about Fact Codes", command=draw_pie_fact_code)
    draw_pie_fact_button.pack()
    draw_pie_fact_button.place(x=680, y=240)

    draw_pie_trust_percent_button = tk.Button(root, text="Draw Pie Chart about Trust", command=draw_pie_trust)
    draw_pie_trust_percent_button.pack()
    draw_pie_trust_percent_button.place(x=680, y=210)

    draw_bar_2_button = tk.Button(root, text="Draw Stackbar about Trust (2)", command=draw_bars_2)
    draw_bar_2_button.pack()
    draw_bar_2_button.place(x=680, y=120)

    draw_bar_3_button = tk.Button(root, text="Draw Stackbar about Trust (3)", command=draw_bars_3)
    draw_bar_3_button.pack()
    draw_bar_3_button.place(x=680, y=150)

    draw_bar_5_button = tk.Button(root, text="Draw Stackbar about Trust (5)", command=draw_bars_5)
    draw_bar_5_button.pack()
    draw_bar_5_button.place(x=680, y=180)

    filter_button = tk.Button(root, text="IQR 1,5 Filter", command=filter_data)
    filter_button.pack()
    filter_button.place(x=680, y=270)

    tukey_butt = tk.Button(root, text="Tukey HSD 3", command=lambda: tuekey(3))
    tukey_butt.pack()
    tukey_butt.place(x=150, y=500)

    tukey_butt5 = tk.Button(root, text="Tukey HSD 5", command=lambda: tuekey(5))
    tukey_butt5.pack()
    tukey_butt5.place(x=240, y=500)

    normal_distribution_button = tk.Button(root, text="Normal Distribution", command=normal_distribution)
    normal_distribution_button.pack()
    normal_distribution_button.place(x=30, y=500)

    histo_label = tk.Label(root, text="Histo Title: ")
    histo_label.pack()
    histo_label.place(x=30, y=540)
    input_title_Histogram = tk.Entry(root, width=30)
    input_title_Histogram.pack(pady=10)
    input_title_Histogram.place(x=150, y=540)

    # Create a variable to store the selected option
    selected_option = tk.StringVar(value="TVS Score")

    # Function to handle option selection
    def update_stat_value():
        global stat_value
        stat_value = selected_option.get()
        print(f"Selected option: {stat_value}")


    # Create radio buttons for the selection options
    radio_tvs = tk.Radiobutton(root, text="TVS Score", variable=selected_option, value="TVS_Score", command=update_stat_value)
    radio_tvs.pack()
    radio_tvs.place(x=30, y=270)

    radio_overall = tk.Radiobutton(root, text="Overall Trust", variable=selected_option, value="Overall_Trust", command=update_stat_value)
    radio_overall.pack()
    radio_overall.place(x=30, y=290)

    radio_own = tk.Radiobutton(root, text="Own Score", variable=selected_option, value="Machine_Score_1", command=update_stat_value)
    radio_own.pack()
    radio_own.place(x=30, y=310)

    radio_trust = tk.Radiobutton(root, text="Trust / No Trust", variable=selected_option, value="Do_you_trust", command=update_stat_value)
    radio_trust.pack()
    radio_trust.place(x=30, y=10)

    radio_others = tk.Radiobutton(root, text="Trust in other", variable=selected_option, value="Trust_In_Others", command=update_stat_value)
    radio_others.pack()
    radio_others.place(x=30, y=30)

    radio_Tech = tk.Radiobutton(root, text="Trust in Technology", variable=selected_option, value="Trust_Technology", command=update_stat_value)
    radio_Tech.pack()
    radio_Tech.place(x=30, y=50)

    radio_Cast = tk.Radiobutton(root, text="Cast Ballot Reflects Intended Selections", variable=selected_option, value="Cast_Ballot", command=update_stat_value)
    radio_Cast.pack()
    radio_Cast.place(x=30, y=70)

    radio_Anon = tk.Radiobutton(root, text="Anonymous", variable=selected_option, value="Anonymous", command=update_stat_value)
    radio_Anon.pack()
    radio_Anon.place(x=30, y=90)

    radio_trans = tk.Radiobutton(root, text="Transparency", variable=selected_option, value="Transparency", command=update_stat_value)
    radio_trans.pack()
    radio_trans.place(x=30, y=110)

    radio_Rel = tk.Radiobutton(root, text="Reliability", variable=selected_option, value="Reliability", command=update_stat_value)
    radio_Rel.pack()
    radio_Rel.place(x=30, y=130)

    radio_SysSec = tk.Radiobutton(root, text="System Security", variable=selected_option, value="Sys_Security", command=update_stat_value)
    radio_SysSec.pack()
    radio_SysSec.place(x=30, y=150)

    radio_usab = tk.Radiobutton(root, text="Usability", variable=selected_option, value="Usability", command=update_stat_value)
    radio_usab.pack()
    radio_usab.place(x=30, y=170)

    radio_acc_count = tk.Radiobutton(root, text="Accuracy Counted", variable=selected_option, value="Accurately_Counted", command=update_stat_value)
    radio_acc_count.pack()
    radio_acc_count.place(x=30, y=190)

    radio_accuracy = tk.Radiobutton(root, text="System Accuracy", variable=selected_option, value="Accuracy", command=update_stat_value)
    radio_accuracy.pack()
    radio_accuracy.place(x=30, y=210)

    radio_fact_code = tk.Radiobutton(root, text="Fact Codes", variable=selected_option, value="Factbased_reason", command=update_stat_value)
    radio_fact_code.pack()
    radio_fact_code.place(x=30, y=230)

    radio_other_fact_code = tk.Radiobutton(root, text="Other Codes", variable=selected_option, value="codes_open_question", command=update_stat_value)
    radio_other_fact_code.pack()
    radio_other_fact_code.place(x=30, y=250)

    # Run the Tkinter event loop
    root.mainloop()


finally:
    # Close the cursor and connection
    connection.close()