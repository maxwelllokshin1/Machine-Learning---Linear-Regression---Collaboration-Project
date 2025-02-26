from sklearn.metrics import mean_squared_error, r2_score
from dataCollectionML import *

# error? the difference is the actual values and the predicted values: y_test and y_prod

# print("Mean squared error: ", mean_squared_error(y_test, y_prod))
# print("R2 score: ", r2_score(y_test, y_prod))

# print('Slope: ', model.coef_)
# print('Intercept: ', model.intercept_)

miles = 50000
price = model.predict([[miles]])
print('price of car with 50000 miles: ', price)
