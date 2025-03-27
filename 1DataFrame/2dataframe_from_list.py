# pip install pandas 
import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]


# data2 = [{'name':'aung aung', 'phone':'04520672'}]
df = pd.DataFrame(data)

print(df.head())
