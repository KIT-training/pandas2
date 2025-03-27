import pandas as pd
data = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\abc.xlsx")
data2 = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\def.xlsx")
# print(data2)


# using a .concat() method
frames = [data, data2]

res1 = pd.concat(frames)
print(res1)
