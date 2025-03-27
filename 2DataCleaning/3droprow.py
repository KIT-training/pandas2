import pandas as pd
data = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\2DataCleaning\\filldata.xlsx')

# 1. Dropping Rows with At Least One Null Value
droprow = data.dropna()
# print(droprow)

# 2. Dropping Rows with All Null Values
allna = data.dropna(how='all')

# 3. Dropping Columns with At Least One Null Value
drop_col = data.dropna(axis=1)
print(drop_col)


