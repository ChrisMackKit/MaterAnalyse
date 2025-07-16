import openpyxl
import string
import filterIQR15 as fi
import mysql.connector
from scipy import stats
import numpy as np
import normalDist as nd
import drawDiagrams as dd
import codingFunction as cf
import trust_notrust as tn
import getpass

# Path to the Excel file
file_path = r"C:\Users\Nutzer\Desktop\Programme\Statistical Data.xlsx"
stat_value = 'TVS_Score'
password = getpass.getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="trustinvoting"
)
try:

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
    
    def get_Age(age, second=''):
        cursor = connection.cursor(buffered=True)
        if second == '':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}'"
        elif second == 'male':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND Gender = '1'"
        elif second == 'female':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND Gender = '2'"
        elif second == 'democrat':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND Political_Leaning = '1'"
        elif second == 'republican':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND Political_Leaning = '2'"
        elif second == 'independent':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND Political_Leaning = '3'"
        elif second == 'bmd':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND (State = 'Georgia' OR State = 'California')"
        elif second == 'drew':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND (State = 'Ohio' OR State = 'Nevada')"
        elif second == 'swing':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND (State = 'Georgia' OR State = 'Nevada')"
        elif second == 'noswing':
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND (State = 'California' OR State = 'Ohio' OR State = 'Louisiana')"
        else:
            query = f"SELECT {stat_value} FROM results WHERE Age = '{age}' AND State = '{second}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()    
        return group1
    
    def get_Age_60(second=''):
        cursor = connection.cursor(buffered=True)
        if second == '':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7')"
        elif second == 'male':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND Gender = '1'"
        elif second == 'female':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND Gender = '2'"
        elif second == 'democrat':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND Political_Leaning = '1'"
        elif second == 'republican':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND Political_Leaning = '2'"
        elif second == 'independent':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND Political_Leaning = '3'"
        elif second == 'bmd':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND (State = 'Georgia' OR State = 'California')"
        elif second == 'drew':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND (State = 'Ohio' OR State = 'Nevada')"
        elif second == 'swing':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND (State = 'Georgia' OR State = 'Nevada')"
        elif second == 'noswing':
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND (State = 'California' OR State = 'Ohio' OR State = 'Louisiana')"
        else:
            query = f"SELECT {stat_value} FROM results WHERE (Age = '5' OR Age = '6' OR Age = '7') AND State = '{second}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        group1 = np.array([value[0] for value in buff if value[0] is not None]) 
        cursor.close()       
        return group1

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

    def get_3_var_list(gender, pl, state):
        cursor = connection.cursor(buffered=True)
        query = f"SELECT {stat_value} FROM results WHERE Gender = '{gender}' AND Political_Leaning = '{pl}' AND State = '{state}'"
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

    def cal_MWU_standard_logic(g1, g2):
            group1 = g1
            group2 = g2
            two_tail = stats.mannwhitneyu(group1, group2, alternative='two-sided')
            less = stats.mannwhitneyu(group1, group2, alternative='less')
            greater = stats.mannwhitneyu(group1, group2, alternative='greater')
            return two_tail.pvalue, less.pvalue, greater.pvalue
    
    def kruskal_5(value1, value2, value3, value4, value5):
        kruskal_wallis = stats.kruskal(value1, value2, value3, value4, value5)
        return kruskal_wallis.pvalue

    def kruskal_3(value1, value2, value3):
        kruskal_wallis = stats.kruskal(value1, value2, value3)
        return kruskal_wallis.pvalue

    def get_trusting(trust_value):
        cursor = connection.cursor(buffered=True)
        #Factbased_reason
        query = f"SELECT {stat_value} FROM results WHERE Do_you_trust = '{trust_value}'"
        cursor.execute(query)
        buff = cursor.fetchall()
        array = np.array([value[0] for value in buff if value[0] is not None])
        cursor.close()
        return array

    def get_all_values():
            cursor = connection.cursor(buffered=True)
            query = f"SELECT {stat_value} FROM results"
            cursor.execute(query)
            buff = cursor.fetchall()
            array = np.array([value[0] for value in buff if value[0] is not None])
            cursor.close()
            return array

    def cal_standard_logic(input_feld_1, input_feld_2):
            field1 = input_feld_1
            field2 = input_feld_2
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
                elif field1 == 'trust':
                    group = get_trusting(1)
                elif field1 == 'notrust':
                    group = get_trusting(2)
                elif field1 == 'notsure':
                    group = get_trusting(3)
                else:
                    group = get_state_values(field1)
            
            match field1:
                case 'overall':
                    if field2 == 'male':
                        group = get_gender('1')
                    if field2 == 'female':
                        group = get_gender('2')
                    if field2 == 'democrat':
                        group = kruskal_get_PL('1')
                    if field2 == 'republican':
                        group = kruskal_get_PL('2')
                    if field2 == 'independent':
                        group = kruskal_get_PL('3')
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
                    elif field2 == 'noswing':
                        group = get_NoSwing_values_PL('1')
                    elif field2 == 'swing':
                        group = get_Swing_values_PL('1')
                case 'republican':
                    if field2 == 'male':
                        group = get_gender_PL('1', '2')
                    elif field2 == 'female':
                        group = get_gender_PL('2', '2')
                    elif field2 == 'noswing':
                        group = get_NoSwing_values_PL('2')
                    elif field2 == 'swing':
                        group = get_Swing_values_PL('2')
                case 'independent':
                    if field2 == 'male':
                        group = get_gender_PL('1', '3')
                    elif field2 == 'female':
                        group = get_gender_PL('2', '3')
                    elif field2 == 'noswing':
                        group = get_NoSwing_values_PL('3')
                    elif field2 == 'swing':
                        group = get_Swing_values_PL('3')
                case 'male':
                    if field2 == 'democrat':
                        group = get_gender_PL('1', '1')
                    elif field2 == 'republican':
                        group = get_gender_PL('1', '2')
                    elif field2 == 'independent':
                        group = get_gender_PL('1', '3')
                    elif field2 == 'noswing':
                        group = get_NoSwing_values_gender('1')
                    elif field2 == 'swing':
                        group = get_Swing_values_gender('1')
                case 'female':
                    if field2 == 'democrat':
                        group = get_gender_PL('2', '1')
                    elif field2 == 'republican':
                        group = get_gender_PL('2', '2')
                    elif field2 == 'independent':
                        group = get_gender_PL('2', '3')
                    elif field2 == 'noswing':
                        group = get_NoSwing_values_gender('2')
                    elif field2 == 'swing':
                        group = get_Swing_values_gender('2')
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

    def cal_standard_logic_3_values(gender, political_leaning, state):
            if gender == 'male':
                genderNum = 1
            elif gender == 'female':
                genderNum = 2
            if political_leaning == 'democrat':
                pl_num = 1
            elif political_leaning == 'republican':
                pl_num = 2
            elif political_leaning == 'independent':
                pl_num = 3
            return get_3_var_list(genderNum, pl_num, state)

    def normal_dist(values):
        shapiro_wilk_test = stats.shapiro(values)
        mittelwert = np.mean(values)
        standardabweichung = np.std(values, ddof=1)
        ks_test = stats.kstest(values, 'norm', args=(mittelwert, standardabweichung))
        return shapiro_wilk_test.pvalue, ks_test.pvalue

    def cal_mean(values):
        mean1 = np.mean(values)
        modus1 = stats.mode(values, axis=None, keepdims=False)
        median1 = np.median(values)
        return mean1, median1, modus1.mode

    def levene_test(values):
        if len(values) == 3:
            stat, p_value = stats.levene(values[0], values[1], values[2])
        elif len(values) == 4:
            stat, p_value = stats.levene(values[0], values[1], values[2], values[3])
        elif len(values) == 5:
            stat, p_value = stats.levene(values[0], values[1], values[2], values[3], values[4])

        #print(f"Levene-Test Statistik: {stat:.4f}")
        #print(f"p-Wert: {p_value:.4f}")

        #if p_value < 0.05:
            #print("→ Die Varianzen sind signifikant unterschiedlich (keine Homogenität).")
        #else:
            #print("→ Die Varianzen sind homogen (Annahme erfüllt).")
        
        return p_value

    def brown_forsythe_test(values):
        if len(values) == 3:
            stat, p_value = stats.levene(values[0], values[1], values[2], center='median')
        elif len(values) == 4:
            stat, p_value = stats.levene(values[0], values[1], values[2], values[3], center='median')
        elif len(values) == 5:
            stat, p_value = stats.levene(values[0], values[1], values[2], values[3], values[4], center='median')
        
        #print(f"Levene-Test Statistik: {stat:.4f}")
        #print(f"p-Wert: {p_value:.4f}")

        #if p_value < 0.05:
            #print("→ Die Varianzen sind signifikant unterschiedlich (keine Homogenität).")
        #else:
            #print("→ Die Varianzen sind homogen (Annahme erfüllt).")
        
        return p_value

    def anova(values):
        if len(values) == 3:
            stat, p_value = stats.f_oneway(values[0], values[1], values[2])
        elif len(values) == 4:
            stat, p_value = stats.f_oneway(values[0], values[1], values[2], values[3])
        elif len(values) == 5:
            stat, p_value = stats.f_oneway(values[0], values[1], values[2], values[3], values[4])
        
        return p_value

    def r_value(group1, group2):
        u, p_value = stats.mannwhitneyu(group1, group2)
        n1 = len(group1)
        n2 = len(group2)
        
        # Verwenden Sie den kleineren der beiden U-Werte für eine konsistentere Interpretation
        u_korrigiert = min(u, n1 * n2 - u)

        r = 1 - (2 * u_korrigiert) / (n1 * n2)
        return r

    def r_value_dunn(group1, group2):
        group1 = np.asarray(group1)
        group2 = np.asarray(group2)

        # Kombinierte Daten und Ränge berechnen
        data = np.concatenate([group1, group2])
        ranks = stats.rankdata(data)

        n1 = len(group1)
        n2 = len(group2)
        N = n1 + n2

        # Mittelwerte der Ränge
        R1 = np.mean(ranks[:n1])
        R2 = np.mean(ranks[n1:])

        # Dunn-Z-Wert
        z = (R1 - R2) / np.sqrt((N * (N + 1)) / 12 * (1/n1 + 1/n2))

        # Effektgröße r
        r = z / np.sqrt(N)
        return r
    
    def eta_squared(values):
        if len(values) == 3:
            h_statistik, p_value = stats.kruskal(values[0], values[1], values[2]) # Fügen Sie alle Ihre Gruppen hinzu
        elif len(values) == 5:
            h_statistik, p_value = stats.kruskal(values[0], values[1], values[2], values[3], values[4]) 
        n = sum([len(gruppe) for gruppe in values]) # Gesamtzahl der Beobachtungen
        k = len(values) # Anzahl der Gruppen

        epsilon_squared = (h_statistik - (k - 1)) / (n - k)
        return epsilon_squared

    # Open the Excel workbook
    def edit_exel(value, cell_letter_list, cell_number, sheet_number):
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.worksheets[sheet_number]  # Get the active sheet
            
            for i in range(len(cell_letter_list)):
                cell = cell_letter_list[i] + str(cell_number)
                sheet[cell] = value[i]
            #for i in range(len(cell_letter_list)):
            #    cell = cell_letter_list[i] + str(cell_number+1)
            #    sheet[cell] = value[i+1]
            

            # Save the workbook
            workbook.save(file_path)
            #print("Value written to A1 successfully.")
        except FileNotFoundError:
            print("The file was not found. Please check the file path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    #edit_exel("Hello World", "b1", 0)  # Example usage

    def row_array(start, end):
        alphabet = list(string.ascii_lowercase)
        start_index = alphabet.index(start)
        end_index = alphabet.index(end) + 1
        row_array = alphabet[start_index:end_index]

        return row_array

    def column_func(value_list, row_array, sheet_number, row_number):
        if len(value_list) == len(row_array):
            #for i in range(len(value_list)):
            edit_exel(value_list, row_array, row_number, sheet_number)
        else:
            print("The length of the value list does not match the length of the row array.")
            return False
        return True

    def get_list(value_1, value_2):
        #todo: SQL Abfrage mit 2 WHERE Klauseln (Inputfeld1 = value_1 AND Inputfeld2 = value_2)
        #transform from np.array to list
        list_value = cal_standard_logic(value_1, value_2)
        return list_value


    #value_1 = Feld 2 bei Interface
    #value_2 Feld 1 bei Interface für Gruppe 1
    #value_3 Feld 1 bei Interface für Gruppe 2
    def row_func(columns, sheet_number, start_row, value_1, value_2, func, score='TVS_Score'):
        global stat_value
        stat_value = score
        row_list = columns
        value_list = [0] * 2 *len(row_list)
        #calculate and store 
        start = start_row
        if value_1 == []:
            value_1 = ['']
        for i in value_1:
            for j in range(len(value_2)):
                score_values_group1 = get_list(value_2[j], i)
                #score_values_group2 = get_list(value_3[j], i)
                #score_values_group3 = get_list(value_4[j], i)
                #score_values_group4 = get_list(value_5[j], i)
                #score_values_group5 = get_list(value_6[j], i)
                #score_values_group1_IQR = fi.filter_outliers_iqr(score_values_group1)
                #score_values_group2_IQR = fi.filter_outliers_iqr(score_values_group2)
                #score_values_group3_IQR = fi.filter_outliers_iqr(score_values_group3)
                #score_values_group4_IQR = fi.filter_outliers_iqr(score_values_group4)
                #score_values_group5_IQR = fi.filter_outliers_iqr(score_values_group5)
                print('p-values:', func(score_values_group1))
                value_list[0], value_list[1] = func(score_values_group1)
                #value_list[0] = func(score_values_group1_IQR)#, score_values_group2_IQR])#, score_values_group3_IQR, score_values_group4_IQR, score_values_group5_IQR])
                column_func([value_list[0]], row_list, sheet_number, start)
                column_func([value_list[1]], row_list, sheet_number, start+1)
                print('values:', value_list[0], value_list[1])
                start += 2

    def cal_trust(valueList):
        trust = np.sum(valueList == 1)
        no_trust = np.sum(valueList == 2)
        not_sure = np.sum(valueList == 3)
        trust_perc = (np.sum(valueList == 1)/ len(valueList))*100
        no_trust_perc = (np.sum(valueList == 2)/ len(valueList))*100
        not_sure_perc = (np.sum(valueList == 3)/ len(valueList))*100
        return trust, no_trust, not_sure, trust_perc, no_trust_perc, not_sure_perc
    

    def row_func_age(columns, sheet_number, start_row, value_1, func, score):
        global stat_value
        stat_value = score
        row_list = columns
        value_list = [0] * len(row_list)
        #calculate and store 
        start = start_row
        for i in value_1:
                score_values_group1 = get_Age('1')
                score_values_group2 = get_Age('2')
                score_values_group3 = get_Age('3')
                score_values_group4 = get_Age('4')
                score_values_group5 = get_Age_60()
                score_values_group1_IQR = fi.filter_outliers_iqr(score_values_group1)
                score_values_group2_IQR = fi.filter_outliers_iqr(score_values_group2)
                score_values_group3_IQR = fi.filter_outliers_iqr(score_values_group3)
                score_values_group4_IQR = fi.filter_outliers_iqr(score_values_group4)
                score_values_group5_IQR = fi.filter_outliers_iqr(score_values_group5)
                value_list[0] = func([score_values_group1, score_values_group2, score_values_group3, score_values_group4, score_values_group5])
                value_list[1] = func([score_values_group1_IQR, score_values_group2_IQR, score_values_group3_IQR, score_values_group4_IQR, score_values_group5_IQR])
                column_func(value_list, row_list, sheet_number, start)
                start += 1


    def list_of_values(groups, second_field, score):
        global stat_value
        stat_value = score
        value_list = []
        for i in groups:
            value_list.append(cal_standard_logic(i, second_field))
        return value_list
    
    def list_of_values_3_vals(groups, second_field, third_field, score):
        global stat_value
        stat_value = score
        value_list = []
        for i in groups:
            value_list.append(cal_standard_logic_3_values(second_field, third_field, i))
        return value_list
    
    def list_of_values_by_age_group(groups, second_field, score):
        global stat_value
        stat_value = score
        value_list = []
        if second_field == '5':
            for i in groups:
                value_list.append(get_Age_60(i))
        else:
            for i in groups:
                value_list.append(get_Age(second_field, i))
        return value_list

    def list_of_values_codes(groups, second_field, score):
        global stat_value
        stat_value = score
        value_list = []
        amounts_list = []
        for i in groups:
            value_list.append(cal_standard_logic(i, second_field))
        if score == 'Factbased_reason':
            for j in value_list:
                total = len(j)
                amounts_list.append(cf.fact_coding_count_list(j))
        elif score == 'codes_open_question':
            for j in value_list:
                total = len(j)

                amounts_list.append(cf.coding_count_list(j))

        return amounts_list

    def list_of_values_age_2nd_field(groups, score, gender):
        global stat_value
        stat_value = score
        value_list = []
        for i in groups:
            value_list.append(get_Age(i, gender))
        return value_list         

    def list_of_values_age(groups, score, second=''):
        global stat_value
        stat_value = score
        value_list = []
        for i in groups:
            value_list.append(get_Age(i, second))
        return value_list          

    def list_of_values_codes_age(groups, score):
        global stat_value
        stat_value = score
        amounts_list = []
        if score == 'Factbased_reason':
            for j in groups:
                amounts_list.append(cf.fact_coding_count_list(j))
        elif score == 'codes_open_question':
            for j in groups:
                amounts_list.append(cf.coding_count_list(j))

        return amounts_list

    #listOfTitles zb ['California', 'Georgia', 'Ohio', 'Nevada', 'Louisiana', 'Overall', 'BMD', 'DREw']
    #   Titel  sind im Filename und im Diagramm selber
    # categories sind die Staaten/Gruppen, die vorkommen sollen zB [['california', 'georgia', 'ohio', 'nevada', 'louisiana', 'overall', 'bmd', 'drew']
    # fact_or_reason: 0 wenn fact und 1 wenn reason coding
    # second_field: falls es zweites Argument gibt für Gruppe
    # age: wenn age Gruppen vergleich: 1
    # labels: label für Gruppen die verglichen werden
    def draw_histo_coding(listOfTitles, categories, fact_or_reason, labels, second_field='', age=0):
        #todo
        #Sonderfall Age abdecken
        if age == 0:
            if fact_or_reason == 0:
                beschrift = ['fake', 'election_feeling', 'machine_feeling', 'election_fact', 'machine_fact', 'misc']
                values = list_of_values_codes(categories, second_field, 'Factbased_reason')
                for i in range(len(values)):
                    dd.zeichne_balkendiagramm(values[i], beschrift, listOfTitles[i], labels)
            else:
                beschrift = ['neutral', 'name', 'hacking positive', 'hacking negative', 'news', 'error positive', 'error negative', 'tested', 'usability', 'secret positive', 'secret negative', 'government', 'dominion', 'verifiable positive', 'verifiable negative', 'believe', 'detection', 'transparent']
                values = list_of_values_codes(categories, second_field, 'codes_open_question')
                print('values len:', len(values))
            
                dd.zeichne_balkendiagramm(values, beschrift, listOfTitles[0], labels)

        elif age == 1:
            names = ['18-29', '30-39', '40-49', '50-59', '60+']
            values_of_age = list_of_values_age(['1', '2', '3', '4'], 'codes_open_question')
            values_of_age.append(get_Age_60())
            count = list_of_values_codes_age(values_of_age, 'codes_open_question')
            #dd.zeichne_balkendiagramm(count[i], eintraege, names[i])
            if fact_or_reason == 0:
                beschrift = ['fake', 'election_feeling', 'machine_feeling', 'election_fact', 'machine_fact', 'misc']
                values_of_age = list_of_values_age(['1', '2', '3', '4'], 'Factbased_reason')
                values_of_age.append(get_Age_60())
                count = list_of_values_codes_age(values_of_age, 'Factbased_reason')
            else:
                beschrift = ['neutral', 'name', 'LLM', 'hacking positive', 'hacking negative', 'news', 'error positive', 'error negative', 'tested', 'usability', 'secret positive', 'secret negative', 'government', 'dominion', 'verifiable positive', 'verifiable negative', 'believe', 'detection', 'transparent']
                values_of_age = list_of_values_age(['1', '2', '3', '4'], 'codes_open_question')
                values_of_age.append(get_Age_60())
                count = list_of_values_codes_age(values_of_age, 'codes_open_question')
            for i in range(len(count)):
                #print(count[i])
                #dd.zeichne_balkendiagramm(values[i], beschrift, title[i], 'for Age Groups')
                dd.zeichne_balkendiagramm(count[i], beschrift, names[i], labels, 'for Age Groups')

    #title: für Dateinamen zB 'States'
    #listOfGroups: zB ['overall', 'california', 'georgia', 'ohio', 'nevada', 'louisiana']
    # list_names: Namen die Angezeigt werden
    #       Für Altersgruppen: ['18-29', '30-39', '40-49', '50-59', '60+']
    #age: 1 wenn Altergruppen verglichen werden, sonst 0
    #factVSfeeling: 1 wenn feeling und fact Kategorien zusammengefasst sein sollen
    def draw_stack_bar_fact(title, listOfGroups, list_names, age=0, factVSfeeling=0, second=''):
        list_group = listOfGroups
        if age == 1:
            list_group_cap = ['18-29', '30-39', '40-49', '50-59', '60+']
            values = list_of_values_age(['1', '2', '3', '4'], 'Factbased_reason', second)
            values.append(get_Age_60(second))
            amounts_list = []
            for j in values:
                total = len(j)
                amounts_list.append(cf.fact_coding_count_list(j))
            if factVSfeeling == 0:
                dd.drawStockBar_fact_code_6_save(title, amounts_list, list_group_cap, 'for Age Groups')
            else:
                dd.drawStockBar_fact_code__save(title, amounts_list, list_group_cap, 'for Age Groups')
        else:
            list_group_cap = list_names
            values = list_of_values_codes(list_group, second, 'Factbased_reason')
            if factVSfeeling == 0:
                dd.drawStockBar_fact_code_6_save(title, values, list_group_cap, title_extra = '')
            else:
                dd.drawStockBar_fact_code__save(title, values, list_group_cap, title_extra = '')
        
    # scores: Liste von Werten die berechnet werden sollen
    #   zB ['TVS_Score', 'Machine_Score_1','Overall_Trust','Trust_In_Others','Trust_Technology','Cast_Ballot','Anonymous','Transparency','Reliability','Sys_Security','Usability','Accurately_Counted','Accuracy']
    # 
    # verglich: relevant für Filename zB 'States'
    # title: Namen der Scores in einer Form, die ausgeschrieben sind um angezeigt zu werden auf Diagramm
    #   zB ['TVS Score', 'Own Score', 'Overall Trust in the Voting Systems', 'Trust In Others', 'Propensity to Trust in Technology', 'Cast Ballot Reflects Intended Selections', 'Vote is Anonymous', 'System Transparency', 'System Reliability', 'System Security', 'System Usability', 'Votes Are Accurately Counted', 'System Accuracy']
    # age: ist 1 wenn Altersgruppen verglichen werden sollen
    # sec_field: zweites merkmal, falls vorhanden
    def draw_box_plot(scores, list_group, vergleich, title, x_axis_names, age=0, sec_field=[''], third_field=''):
        
        if third_field != '':
            for j in sec_field:
                for i in range(len(scores)):
                    print(f'Score: {scores[i]}')
                    values = list_of_values_3_vals(list_group, j, third_field, scores[i])
                    if scores[i] == 'Machine_Score_1':
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, 'Own Score', j, 41, third_field)
                    elif scores[i] == 'TVS_Score':
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, scores[i], j, 105)
                    else:
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, scores[i], j, 5.2, third_field)
        
        elif age == 0:
            list_group_cap = x_axis_names
            for j in sec_field:
                for i in range(len(scores)):
                    print(f'Score: {scores[i]}')
                    values = list_of_values(list_group, j, scores[i])
                    if scores[i] == 'Machine_Score_1':
                        dd.draw_boxplot_6(values, vergleich, title[i], list_group_cap, 'Own Score', j, 41)
                    elif scores[i] == 'TVS_Score':
                        dd.draw_boxplot_6(values, vergleich, title[i], list_group_cap, scores[i], j, 105)
                    else:
                        dd.draw_boxplot_6(values, vergleich, title[i], list_group_cap, scores[i], j)
        elif age == 1:
            list_groups = ['18-29', '30-39', '40-49', '50-59', '60+']
            for j in sec_field:
                for i in range(len(scores)):
                    print(f'Score: {scores[i]}')
                    values = list_of_values_age(['1', '2', '3', '4'], scores[i], j)
                    values.append(get_Age_60(j))
                    if scores[i] == 'Machine_Score_1':
                        dd.draw_boxplot_6(values, vergleich, title[i], list_groups, 'Own Score', j, 41)
                    elif scores[i] == 'TVS_Score':
                        dd.draw_boxplot_6(values, vergleich, title[i], list_groups, scores[i], j, 105)
                    else:
                        dd.draw_boxplot_6(values, vergleich, title[i], list_groups, scores[i], j)
        
        elif age ==2:
            age_name = ['18-29', '30-39', '40-49', '50-59', '60+']
            for j in range(len(age_name)):
                for i in range(len(scores)):
                    values = list_of_values_by_age_group(list_group, j+1, scores[i])
                    if scores[i] == 'Machine_Score_1':
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, 'Own Score', age_name[j], 41)
                    elif scores[i] == 'TVS_Score':
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, scores[i], age_name[j], 105)
                    else:
                        dd.draw_boxplot_6(values, vergleich, title[i], x_axis_names, scores[i], age_name[j])

    # title: 
    # valueList: Liste von Gruppen
    # age: wenn 1 dann Vergleich von Altersgruppen, 2 wenn vergleich innerhalb einer Altersgruppe
    def draw_stack_trust(title, valueList, namingList, sec_field='', age=0, title_extra='', third_field =''):
        #drawStockBar_trust_2_save(title, valueList, namingList, title_extra = '')
        if third_field != '':
            values = list_of_values_3_vals(valueList, sec_field, third_field, 'Do_you_trust')
            if len(valueList) == 2:
                dd.drawStockBar_trust_2_save(title, values, namingList, title_extra)
            elif len(valueList) == 3:
                dd.drawStockBar_trust_3_save(title, values, namingList, title_extra)
            elif len(valueList) == 5:
                dd.drawStockBar_trust_5_save(title, values, namingList, title_extra)
            elif len(valueList) == 6:
                dd.drawStockBar_trust_6_save(title, values, namingList, title_extra)

        elif age == 0:
            values = list_of_values(valueList, sec_field, 'Do_you_trust')
            if len(valueList) == 2:
                dd.drawStockBar_trust_2_save(title, values, namingList, title_extra)
            elif len(valueList) == 3:
                dd.drawStockBar_trust_3_save(title, values, namingList, title_extra)
            elif len(valueList) == 5:
                dd.drawStockBar_trust_5_save(title, values, namingList, title_extra)
            elif len(valueList) == 6:
                dd.drawStockBar_trust_6_save(title, values, namingList, title_extra)
            
        elif age == 1:
            namingList = ['18-29', '30-39', '40-49', '50-59', '60+']
            values_of_age = list_of_values_age(['1', '2', '3', '4'], 'Do_you_trust', sec_field)
            values_of_age.append(get_Age_60(sec_field))
            dd.drawStockBar_trust_5_save(title, values_of_age, namingList, title_extra)

        elif age == 2:
            values = list_of_values_by_age_group(valueList, sec_field, 'Do_you_trust')
            if len(valueList) == 2:
                dd.drawStockBar_trust_2_save(title, values, namingList, title_extra)
            elif len(valueList) == 3:
                dd.drawStockBar_trust_3_save(title, values, namingList, title_extra)
            elif len(valueList) == 5:
                dd.drawStockBar_trust_5_save(title, values, namingList, title_extra)
            elif len(valueList) == 6:
                dd.drawStockBar_trust_6_save(title, values, namingList, title_extra)

    # groups: liste der Gruppen
    #   zb ['overall', 'california', 'georgia', 'ohio', 'nevada', 'louisiana', 'male', 'female', 'democrat', 'republican', 'independent', 'swing', 'noswing', 'bmd', 'drew']
    # scores: liste der Score
    #   zb ['TVS_Score','Machine_Score_1','Overall_Trust','Trust_In_Others','Trust_Technology','Cast_Ballot','Anonymous','Transparency','Reliability','Sys_Security','Usability','Accurately_Counted','Accuracy']
    # age: wenn 1 dann allw normalverteilungen der Altersgruppen und insgesamt
    # titles: List of titles for the diagrams
    # score_name: List of names for the scores, used in the diagram title
    def draw_Normalverteilung(groups, scores, titles, score_name, second_field='', age=0):
        #todo Normaldist + QQ
        #Sonderfall Age abdecken
        global stat_value
        #print('age: ', age)
        if age==1:
            print('Normalverteilung Age')
            groups = ['18-29', '30-39', '40-49', '50-59', '60+']
            
            for i in scores:
                values_of_age = list_of_values_age(['1', '2', '3', '4'], i)
                values_of_age.append(get_Age_60())
                #print(f'score: {i} Werte: {values_of_age}')
                stat_value = i
                for j in range(len(values_of_age)):
                    if i == 'Machine_Score_1':
                        nd.save_graphs(values_of_age[j], f'{groups[j]}', 'Own Score')
                    else:
                        nd.save_graphs(values_of_age[j], f'Age Group {groups[j]}', i)
        elif age==0:
            #print('Normalverteilung States')
            for i in scores:
                stat_value = i
                for j in range(len(groups)):
                    if i == 'Machine_Score_1':
                        #print('group: ', groups[j])
                        nd.save_graphs(get_list(groups[j], second_field), titles[j], score_name[j], 'Own Score')
                        
                    else:
                        #save_graphs([array_of_values], 'Title_and_name', 'File_name')
                        #print('group: ', groups[j])
                        nd.save_graphs(get_list(groups[j], second_field), titles[j], score_name[j], i)
                    print(f'score: {stat_value}, group: {j}')
        
    
    #scores_page: liste von Tupeln mit Score und der jeweiligen Seite im Excel (beginnend bei 0)
    # zB: [('TVS_Score', 0),('Machine_Score_1', 1), ('Overall_Trust', 5), ('Trust_In_Others', 6)]
    # func: funktion, die berechnen soll
    # list_columns: liste der Spalten, angabe der Buchstaben jeweils
    #   zB ['AE', 'AF']
    # start_row: Zahl der Reihe, bei der es starten soll
    # list_1, list_2 ... : liste von den Gruppen die jeweils verglichen werden. list_1[0] vs lsit_2[0] usw.
    #   zB list_1 ['california', 'bmd'] list_2 ['georgia', 'drew']
    # subgroup: liste von zweiter Eigenschaft, falls vorhanden
    def excel_loops(scores_page, func, list_columns, start_row, list_1, subgroup=[]):
        #todo alle Scores etc hier rein?
        #Sonderfall Age abdecken
        for i in scores_page:
            # Anzahl der list_X Listen jeweils anpassen
            row_func(list_columns, i[1], start_row, subgroup, list_1, func, i[0])
        return True

    score_list = [('TVS_Score', 0),('Machine_Score_1', 1), ('Overall_Trust', 5), ('Trust_In_Others', 6), ('Trust_Technology', 7), ('Cast_Ballot', 8), ('Anonymous', 9), ('Transparency', 10), ('Reliability', 11), ('Sys_Security', 12), ('Usability', 13), ('Accurately_Counted', 14), ('Accuracy', 15)]
    scores = ['TVS_Score','Machine_Score_1','Overall_Trust','Trust_In_Others','Trust_Technology','Cast_Ballot','Anonymous','Transparency','Reliability','Sys_Security','Usability','Accurately_Counted','Accuracy']
    scoreName = ['TVS Score', 'Own Score', 'Overall Trust in the Voting Systems', 'Trust In Others', 'Propensity to Trust in Technology', 'Cast Ballot Reflects Intended Selections', 'Vote is Anonymous', 'System Transparency', 'System Reliability', 'System Security', 'System Usability', 'Votes Are Accurately Counted', 'System Accuracy']
    list_group = ['overall', 'california', 'georgia', 'ohio', 'nevada', 'louisiana']
    list_group_cap = [x.capitalize() for x in list_group]
    values = list_of_values_codes(list_group, '', 'Factbased_reason')
    groups = ['california', 'georgia', 'ohio', 'nevada', 'louisiana', 'bmd', 'drew', 'female', 'male', 'democrat', 'republican', 'independent']
    titles = ['California', 'Georgia', 'Ohio', 'Nevada', 'Louisiana', 'BMD', 'Dre with VVPAT', 'Female', 'Male', 'Democrat', 'Republican', 'Independent']
    
    func = normal_dist
    list_columns = ['X']
    start_row = 4
    l1 = ['california', 'georgia', 'ohio', 'nevada', 'louisiana', 'male', 'female', 'democrat', 'republican', 'independent']

    #excel_loops(score_list, func, list_columns, start_row, l1)

    #draw_Normalverteilung(groups, scores, titles, scoreName, second_field='', age=0)
    #draw_stack_trust(title, valueList, namingList, sec_field='', age=0, title_extra='')
    #draw_box_plot(scores, list_groups, vergleich, title, age=0, sec_field='')
    #draw_stack_bar_fact(title, listOfGroups, list_groups, age=0, factVSfeeling=0, second='')
    #draw_histo_coding(listOfTitles, categories, fact_or_reason, second_field='', age=0)

    #list_group = ['democrat', 'republican', 'independent']
    #list_group_cap = ['Democrats', 'Republicans', 'Independent']
    #list_of_values(valueList, sec_field, 'Do_you_trust')
    scores = ['TVS_Score', 'Machine_Score_1','Overall_Trust','Trust_In_Others','Trust_Technology','Cast_Ballot','Anonymous','Transparency','Reliability','Sys_Security','Usability','Accurately_Counted','Accuracy']
    title = ['TVS Score', 'Machine based Score', 'Overall Trust in the Voting Systems', 'Trust In Others', 'Propensity to Trust in Technology', 'Cast Ballot Reflects Intended Selections', 'Vote is Anonymous', 'System Transparency', 'System Reliability', 'System Security', 'System Usability', 'Votes Are Accurately Counted', 'System Accuracy']
    #names = ['18-29', '30-39', '40-49', '50-59', '60+']
    #values = ['bmd', 'drew', 'louisiana']
    #name_axis = ['BMD', 'DRE/w VVPAT', 'DRE/wo VVPAT']
    #values = ['swing', 'noswing']
    #name_axis = ['Swing', 'No Swing']
    valuesList = [['california', 'ohio', 'louisiana']]
    name_axis_list = [['BMD\n(NSS)', 'DRE\nwith VVPAT\n(NSS)', 'DRE without\nVVPAT\n(NSS)']]
    vergleich_list = ['Non Swing Maschines'] #name des files
    #sec_field = ['male', 'female']
    #third_field = ['democrat', 'republican', 'independent']
    for j in range(len(valuesList)):
        draw_box_plot(scores, valuesList[j], vergleich_list[j], title, name_axis_list[j], age=0)
    
    names = ['BMD', 'DRE with VVPAT']
    #draw_histo_coding(['BMD in California and Georgia'], ['california', 'georgia'], 1, ['California (NSS)', 'Georgia (SS)'])
    #draw_histo_coding(['DRE with VVPAT in Ohio and Nevada'], ['ohio', 'nevada'], 1, ['Ohio (NSS)', 'Nevada (SS)'])
    #for i in range(len(names)):
        
        #draw_stack_bar_fact(names[i], valuesList[i], name_axis_list[i], age=0, factVSfeeling=0)
        #draw_stack_bar_fact(names[i], valuesList[i], name_axis_list[i], age=0, factVSfeeling=1)
        #draw_stack_trust(names[i], valuesList[i], name_axis_list[i])

finally:
    connection.close()
