import getpass
import mysql.connector
import numpy as np
from scipy import stats

password = getpass.getpass("Enter your MySQL password: ")
# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="trustinvoting"
)

def find_incorrect(listCodes):
    listOfCodes = listCodes.tolist()
    for j in listOfCodes:
        x = j[0].split(', ')
        for i in x:
            if i != 'neutral' and i != 'LLM' and i != 'name' and i != 'hacking_neg' and i != 'hacking_pos' and i != 'news' and i != 'error_pos' and i != 'error_neg' and i != 'tested' and i != 'usability' and i != 'secret_pos' and i != 'secret_neg' and i != 'government'and i != 'dominion' and i != 'verifiable_pos' and i != 'verifiable_neg' and i != 'believe' and i != 'detection' and i != 'transparent':
            #if i != 'fake' and i != 'election_feeling' and i != 'machine_feeling' and i != 'misc' and i != 'election_fact' and i != 'machine_fact':
                print(f'code: {i}, ID: {j[1]}')

    

def fix_codes():
    cursor = connection.cursor(buffered=True)
    query = f"SELECT codes_open_question, DB_ID FROM results"
    cursor.execute(query)
    buff = cursor.fetchall()
    group1 = np.array([(value[0], value[1]) for value in buff if value[0] is not None])
    find_incorrect(group1) 
    cursor.close() 


fix_codes()

connection.close()