import pandas as pd

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

print("Missing Values Before Cleaning:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['City'] = df['City'].fillna(df['City'].mode()[0])

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)

print("\nDataset cleaned and saved successfully!")