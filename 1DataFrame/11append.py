import pandas as pd
data = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\abc.xlsx")
data2 = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\def.xlsx")
# print(data2)
# using append function

res = data.append(data2)
print(res)
