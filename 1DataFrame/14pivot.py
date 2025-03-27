import pandas as pd
df = pd.read_excel("C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\abc.xlsx")
# df1 = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\def.xlsx")

# print(df)
pivot = df.pivot_table(index=['Emp ID'],
					values=['Pay Rate'],
					aggfunc='sum')
# print(pivot)

#More Col Pivot
pivot1 = df.pivot_table(index=['Dept', 'Emp ID', 'First Name'],
					values=['Pay Rate'], aggfunc='sum')
# print(pivot1)


# 'mean', 'min'} will get median, mean and
# minimum of sales respectively
pivot2 = df.pivot_table(index=['Dept'], values=['Pay Rate'],
					aggfunc={'median', 'mean', 'min'})
print(pivot2)
