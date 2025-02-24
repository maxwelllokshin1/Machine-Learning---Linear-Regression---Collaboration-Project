import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from example import *
from exampleSplit import *
from examplePlot import *

#create the model
model = LinearRegression()

# train the model using the training set
model.fit(X_train, y_train)

# get the models prediction on the test set
y_prod = model.predict(X_test)

print(y_prod)
print(y_test)

# #plot the data train data
# plt.scatter(X_train, y_train, color='red')
# plt.plot(X_train, model.predict(X_train), color='blue')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.title('Salary vs Years of Experience (Training set)')
# plt.show()

# test data model's prediction
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, model.predict(X_test), color='blue')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience (Test set)')
plt.show()