import pandas as pd

data = {'values':[85,95,70,85,90]}
df = pd.DataFrame(data)
df['rank'] = df['values'].rank(method='max',ascending='False')
print(df)