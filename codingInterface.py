import getpass
import mysql.connector
import numpy as np
from scipy import stats
import tkinter as tk
import matplotlib.pyplot as plt
import statsmodels.api as sm
import tkinter.scrolledtext as scrolledtext

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
    cursorG = connection.cursor(buffered=True)
    cursorC = connection.cursor(buffered=True)
    cursorN = connection.cursor(buffered=True)
    cursorO = connection.cursor(buffered=True)
    cursorL = connection.cursor(buffered=True)

    # Spalte mit berechneten Werten füllen
    '''
    georgia = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID from results WHERE State = 'Georgia'
    """
    california = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID from results WHERE State = 'California'
    """
    nevada = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID from results WHERE State = 'Nevada'
    """
    ohio = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID from results WHERE State = 'Ohio'
    """
    louisiana = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID from results WHERE State = 'Louisiana'
    """


    cursorG.execute(georgia)
    cursorC.execute(california)
    cursorN.execute(nevada)
    cursorO.execute(ohio)
    cursorL.execute(louisiana)
    georgiaResults = cursorG.fetchall()
    californiaResults = cursorC.fetchall()
    nevadaResults = cursorN.fetchall()
    ohioResults = cursorO.fetchall()
    louisianaResults = cursorL.fetchall()


    georgiaResults2 = np.array([(value[0], value[1], value[2]) for value in georgiaResults if value[0] is not None])
    californiaResults2 = np.array([(value[0], value[1], value[2]) for value in californiaResults if value[0] is not None])
    nevadaResults2 = np.array([(value[0], value[1], value[2]) for value in nevadaResults if value[0] is not None])
    ohioResults2 = np.array([(value[0], value[1], value[2]) for value in ohioResults if value[0] is not None])
    louisianaResults2 = np.array([(value[0], value[1], value[2]) for value in louisianaResults if value[0] is not None])
    '''
    all = """
        SELECT Do_you_trust, Open_Question_about_Trust, DB_ID, State from results
        """
    cursorG.execute(all)
    allResults = cursorG.fetchall()
    allResults2 = np.array([(value[0], value[1], value[2], value[3]) for value in allResults if value[0] is not None])

    for i in range(len(allResults2)):
        if allResults2[i][0] == "1":
            allResults2[i][0] = "Do Trust"
        elif allResults2[i][0] == "2":
            allResults2[i][0] = "Don't Trust"
        elif allResults2[i][0] == "3":
            allResults2[i][0] = "Not Sure"
        else:
            allResults2[i][0] = "Unknown"
    # Initialize the index for displaying results
    current_index = 0

    # Function to update the displayed values
    def update_display():
        if 0 <= current_index < len(allResults2):
            value1_label.config(text=f"{allResults2[current_index][0]}")
            #value2_label.config(text=f"Reason: {georgiaResults2[current_index][1]}")
            value3_label.config(text=f"DB ID: {allResults2[current_index][2]}")
            value4_label.config(text=f"State: {allResults2[current_index][3]}")
            text_field.delete(1.0, tk.END)  # Clear the text field
            text_field.insert(tk.END, f"{allResults2[current_index][1]}\n")
        else:
            value1_label.config(text="Value 1: N/A")
            #value2_label.config(text="Value 2: N/A")
            value3_label.config(text="Value 3: N/A")
            value4_label.config(text="State: N/A")
            text_field.delete(1.0, tk.END)
            text_field.insert(tk.END, "No more entries.")

    # Function to handle the 'Next' button click
    def next_entry():
        global current_index
        if current_index < len(allResults2) - 3:
            current_index += 3
            update_display()

    # Create the main window
    root = tk.Tk()
    root.title("Georgia Results Viewer")

    # Create labels to display the values
    value1_label = tk.Label(root, text="Trust: ")
    value1_label.pack()

    value3_label = tk.Label(root, text="DB ID: ")
    value3_label.pack()

    value4_label = tk.Label(root, text="State: ")
    value4_label.pack()

    #value2_label = tk.Label(root, text="Reason: ")
    #value2_label.pack()

    # Feste Fenstergröße einstellen
    root.geometry("1000x500")  # Breite x Höhe
    root.resizable(False, False)  # Verhindert das Ändern der Fenstergröße

    #Textfield
    text_field = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_field.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create the 'Next' button
    next_button = tk.Button(root, text="Next", command=next_entry)
    next_button.pack()

    # Function to handle the 'Save' button click
    def save_code():
        global codes
        codes = input_field.get()
        print(f"Saved code: {codes}")  # Optional: Print the saved code for confirmation
        sql_input = f"UPDATE results SET codes_open_question = '{codes}' WHERE DB_ID = {allResults2[current_index][2]}"
        cursorC.execute(sql_input)
        connection.commit()
        

    # Create an input field
    input_field = tk.Entry(root, width=50)
    input_field.pack(pady=10)

    # Create the 'Save' button
    save_button = tk.Button(root, text="Save", command=save_code)
    save_button.pack()

    # Initialize the display with the first entry
    update_display()

    # Run the Tkinter event loop
    root.mainloop()


finally:
    # Close the cursor and connection
    cursorG.close()
    cursorC.close()
    cursorN.close()
    cursorO.close()
    cursorL.close()
    connection.close()