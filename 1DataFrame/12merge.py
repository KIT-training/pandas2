import pandas as pd
df = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data.xlsx')
df1 = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\DataFrame\\data1.xlsx')


# left	===> LEFT OUTER JOIN	Use keys from left frame only
# right	===> RIGHT OUTER JOIN	Use keys from right frame only
# outer	===> FULL OUTER JOIN	Use union of keys from both frames
# inner	===> INNER JOIN	        Use intersection of keys from both frames

# using .merge() -on function
res = pd.merge(df, df1, on='NAME')

res.to_excel("output.xlsx", sheet_name='Sheet1')
# print(res)


# merging dataframe using multiple keys
# res1 = pd.merge(df, df1, on=['Emp ID', 'First Name'])
# print(res1)

# using keys from left frame
# res2 = pd.merge(df, df1, how='left', on=['key', 'key1'])
 

# using keys from right frame
# res3 = pd.merge(df, df1, how='right', on=['key', 'key1'])


# getting union  of keys
# res4 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
 
# getting intersection of keys
# res5 = pd.merge(df, df1, how='inner', on=['key', 'key1'])





