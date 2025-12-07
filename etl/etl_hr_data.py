import pandas as pd 
df = pd.read_csv('data/raw/hR.csv')

# Assertation for unique employee_id 
assert df['EmployeeNumber'].is_unique, "Duplicate employee IDs found!"

# Preview 
print("Shape:", df.shape)
print(df.head())

# Department cleaning 
missing_dept = df[df['Department'].isna() | (df['Department'].str.strip() == "")]
#hello
# Gender cleaning 
df['Gender'] = df['Gender'].str.lower().map({
'm':'Male',
'male': 'Male',
'female': 'Female',
'f' : "Female"
})

#Salary Cleaning 
df["MonthlyIncome"] = df["MonthlyIncome"].replace('[\$,]', '', regex=True) 
df["MonthlyIncome"] = df['MonthlyIncome'].fillna(
    df.groupby('Department')["MonthlyIncome"].transform('mean'))
df.to_csv("data/clean/clean.csv", index=False)


