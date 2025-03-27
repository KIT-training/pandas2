import pandas as pd
# url = './data.xlsx'

data = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data.xlsx')
data1 = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data1.xlsx')
data2 = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data2.xlsx')

# filter_data = data.loc[(data['SALY']>=200000) | (data['TA']>=40000)]
# frame = [data, data1, data2]
res = data.append(data2)
print(res)

