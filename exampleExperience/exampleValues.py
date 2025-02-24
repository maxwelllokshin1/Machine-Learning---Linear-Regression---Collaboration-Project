from sklearn.metrics import mean_squared_error, r2_score
from exampleML import *

# error? the difference is the actual values and the predicted values: y_test and y_prod

print("Mean squared error: ", mean_squared_error(y_test, y_prod))
print("R2 score: ", r2_score(y_test, y_prod))

print('Slope: ', model.coef_)
print('Intercept: ', model.intercept_)

years_of_experience = 10
salary = model.predict([[years_of_experience]])
print('Salary of someone with 10 years of experience: ', salary)