import pandas as pd

data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]

df = pd.DataFrame(data)

print(df['a'])
