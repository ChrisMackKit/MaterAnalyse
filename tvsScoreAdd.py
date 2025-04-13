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



    # Spalte mit berechneten Werten füllen
    sql_update = """
        UPDATE results
        SET TVS_Score = (((((Cast_Ballot_Reflects_Every_Choice + Cast_Ballot_Reflects_Intended + Cast_Ballot_Reflects_Intentions_Beliefs + Cast_Ballot_Reflects_People_Propositions)/4)-1) + (((Propensity_to_Trust_in_Tech_Comfortable + Propensity_to_Trust_in_Tech_Confident + Propensity_to_Trust_in_Tech_Fine + Propensity_to_Trust_in_Tech_General)/4)-1) + (((Votes_Are_accurately_Accurately_Counted + Votes_Are_accurately_Included + Votes_Are_accurately_No_Leave_Out + Votes_Are_accurately_Selections_Counted)/4)-1) + (((Vote_is_anonymous_Anonymous + Vote_is_anonymous_No_Trace + Vote_is_anonymous_Only_I_Know + Vote_is_anonymous_Unless_Tell)/4)-1) + (((Trust_in_Others_Basically_Moral + Trust_in_Others_Good_Intentions + Trust_in_Others_Human_Goodness + Trust_in_Others_Trust_People)/4)-1) + (((System_Usability_Confident + System_Usability_Great + System_Usability_Rely_Future + System_Usability_Works_Want)/4)-1) + (((System_Transparency_Confident + System_Transparency_No_Hide + System_Transparency_Verify_Vote + System_Transparency_Verify_Working)/4)-1) + (((System_Security_No_Harm + System_Security_No_Tamper + System_Security_Riskless + System_Security_Secure)/4)-1) + (((System_Reliability_Always_Works + System_Reliability_Dependable + System_Reliability_Never_Fails + System_Reliability_Reliable)/4)-1) + (((System_Accuracy_Accurate + System_Accuracy_Always_Correct + System_Accuracy_Precise + System_Accuracy_Supposed_To_Do)/4)-1))* 2.5)
    """


    cursor.execute(sql_update)

    # Änderungen speichern
    connection.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()