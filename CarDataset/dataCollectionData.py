from dataCollection import *

X = dataset.iloc[:, [6]].values
y = dataset.iloc[:, -1].values

print(X)
print(y)