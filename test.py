import numpy as np
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def tuekey_hsd_fuer_gruppen(gruppen_werte):
    """
    Führt den Tukey-HSD-Test auf einer Liste von NumPy-Arrays durch,
    wobei jedes Array die Werte einer Gruppe repräsentiert.

    Args:
        gruppen_werte (list of np.ndarray): Eine Liste von NumPy-Arrays.
                                           Jedes Array enthält die Messwerte für eine Gruppe.

    Returns:
        pandas.DataFrame: Ein DataFrame mit den Ergebnissen des Tukey-HSD-Tests.
                          Die Spalten enthalten 'group1', 'group2', 'meandiff' (Mittelwertdifferenz),
                          'lower' (untere Konfidenzgrenze), 'upper' (obere Konfidenzgrenze),
                          'reject' (ob die Nullhypothese der Gleichheit der Mittelwerte abgelehnt wird).
    """
    data = []
    gruppen_namen = []
    for i, gruppe in enumerate(gruppen_werte):
        data.extend(gruppe)
        gruppen_namen.extend([f'Gruppe {i+1}'] * len(gruppe))

    df = pd.DataFrame({'Werte': data, 'Gruppe': gruppen_namen})

    tukey_result = pairwise_tukeyhsd(df['Werte'], df['Gruppe'], alpha=0.05) # alpha ist das Signifikanzniveau
    result = pd.DataFrame(data=tukey_result._results_table.data[1:], columns=tukey_result._results_table.data[0])
    print(result)
    return result

# Beispielhafte Verwendung:
gruppe_a = np.array([10, 12, 15, 11, 13])
gruppe_b = np.array([18, 20, 22, 19, 21])
gruppe_c = np.array([12, 14, 16, 13, 15])
gruppe_d = np.array([25, 27, 30, 26, 28])

gruppen_daten = [gruppe_a, gruppe_b, gruppe_c, gruppe_d]

tukey_ergebnisse = tuekey_hsd_fuer_gruppen(gruppen_daten)
print(tukey_ergebnisse)