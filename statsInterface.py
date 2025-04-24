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

    def mann_whitneySNS():
        mann_whitneyBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(get_state_values_swing(), get_state_values_NoSwing(), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def mann_whitney_Gender():
        mann_whitneyBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(get_gender('1'), get_gender('2'), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def mann_whitney_PL():
        state1 = input_field_state1.get()
        state2 = input_field_state2.get()
        if state1 == 'Democrat':
            state1 = '1'
        elif state1 == 'Independent':
            state1 = '3'
        elif state1 == 'Republican':
            state1 = '2'
        if state2 == 'Democrat':
            state2 = '1'
        elif state2 == 'Independent':
            state2 = '3'
        elif state2 == 'Republican':
            state2 = '2'
        mann_whitneyBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='two-sided')
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: {mann_whitneyBMD.pvalue}")
        mann_whitneyGreaterBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='greater')
        value_label_gr.config(text=f"Mann-Whitney-U Greater: {mann_whitneyGreaterBMD.pvalue}")
        mann_whitneyLessBMD = stats.mannwhitneyu(kruskal_get_PL(state1), kruskal_get_PL(state2), alternative='less')
        value_label_le.config(text=f"Mann-Whitney-U Less: {mann_whitneyLessBMD.pvalue}")
        value_label_Kr.config(text=f"Kruskal-Wallis: ")
        value_label_dunn.config(text=f"Dunn-Test: ")

    def kruskal_PL():
        kruskal_wallis = stats.kruskal(kruskal_get_PL(1), kruskal_get_PL(2), kruskal_get_PL(3))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([kruskal_get_PL(1), kruskal_get_PL(2), kruskal_get_PL(3)], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")

    def kruskal_Age():
        kruskal_wallis = stats.kruskal(kruskal_get_Age(1), kruskal_get_Age(2), kruskal_get_Age(3), kruskal_get_Age(4), kruskal_get_Age(5), kruskal_get_Age(6))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([kruskal_get_Age(1), kruskal_get_Age(2), kruskal_get_Age(3), kruskal_get_Age(4), kruskal_get_Age(5), kruskal_get_Age(6)], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")

    def kruskal_NS():
        kruskal_wallis = stats.kruskal(get_state_values('California'), get_state_values('Ohio'), get_state_values('Louisiana'))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([get_state_values('California'), get_state_values('Ohio'), get_state_values('Louisiana')], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")

    def kruskal_All_States():
        kruskal_wallis = stats.kruskal(get_state_values('Georgia'), get_state_values('California'), get_state_values('Nevada'), get_state_values('Ohio'), get_state_values('Louisiana'))
        value_label_Kr.config(text=f"Kruskal-Wallis: {kruskal_wallis.pvalue}")
        dunn = sp.posthoc_dunn([get_state_values('Georgia'), get_state_values('California'), get_state_values('Nevada'), get_state_values('Ohio'), get_state_values('Louisiana')], p_adjust='bonferroni')
        value_label_dunn.config(text=f"Dunn-Test: \n{dunn}")
        value_label_le.config(text=f"Mann-Whitney-U Less:")
        value_label_gr.config(text=f"Mann-Whitney-U Greater: ")
        value_label_2t.config(text=f"Mann-Whitney-U 2 Tail: ")

    # Create the main window
    root = tk.Tk()
    root.title("Stats for Trust in Voting")

    # Create labels to display the values
    value_label_2t = tk.Label(root, text="2-tail: ")
    value_label_2t.pack()

    value_label_gr = tk.Label(root, text="greater: ")
    value_label_gr.pack()

    value_label_le = tk.Label(root, text="less: ")
    value_label_le.pack()

    value_label_Kr = tk.Label(root, text="Kruskal: ")
    value_label_Kr.pack()

    value_label_dunn = tk.Label(root, text="Dunn: ")
    value_label_dunn.pack()

    # Feste Fenstergröße einstellen
    root.geometry("800x600")  # Breite x Höhe

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
    kruskalPL_button.place(x=30, y=500)
    kruskalAge_button = tk.Button(root, text="Kruskal-Mann Age", command=kruskal_Age)
    kruskalAge_button.pack()
    kruskalAge_button.place(x=230, y=500)
    kruskalNS_button = tk.Button(root, text="Kruskal-Mann No Swing States", command=kruskal_NS)
    kruskalNS_button.pack()
    kruskalNS_button.place(x=380, y=500)
    kruskal_All_States_button = tk.Button(root, text="Kruskal-Mann All States", command=kruskal_All_States)
    kruskal_All_States_button.pack()
    kruskal_All_States_button.place(x=580, y=500)

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