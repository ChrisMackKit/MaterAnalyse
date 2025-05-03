import getpass
import mysql.connector
import numpy as np
from scipy import stats
import tkinter as tk
import matplotlib.pyplot as plt
import statsmodels.api as sm
import tkinter.scrolledtext as scrolledtext
import scikit_posthocs as sp
import trust_notrust as tn
import codingFunction as cf
import drawDiagrams as dd

# Prompt the user for the MySQL password
password = getpass.getpass("Enter your MySQL password: ")
group_for_mult_group_test_1 = []
group_for_mult_group_test_2 = []
group_for_mult_group_test_3 = []
group_for_mult_group_test_4 = []
group_for_mult_group_test_5 = []

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
    

    # Function to handle the 'Next' button click
    def mann_whitney():
        state1 = input_field_state1.get()
        state2 = input_field_state2.get()
        mann_whitneyBMD = stats.mannwhitneyu(get_state_values(state1), get_state_values(state2), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(get_state_values(state1), get_state_values(state2), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(get_state_values(state1), get_state_values(state2), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def mann_whitneySNS():
        mann_whitneyBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def mann_whitney_Gender():
        mann_whitneyBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def mann_whitney_PL():
        state1 = input_field_state1.get()
        state2 = input_field_state2.get()
        if state1 == 'democrat':
            state1 = '1'
        elif state1 == 'independent':
            state1 = '3'
        elif state1 == 'republican':
            state1 = '2'
        if state2 == 'democrat':
            state2 = '1'
        elif state2 == 'independent':
            state2 = '3'
        elif state2 == 'republican':
            state2 = '2'
        mann_whitneyBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def kruskal_PL():
        kruskal_wallis = stats.kruskal(kruskal_get_PL(1), kruskal_get_PL(2), kruskal_get_PL(3))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([kruskal_get_PL(1), kruskal_get_PL(2), kruskal_get_PL(3)], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

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

    def kruskal_NS():
        kruskal_wallis = stats.kruskal(get_state_values('California'), get_state_values('Ohio'), get_state_values('Louisiana'))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([get_state_values('California'), get_state_values('Ohio'), get_state_values('Louisiana')], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")

    def kruskal_All_States():
        kruskal_wallis = stats.kruskal(get_state_values('Georgia'), get_state_values('California'), get_state_values('Nevada'), get_state_values('Ohio'), get_state_values('Louisiana'))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([get_state_values('Georgia'), get_state_values('California'), get_state_values('Nevada'), get_state_values('Ohio'), get_state_values('Louisiana')], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_modus.config(text=f"Modus: ")
        value_label_median.config(text=f"Median: ")
        value_label_mean.config(text=f"Mean: ")


    def calc_mean():
        state1 = input_field_state1.get()
        mean1 = np.mean(get_state_values(state1))
        value_label_mean.config(text=f"Mean {state1}: {mean1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        cal_median()
        cal_modus()

    def cal_median():
        state1 = input_field_state1.get()
        median1 = np.median(get_state_values(state1))
        value_label_median.config(text=f"Median {state1}: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    
    def cal_modus():
        state1 = input_field_state1.get()
        modus1 = stats.mode(get_state_values(state1), axis=None, keepdims=False)
        value_label_modus.config(text=f"Modus {state1}: {modus1.mode}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def calc_mean_gen():
        state1 = input_field_state1.get()
        if state1 == 'female':
            state1_ = '2'
        elif state1 == 'male':
            state1_ = '1'
        elif state1 == 'other':
            state1_ = '3'
        mean1 = np.mean(get_gender(state1_))
        value_label_mean.config(text=f"Mean {state1}: {mean1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        cal_median_gen()
        cal_modus_gen()

    def cal_median_gen():
        state1 = input_field_state1.get()
        if state1 == 'female':
            state1_ = '2'
        elif state1 == 'male':
            state1_ = '1'
        elif state1 == 'other':
            state1_ = '3'
        median1 = np.median(get_gender(state1_))
        value_label_median.config(text=f"Median {state1}: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    
    def cal_modus_gen():
        state1 = input_field_state1.get()
        if state1 == 'female':
            state1_ = '2'
        elif state1 == 'male':
            state1_ = '1'
        elif state1 == 'other':
            state1_ = '3'
        modus1 = stats.mode(get_gender(state1_), axis=None, keepdims=False)
        value_label_modus.config(text=f"Modus {state1}: {modus1.mode}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def calc_mean_PL():
        state1 = input_field_state1.get()
        if state1 == 'democrat':
            state1_ = '1'
        elif state1 == 'republican':
            state1_ = '2'
        elif state1 == 'independent':
            state1_ = '3'
        mean1 = np.mean(get_gender(state1_))
        value_label_mean.config(text=f"Mean {state1}: {mean1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        cal_modus_PL()
        cal_median_PL()

    def cal_median_PL():
        state1 = input_field_state1.get()
        if state1 == 'democrat':
            state1_ = '1'
        elif state1 == 'republican':
            state1_ = '2'
        elif state1 == 'independent':
            state1_ = '3'
        median1 = np.median(get_gender(state1_))
        value_label_median.config(text=f"Median {state1}: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    
    def cal_modus_PL():
        state1 = input_field_state1.get()
        if state1 == 'democrat':
            state1_ = '1'
        elif state1 == 'republican':
            state1_ = '2'
        elif state1 == 'independent':
            state1_ = '3'
        modus1 = stats.mode(get_gender(state1_), axis=None, keepdims=False)
        value_label_modus.config(text=f"Modus {state1}: {modus1.mode}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_mean_S():
        mean1 = np.mean(get_state_values_swing())
        modus1 = stats.mode(get_state_values_swing(), axis=None, keepdims=False)
        median1 = np.median(get_state_values_swing())
        value_label_mean.config(text=f"Mean Swing State: {mean1}")
        value_label_modus.config(text=f"Modus Swing State: {modus1.mode}")
        value_label_median.config(text=f"Median Swing State: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_mean_NS():
        mean1 = np.mean(get_state_values_NoSwing())
        modus1 = stats.mode(get_state_values_NoSwing(), axis=None, keepdims=False)
        median1 = np.median(get_state_values_NoSwing())
        value_label_mean.config(text=f"Mean Non Swing State: {mean1}")
        value_label_modus.config(text=f"Modus Non Swing State: {modus1.mode}")
        value_label_median.config(text=f"Median Swing State: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_mean_BMD():
        mean1 = np.mean(get_BMD())
        modus1 = stats.mode(get_BMD(), axis=None, keepdims=False)
        median1 = np.median(get_BMD())
        value_label_mean.config(text=f"Mean Non Swing State: {mean1}")
        value_label_modus.config(text=f"Modus Non Swing State: {modus1.mode}")
        value_label_median.config(text=f"Median Swing State: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def cal_mean_DREw():
        mean1 = np.mean(get_DREw())
        modus1 = stats.mode(get_DREw(), axis=None, keepdims=False)
        median1 = np.median(get_DREw())
        value_label_mean.config(text=f"Mean Non Swing State: {mean1}")
        value_label_modus.config(text=f"Modus Non Swing State: {modus1.mode}")
        value_label_median.config(text=f"Median Swing State: {median1}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

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
        mann_whitneyBMD = stats.mannwhitneyu(group_for_mult_group_test_1, group_for_mult_group_test_2, alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(group_for_mult_group_test_1, group_for_mult_group_test_2, alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(group_for_mult_group_test_1, group_for_mult_group_test_2, alternative='less')
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
        trsut_p, noTrust_p, not_sure_p = tn.trust_percent(group_for_mult_group_test_1)
        value_label_2t.config(text=f"Trust: {trsut_p}%")
        value_label_gr.config(text=f"No Trust: {noTrust_p}%")
        value_label_le.config(text=f"Not Sure: {not_sure_p}%")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")
        value_label_modus.config(text=f"Modus: ")
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
        fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest = cf.fact_coding_percent(cf.fact_coding_count(listOfFactCodes)[0], cf.fact_coding_count(listOfFactCodes)[1], cf.fact_coding_count(listOfFactCodes)[2], cf.fact_coding_count(listOfFactCodes)[3], cf.fact_coding_count(listOfFactCodes)[4], cf.fact_coding_count(listOfFactCodes)[5], cf.fact_coding_count(listOfFactCodes)[6])
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
        neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest = cf.coding_count(listOfFactCodes)
        value_label_2t.config(text=f"neutral: {neutral}, name: {name}, LLM: {llm}")
        value_label_gr.config(text=f"hacking: {hacking}, news: {news}, error: {error}")
        value_label_le.config(text=f"tested: {tested}, usability: {usability}, secret: {secret}")
        value_label_Kr.config(text=f"government: {government}, dominion: {dominion}, verifiable: {verifiable}")
        value_label_dunn.config(text=f"believe: {believe}, detection: {detection}, transparent: {transparent}")
        value_label_modus.config(text=f"")
        value_label_median.config(text=f"rest: {rest}")
        value_label_mean.config(text=f"")

    def coding_number_perc():
        listOfFactCodes = group_for_mult_group_test_1
        neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest = cf.coding_count_p(cf.coding_count(listOfFactCodes)[0], cf.coding_count(listOfFactCodes)[1], cf.coding_count(listOfFactCodes)[2], cf.coding_count(listOfFactCodes)[3], cf.coding_count(listOfFactCodes)[4], cf.coding_count(listOfFactCodes)[5], cf.coding_count(listOfFactCodes)[6], cf.coding_count(listOfFactCodes)[7], cf.coding_count(listOfFactCodes)[8], cf.coding_count(listOfFactCodes)[9], cf.coding_count(listOfFactCodes)[10], cf.coding_count(listOfFactCodes)[11], cf.coding_count(listOfFactCodes)[12], cf.coding_count(listOfFactCodes)[13], cf.coding_count(listOfFactCodes)[14], cf.coding_count(listOfFactCodes)[15])
        value_label_2t.config(text=f"neutral: {round(neutral, 3)}%, name: {round(name, 3)}%, LLM: {round(llm, 3)}%")
        value_label_gr.config(text=f"hacking: {round(hacking, 3)}%, news: {round(news, 3)}%, error: {round(error, 3)}%")
        value_label_le.config(text=f"tested: {round(tested, 3)}%, usability: {round(usability, 3)}%, secret: {round(secret, 3)}%")
        value_label_Kr.config(text=f"government: {round(government, 3)}%, dominion: {round(dominion, 3)}%, verifiable: {round(verifiable, 3)}%")
        value_label_dunn.config(text=f"believe: {round(believe, 3)}%, detection: {round(detection, 3)}%, transparent: {round(transparent, 3)}%")
        value_label_modus.config(text=f"")
        value_label_median.config(text=f"rest: {round(rest, 3)}%")
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

    # Create the 'Next' button
    MW_button = tk.Button(root, text="Mann-Whitney States", command=mann_whitney)
    MW_button.pack() 
    MW_button.place(x=30, y=400)
    MWSNS_button = tk.Button(root, text="Mann-Whitney Swing v NoSwing", command=mann_whitneySNS)
    MWSNS_button.pack()
    MWSNS_button.place(x=180, y=400)
    MWG_button = tk.Button(root, text="Mann-Whitney Gender", command=mann_whitney_Gender)
    MWG_button.pack() 
    MWG_button.place(x=380, y=400)
    MW_PL_button = tk.Button(root, text="Mann-Whitney Political Leaning", command=mann_whitney_PL)
    MW_PL_button.pack()
    MW_PL_button.place(x=530, y=400)

    # Create an input field
    input_field_state1 = tk.Entry(root, width=30)
    input_field_state1.pack(pady=10)
    input_field_state2 = tk.Entry(root, width=30)
    input_field_state2.pack(pady=10)

    # Create the 'Save' button
    kruskalPL_button = tk.Button(root, text="Kruskal-Mann Political Leaning", command=kruskal_PL)
    kruskalPL_button.pack()
    kruskalPL_button.place(x=30, y=450)
    kruskalAge_button = tk.Button(root, text="Kruskal-Mann Age", command=kruskal_Age)
    kruskalAge_button.pack()
    kruskalAge_button.place(x=230, y=450)
    kruskalNS_button = tk.Button(root, text="Kruskal-Mann No Swing States", command=kruskal_NS)
    kruskalNS_button.pack()
    kruskalNS_button.place(x=380, y=450)
    kruskal_All_States_button = tk.Button(root, text="Kruskal-Mann All States", command=kruskal_All_States)
    kruskal_All_States_button.pack()
    kruskal_All_States_button.place(x=580, y=450)

    mean_button = tk.Button(root, text="Mean/Median/Modus", command=calc_mean)
    mean_button.pack()
    mean_button.place(x=30, y=500)


    mean_button_gen = tk.Button(root, text="Mean/Median/Modus Gender", command=calc_mean_gen)
    mean_button_gen.pack()
    mean_button_gen.place(x=230, y=500)


    mean_button_PL = tk.Button(root, text="Mean/Median/Modus Poli Leaning", command=calc_mean_PL)
    mean_button_PL.pack()
    mean_button_PL.place(x=430, y=500)

    mean_button_SS = tk.Button(root, text="Mean/Median/Modus Swing State", command=cal_mean_S)
    mean_button_SS.pack()
    mean_button_SS.place(x=30, y=550)

    mean_button_NSS = tk.Button(root, text="Mean/Median/Modus No Swing State", command=cal_mean_NS)
    mean_button_NSS.pack()
    mean_button_NSS.place(x=230, y=550)

    mean_button_BMD = tk.Button(root, text="Mean/Median/Modus BMD", command=cal_mean_BMD)
    mean_button_BMD.pack()
    mean_button_BMD.place(x=30, y=600)

    mean_button_DREw = tk.Button(root, text="Mean/Median/Modus DREw", command=cal_mean_DREw)
    mean_button_DREw.pack()
    mean_button_DREw.place(x=230, y=600)

    mean_button_subgroup = tk.Button(root, text="Mean/Median/Modus Subgroups", command=cal_mean_standard_Logic)
    mean_button_subgroup.pack()
    mean_button_subgroup.place(x=30, y=650)

    set_group1 = tk.Button(root, text="set group 1", command=lambda: set_group(1))
    set_group1.pack()
    set_group1.place(x=230, y=650)

    set_group2 = tk.Button(root, text="set group 2", command=lambda: set_group(2))
    set_group2.pack()
    set_group2.place(x=330, y=650)

    set_group3 = tk.Button(root, text="set group 3", command=lambda: set_group(3))
    set_group3.pack()
    set_group3.place(x=430, y=650)

    set_group4 = tk.Button(root, text="set group 4", command=lambda: set_group(4))
    set_group4.pack()
    set_group4.place(x=530, y=650)

    set_group5 = tk.Button(root, text="set group 5", command=lambda: set_group(5))
    set_group5.pack()
    set_group5.place(x=630, y=650)

    mean_button_set_group2 = tk.Button(root, text="Mann Whitney set groups", command=cal_MWU_standard_logic)
    mean_button_set_group2.pack()
    mean_button_set_group2.place(x=610, y=600)

    draw_boxplot_button = tk.Button(root, text="Draw Boxplot Subgroups", command=lambda: draw_boxplot(input_field_state1.get()))
    draw_boxplot_button.pack()
    draw_boxplot_button.place(x=430, y=600)

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

    radio_overall = tk.Radiobutton(root, text="Overall Trust", variable=selected_option, value="Overall_Trust", command=update_stat_value)
    radio_overall.pack()

    radio_own = tk.Radiobutton(root, text="Own Score", variable=selected_option, value="Machine_Score_1", command=update_stat_value)
    radio_own.pack()

    radio_trust = tk.Radiobutton(root, text="Trust / No Trust", variable=selected_option, value="Do_you_trust", command=update_stat_value)
    radio_trust.pack()

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