import matplotlib.pyplot as plt
from dataCollection import *

plt.scatter(dataset['Mileage'], dataset['Price'])
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Mileage vs Price')
plt.show()