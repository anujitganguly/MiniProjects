import pandas as pd

#excel file
df = pd.read_csv("input.csv")

# Keep original column names
col_a = df.columns[0]
col_b = df.columns[1]

#values from column A and B as sets exclding 1st row
a_values = set(df[col_a].iloc[1:].dropna())
b_values = set(df[col_b].iloc[1:].dropna())

#comparing sets
duplicates = a_values.intersection(b_values)
a_uniques = a_values - b_values
b_uniques = b_values - a_values

#create new columns
df['Duplicates'] = df.apply(lambda row: row[col_a] if row.name != 0 and (row[col_a] in duplicates or row[col_b] in duplicates) else '', axis=1)
df['Unique_in_' + col_a] = df[col_a].apply(lambda x: x if x in a_uniques else '')
df['Unique_in_' + col_b] = df[col_b].apply(lambda x: x if x in b_uniques else '')

# Export to CSV
df.to_csv("output.csv", index=False)

#run using <python Excel_compare.py>