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

    print(f"\nChi-Quadrat-Wert: {chi2:.4f}")
    print(f"p-Wert: {p:.4f}")
    print(f"Freiheitsgrade: {dof}")


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
    perc_trust = (np.sum(g1 == 1) / len(g1)) * 100
    perc_no_trust = (np.sum(g1 == 2) / len(g1)) * 100
    perc_not_sure = (np.sum(g1 == 3) / len(g1)) * 100
    return perc_trust, perc_no_trust, perc_not_sure
