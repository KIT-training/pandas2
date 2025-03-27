import pandas as pd
data = pd.read_excel("C:\\Users\\E15\\Desktop\\PandasExample\\pandastutorial\\DataFrame\\abc.xlsx")
# print(data)
# Select a single column
first = data["First Name"]
print("\nSingle Column selected from Dataset")
print(first.head(5))

multicol = data[["Last Name", "First Name", "Dept"]]
print("\nMultiple Columns selected from Dataset")
print(multicol.head(5))  
