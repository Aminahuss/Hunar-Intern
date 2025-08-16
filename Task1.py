import pandas as pd

df = pd.read_csv("C:/Users/Amina Hussain/OneDrive/Documents/004/food_coded.csv")
df = df.loc[:, ~df.columns.duplicated()]

for column in df.columns:
    if df[column].dtype in ['float64', 'int64']:
        df[column] = df[column].fillna(df[column].mean())
    else:
        mode_val = df[column].mode()
        if not mode_val.empty:
            df[column] = df[column].fillna(mode_val[0])

df.drop_duplicates(inplace=True)

df.to_csv("C:/Users/Amina Hussain/OneDrive/Documents/004/food_coded_cleaned.csv", index=False)
print("✅ Data cleaned successfully and saved.")
