import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Beispieldaten
def chi_squared_test(g1, g2):
    # Angenommen, du hast zwei Arrays mit Werten 1, 2, 3
    gruppe1 = g1  # Beispieldaten
    gruppe2 = g2  # Beispieldaten

    # Erstelle eine Häufigkeitstabelle (Kontingenztabelle)
    # Zähle Häufigkeiten für jede Kategorie in beiden Gruppen
    tabelle = pd.crosstab(
        index=np.array(['Gruppe1']*len(gruppe1) + ['Gruppe2']*len(gruppe2)),
        columns=np.array(list(gruppe1) + list(gruppe2))
    )

    # Benenne die Spalten für bessere Lesbarkeit um
    tabelle.columns = ['Trust', 'No Trust', 'Not Sure']


    # Führe den Chi-Quadrat-Test durch
    chi2, p, dof, expected = chi2_contingency(tabelle)

    #print(f"\nChi-Quadrat-Wert: {chi2:.4f}")
    #print(f"p-Wert: {p:.4f}")
    #print(f"Freiheitsgrade: {dof}")


    return chi2, p

def chi_squared_test_3(g1, g2, g3):
    # Angenommen, du hast zwei Arrays mit Werten 1, 2, 3
    gruppe1 = g1  # Beispieldaten
    gruppe2 = g2  # Beispieldaten
    gruppe3 = g3  # Beispieldaten

    # Erstelle eine Häufigkeitstabelle (Kontingenztabelle)
    # Zähle Häufigkeiten für jede Kategorie in beiden Gruppen
    tabelle = pd.crosstab(
        index=np.array(['Gruppe1']*len(gruppe1) + ['Gruppe2']*len(gruppe2) + ['Gruppe3']*len(gruppe3)),
        columns=np.array(list(gruppe1) + list(gruppe2) + list(gruppe3))
    )

    # Benenne die Spalten für bessere Lesbarkeit um
    tabelle.columns = ['Trust', 'No Trust', 'Not Sure']

    # Führe den Chi-Quadrat-Test durch
    chi2, p, dof, expected = chi2_contingency(tabelle)

    print(f"\nChi-Quadrat-Wert: {chi2:.4f}")
    print(f"p-Wert: {p:.4f}")
    print(f"Freiheitsgrade: {dof}")

    return chi2, p

def chi_squared_test_5(g1, g2, g3, g4, g5):
    # Angenommen, du hast zwei Arrays mit Werten 1, 2, 3
    gruppe1 = g1  # Beispieldaten
    gruppe2 = g2  # Beispieldaten
    gruppe3 = g3  # Beispieldaten
    gruppe4 = g4  # Beispieldaten
    gruppe5 = g5  # Beispieldaten

    # Erstelle eine Häufigkeitstabelle (Kontingenztabelle)
    # Zähle Häufigkeiten für jede Kategorie in beiden Gruppen
    tabelle = pd.crosstab(
        index=np.array(['Gruppe1']*len(gruppe1) + ['Gruppe2']*len(gruppe2) + ['Gruppe3']*len(gruppe3) + ['Gruppe4']*len(gruppe4) + ['Gruppe5']*len(gruppe5)),
        columns=np.array(list(gruppe1) + list(gruppe2) + list(gruppe3) + list(gruppe4) + list(gruppe5))
    )

    # Benenne die Spalten für bessere Lesbarkeit um
    tabelle.columns = ['Trust', 'No Trust', 'Not Sure']

    # Führe den Chi-Quadrat-Test durch
    chi2, p, dof, expected = chi2_contingency(tabelle)

    print(f"\nChi-Quadrat-Wert: {chi2:.4f}")
    print(f"p-Wert: {p:.4f}")
    print(f"Freiheitsgrade: {dof}")

    return chi2, p

def trust_percent(g1):
    trust = np.sum(g1 == 1)
    no_trust = np.sum(g1 == 2)
    not_sure = np.sum(g1 == 3)
    perc_trust = (np.sum(g1 == 1) / len(g1)) * 100
    perc_no_trust = (np.sum(g1 == 2) / len(g1)) * 100
    perc_not_sure = (np.sum(g1 == 3) / len(g1)) * 100
    return perc_trust, perc_no_trust, perc_not_sure, trust, no_trust, not_sure

def cramers_v(amount, g1, g2, g3='', bias_correction=False):

    if amount == 2:
        table = pd.crosstab(
        index=np.array(['Gruppe1']*len(g1) + ['Gruppe2']*len(g2)),
        columns=np.array(list(g1) + list(g2))
    )
    elif amount == 3:
        table = pd.crosstab(
        index=np.array(['Gruppe1']*len(g1) + ['Gruppe2']*len(g2)+ ['Gruppe3']*len(g3)),
        columns=np.array(list(g1) + list(g2) + list(g3))
    )

    chi2, _, _, _ = chi2_contingency(table)
    n = np.sum(table)
    phi2 = chi2 / n
    r, k = table.shape

    if bias_correction:
        phi2_corr = max(0, phi2 - ((k - 1)*(r - 1)) / (n - 1))
        r_corr = r - ((r - 1)**2) / (n - 1)
        k_corr = k - ((k - 1)**2) / (n - 1)
        return np.sqrt(phi2_corr / min((k_corr - 1), (r_corr - 1)))
    else:
        return np.sqrt(phi2 / min(k - 1, r - 1))