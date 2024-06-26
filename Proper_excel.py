 import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("your_excel_file.xlsx")

# Split attribute_name into multiple columns
attributes = df['attribute_name'].str.get_dummies(sep=', ')

# Combine attributes DataFrame with the original DataFrame
df_combined = pd.concat([df, attributes], axis=1)

# Drop the original attribute_name column
df_combined.drop('attribute_name', axis=1, inplace=True)

# Iterate over unique attributes and create new columns with 0 or 1 values based on label presence
for attribute in attributes.columns:
    df_combined[attribute] = df_combined.apply(lambda row: 1 if attribute in row['label'] else 0, axis=1)

# Drop the original label column
df_combined.drop('label', axis=1, inplace=True)

# Now df_combined contains the desired DataFrame with attribute_name split into multiple columns
import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("your_excel_file.xlsx")

# Split attribute_name into multiple columns
attributes = df['attribute_name'].str.get_dummies(sep=', ')

# Fill null values in the label column with an empty string
df['label'] = df['label'].fillna('')

# Use str.contains() to check if each attribute is present in the label column
df = pd.concat([df, attributes.apply(lambda x: df['label'].str.contains(x.name).astype(int))], axis=1)

# Replace null values in attribute columns with zeros
df[attributes.columns] = df[attributes.columns].fillna(0)

# Drop the original columns
df.drop(['attribute_name', 'label'], axis=1, inplace=True)
