import pandas as pd
original_df = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
})

new_df = original_df[['Name']] 
print(new_df)
