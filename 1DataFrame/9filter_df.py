import pandas as pd
data = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\abc.xlsx")
# print(data)

filter_data = data.loc[(data['Pay Rate']>=30)]
# print(filter_data)

filter_datas = data.loc[(data['Pay Rate']>=30) & (data['First Name'].str.startswith('K'))]
# print(filter_datas)

