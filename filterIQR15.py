import numpy as np

def filter_outliers_iqr(data):
    
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    # Identifizieren der Ausreißer
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    # Filtern der Ausreißer aus den Daten
    filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]

    return filtered_data, outliers
