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


    bmd = f"SELECT TVS_Score FROM results"
    cursor.execute(bmd)

    tvs_score = cursor.fetchall()

    # Ergebnisse in ein NumPy-Array konvertieren
    score = np.array([value[0] for value in tvs_score if value[0] is not None])

    # Normalverteilung prüfen
    shapiro_wilk_test = stats.shapiro(score)
    print(f"Shapiro-Wilk-Test: Statistik={shapiro_wilk_test.statistic}, p-Wert={shapiro_wilk_test.pvalue}")

    # Interpretation
    alpha = 0.05
    if shapiro_wilk_test.pvalue > alpha:
        print("Die Daten scheinen normalverteilt zu sein (Nullhypothese nicht abgelehnt).")
    else:
        print("Die Daten scheinen nicht normalverteilt zu sein (Nullhypothese abgelehnt).")
    
    # Normalverteilung anpassen (Mittelwert und Standardabweichung schätzen)
    mittelwert = np.mean(score)
    standardabweichung = np.std(score, ddof=1)  # ddof=1 für Stichprobenstandardabweichung

    # K-S-Test durchführen
    ks_test = stats.kstest(score, 'norm', args=(mittelwert, standardabweichung))
    print(f"K-S-Test: Statistik={ks_test.statistic}, p-Wert={ks_test.pvalue}")

    # Interpretation
    alpha = 0.05
    if ks_test.pvalue > alpha:
        print("Die Daten scheinen normalverteilt zu sein (Nullhypothese nicht abgelehnt) [Kolomogov-Smirnov].")
    else:
        print("Die Daten scheinen nicht normalverteilt zu sein (Nullhypothese abgelehnt) [Kolomogov-Smirnov].")

    anderson_test = stats.anderson(score, dist='norm')
    # Interpretation
    alpha = 0.05
    kritischer_wert = anderson_test.critical_values[2]  # Kritischer Wert für alpha = 0.05
    print(f"Anderson-Darling-Test: Statistik={anderson_test.statistic}, Kritischer Wert={kritischer_wert}")
    if anderson_test.statistic < kritischer_wert:
        print("Die Daten scheinen normalverteilt zu sein (Nullhypothese nicht abgelehnt) [anderson darling test].")
    else:
        print("Die Daten scheinen nicht normalverteilt zu sein (Nullhypothese abgelehnt) [anderson darling test].")



    
    plt.hist(score, bins=30, density=True, alpha=0.6, color='g')

    # Normale Verteilungskurve zum Vergleich hinzufügen
    mu, std = np.mean(score), np.std(score)
    x = np.linspace(min(score), max(score), 100)
    plt.plot(x, stats.norm.pdf(x, mu, std), 'k', linewidth=2)

    plt.title('Histogramm mit Normalverteilungskurve')
    plt.xlabel('Werte')
    plt.ylabel('Häufigkeit')
    plt.show()

    sm.qqplot(score, line='s')
    plt.title('Q-Q-Diagramm')
    plt.show()




finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()