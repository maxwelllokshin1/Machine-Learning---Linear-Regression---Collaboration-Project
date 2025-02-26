import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from dataCollectionPlot import *
from dataCollectionSplit import *


model = LinearRegression()

model.fit(X_train, y_train)

y_prod = model.predict(X_test)

print(y_prod)
print(y_test)

#plot the data train data
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, model.predict(X_train), color='blue')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Price vs Mileage (Training set)')
plt.show()

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, model.predict(X_test), color='blue')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Price vs Mileage (Test set)')
plt.show()