import pandas as pd
data = pd.read_excel('C:\\Users\\LENOVO\\Documents\\GitHub\\pandastutorial\\2DataCleaning\\filldata.xlsx')

#Fill Missing Values with Zero
filldata = data.fillna(0)
# print(filldata)
#####################################

#Fill with Previous Value (Forward Fill)
forward_fill = data.fillna(method='pad')
# print(forward_fill)

backword_fill = data.fillna(method='bfill')  # Backward fill


# Fill NaN Values with ‘Specific String’ using fillna()
 # filling a null values using fillna() 
data["SALY"].fillna('No Salary', inplace = True) 
# print(data)




