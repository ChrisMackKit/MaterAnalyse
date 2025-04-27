import getpass
import mysql.connector
import numpy as np
from scipy import stats
import tkinter as tk
import matplotlib.pyplot as plt
import statsmodels.api as sm
import tkinter.scrolledtext as scrolledtext
import scikit_posthocs as sp

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
                group = get_DREw('2')
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
        print("Standard Logic Func: ", group)
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
        print(f"Group: ", group_for_mult_group_test_1)

    
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
    root.geometry("800x750")  # Breite x Höhe

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
    mean_button_set_group2.place(x=230, y=700)

    draw_boxplot_button = tk.Button(root, text="Draw Boxplot Subgroups", command=lambda: draw_boxplot(input_field_state1.get()))
    draw_boxplot_button.pack()
    draw_boxplot_button.place(x=30, y=700)

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


    # Run the Tkinter event loop
    root.mainloop()


finally:
    # Close the cursor and connection
    connection.close()