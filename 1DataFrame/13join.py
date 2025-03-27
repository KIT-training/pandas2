import pandas as pd
df = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\abc.xlsx")
df1 = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\def.xlsx")
# print(data2)

# joining dataframe
res = df.join(df1)
 
# getting union
res1 = df.join(df1, how='outer')
 

# using 'on' argument in join
res2 = df.join(df1, on='Key')
 

# joining singly indexed with
# multi indexed
result = df.join(df1, how='inner')
 



