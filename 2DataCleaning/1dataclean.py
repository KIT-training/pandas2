import pandas as pd
data = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data.xlsx')
data1 = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data1.xlsx')

# Checking for missing values using isnull()
missing_values = data.isnull()
# print(missing_values)


# Filtering Data Based on Missing Values
bool_series = pd.isnull(data["ATT DAY"])
missing_data = data[bool_series]
# print(missing_data)



# Identifying non-missing values in the  column
non_missing_data = pd.notnull(data["ATT DAY"])

non_missing_dataframe = data[non_missing_data]
print(non_missing_dataframe)

