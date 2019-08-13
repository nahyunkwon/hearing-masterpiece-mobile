import pandas as pd

d = pd.DataFrame({'col1': ['a', 'b'], 'col2': ['c', 'd']})

print(d)

for i in range(len(d)):
    d.iloc[i][0] = d.iloc[i][0] + "b"
    print(d.iloc[i][0])

print(d.dtypes)