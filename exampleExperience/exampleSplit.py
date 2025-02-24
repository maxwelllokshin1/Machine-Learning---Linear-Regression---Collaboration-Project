from example import *
from exampleData import *
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=1)
# X_train 80% of data
# X_test 20% of data
# y_train 80% of data
# y_test 20% of data

#X is feature set, y is target set, random state is new sead after every random run, test size is the % used for testing and training

print(X_train.shape) # data set cause two values
print(X_test.shape)
print(y_train.shape) # vector cause one value
print(y_test.shape)