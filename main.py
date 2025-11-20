import pandas as pd

data: list = [10, 20,  30]

series = pd.Series(data=data, index=['a', 'b', 'c'])
print(series)

num_list = [1, 2, 3, 4, 5]
series = pd.Series(num_list)
print(series)

num_dict = {'a': 10, 'b': 20, 'c': 30}
series = pd.Series(num_dict)
print(series[[1, 2]])

data: dict = {
    "names": ['rasul', 'ahmad', 'ismail' ],
    'ages': [22, 12, 32],
    'cities': ['grozny', 'moscow', 'saratov']
}

df = pd.DataFrame(data=data)

print(df)
print(df.head())

df['occu'] = ['Engineer', 'Doctor', 'Artist']
print(df)

df['ages'] = df['ages']+1
print(df)

print(df.head(2))
print('\n')

print(df.tail(1))
print('\n')

print(df.sample(2))
print('\n')

print(df.loc[1])
print(df.iloc[2])

print('\n')
print(df.loc[0, 'names'])

matrix  = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]

# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

# print(matrix[2][2])
# print(matrix[1][1])
# print(matrix[0][0])


