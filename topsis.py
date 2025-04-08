import pandas as pd
import numpy as np

def run_topsis(df, weights):
    df_copy = df.copy()
    route_info = df_copy[['Route']]
    criteria_cols = ['Safety (1-5)', 'Time (min)', 'Distance (km)', 'Traffic (1-10)', 'Road Quality (1-5)']

    # Convert to numeric (in case there are string/dirty values)
    for col in criteria_cols:
        df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce')

    # Drop rows with NaNs in criteria columns
    df_copy.dropna(subset=criteria_cols, inplace=True)

    if df_copy.empty:
        return pd.DataFrame([{'Route': 'No valid data', 'Topsis Score': np.nan, 'Rank': np.nan}])
    if len(df_copy) == 1:
        df_copy['Topsis Score'] = 0.5  # Neutral score, can change to 1.0 if preferred
        df_copy['Rank'] = 1
        result = pd.concat([route_info.reset_index(drop=True), df_copy[['Topsis Score', 'Rank']].reset_index(drop=True)], axis=1)
        result['Note'] = "Only one route available — score is default."
        return result

    data = df_copy[criteria_cols].values.astype(float)
    weights = np.array(weights)

    # Normalize
    norm = data / np.sqrt((data**2).sum(axis=0))

    # Weighted normalization
    weighted = norm * weights

    # Ideal best and worst
    ideal_best = np.max(weighted, axis=0)
    ideal_worst = np.min(weighted, axis=0)

    # Distances
    dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    # Avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        scores = dist_worst / (dist_best + dist_worst)
        scores = np.nan_to_num(scores)  # Replace nan with 0 if any

    df_copy['Topsis Score'] = scores
    df_copy['Rank'] = df_copy['Topsis Score'].rank(ascending=False, method='min').fillna(0).astype(int)

    return pd.concat([route_info.reset_index(drop=True), df_copy[['Topsis Score', 'Rank']].reset_index(drop=True)], axis=1).sort_values(by='Rank')
