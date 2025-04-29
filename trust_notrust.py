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

    # Zeige die Kontingenztabelle
    print("Kontingenztabelle:")
    print(tabelle)

    # Führe den Chi-Quadrat-Test durch
    chi2, p, dof, expected = chi2_contingency(tabelle)

    print(f"\nChi-Quadrat-Wert: {chi2:.4f}")
    print(f"p-Wert: {p:.4f}")
    print(f"Freiheitsgrade: {dof}")

    if p < 0.05:
        print("Es gibt einen signifikanten Unterschied zwischen den Gruppen.")
    else:
        print("Es gibt keinen signifikanten Unterschied zwischen den Gruppen.")

    '''
    # Optional: Berechne die standardisierten Residuen
    observed = tabelle.values
    expected = chi2_contingency(tabelle)[3]
    residuals = (observed - expected) / np.sqrt(expected)

    print("\nStandardisierte Residuen:")
    residuals_df = pd.DataFrame(
        residuals, 
        index=tabelle.index, 
        columns=tabelle.columns
    )
    print(residuals_df)'''

    return chi2, p


def trust_percent(g1):
    perc_trust = (np.sum(g1 == 1) / len(g1)) * 100
    perc_no_trust = (np.sum(g1 == 2) / len(g1)) * 100
    perc_not_sure = (np.sum(g1 == 3) / len(g1)) * 100
    return perc_trust, perc_no_trust, perc_not_sure

