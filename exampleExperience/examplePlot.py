import matplotlib.pyplot as plt
from example import *


#plot the data
plt.scatter(dataset['YearsExperience'], dataset['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.show()