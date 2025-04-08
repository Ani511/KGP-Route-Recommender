import pandas as pd

# Load dataset
df = pd.read_csv('KGP_Topsis_Uncleaned.csv')

# Strip leading/trailing whitespaces from all string columns
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# Standardize column names if needed
df.rename(columns=lambda x: x.strip().title(), inplace=True)

# Fill missing or empty route names
df['Route'] = df['Route'].fillna('Unnamed Route')
df['Route'] = df['Route'].replace('', 'Unnamed Route')

# Warn if any row has missing values
missing_rows = df[df.isnull().any(axis=1)]
if not missing_rows.empty:
    print("⚠️ Rows with missing values:")
    print(missing_rows)

# Save cleaned dataset
df.to_csv('KGP_Topsis_Dataset.csv', index=False)
print("✅ Cleaned dataset saved as 'KGP_Topsis_Dataset.csv'")
