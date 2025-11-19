import pandas as pd

data = [10, 20,  30]

series = pd.Series(data=data, index=['a', 'b', 'c'])

data = {
    "names": ['r', 'a', 'i' ],
    'ages': [1, 2, 3],
    'cities': ['g', 'm', 's']
}
df = pd.DataFrame(data=data)

print(df)
