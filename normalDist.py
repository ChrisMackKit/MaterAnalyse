import getpass
import mysql.connector
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm


def normal_distribution_analysis(ova_score, hist_title):
    # Normalverteilung prüfen
    shapiro = stats.shapiro(ova_score)
    print(f"Shapiro-Wilk-Test: Statistik={shapiro.statistic}, p-Wert={shapiro.pvalue}")

    # Interpretation
    alpha = 0.05
    if shapiro.pvalue > alpha:
        print("Die Daten scheinen normalverteilt zu sein (Nullhypothese nicht abgelehnt).")
    else:
        print("Die Daten scheinen nicht normalverteilt zu sein (Nullhypothese abgelehnt).")
    
    # Normalverteilung anpassen (Mittelwert und Standardabweichung schätzen)
    mittelwert = np.mean(ova_score)
    standardabweichung = np.std(ova_score, ddof=1)  # ddof=1 für Stichprobenstandardabweichung

    # K-S-Test durchführen
    ks_test = stats.kstest(ova_score, 'norm', args=(mittelwert, standardabweichung))
    print(f"K-S-Test: Statistik={ks_test.statistic}, p-Wert={ks_test.pvalue}")

    # Interpretation
    alpha = 0.05
    if ks_test.pvalue > alpha:
        print("Die Daten scheinen normalverteilt zu sein (Nullhypothese nicht abgelehnt) [Kolomogov-Smirnov].")
    else:
        print("Die Daten scheinen nicht normalverteilt zu sein (Nullhypothese abgelehnt) [Kolomogov-Smirnov].")

    
    plt.hist(ova_score, bins=30, density=True, alpha=0.6, color='g')

    # Normale Verteilungskurve zum Vergleich hinzufügen
    mu, std = np.mean(ova_score), np.std(ova_score)
    x = np.linspace(min(ova_score), max(ova_score), 100)
    plt.plot(x, stats.norm.pdf(x, mu, std), 'k', linewidth=2)

    plt.title(hist_title)
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.show()

    sm.qqplot(ova_score, line='s')
    plt.title(hist_title)
    plt.show()
    return shapiro, ks_test

def save_graphs(values, hist_title, score_type, file_path):
    file_path = f'G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Normalverteilung\\{file_path}'

    plt.figure()
    plt.hist(values, bins=30, density=True, alpha=0.6, color='g')

    # Normale Verteilungskurve zum Vergleich hinzufügen
    print(f'values: {values}')
    mu, std = np.mean(values), np.std(values)
    x = np.linspace(min(values), max(values), 100)
    plt.plot(x, stats.norm.pdf(x, mu, std), 'k', linewidth=2)

    plt.title(f'Normal Distribution for {hist_title} based on {score_type}')
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.savefig(f"{file_path}\\histogram_{hist_title}_{score_type}.png", dpi=300, bbox_inches='tight')
    #plt.show()
    plt.close()

    plt.figure()
    sm.qqplot(values, line='s')
    plt.title(f'Q-Q Plot for {hist_title} based on {score_type}')
    plt.savefig(f"{file_path}\\qq_{hist_title}_{score_type}.png", dpi=300, bbox_inches='tight')
    #plt.show()
    plt.close()




