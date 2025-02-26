import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# import the dataset
dataset = pd.read_csv('./car_price_dataset.csv')
model = LinearRegression()

# print(dataset.head())

# print(dataset.describe())

# print(dataset.shape)

def printReferenceTable(dataset1, dataset2, modelOn, label):
    plt.scatter(dataset1, dataset2, color='red')
    if modelOn:
        plt.plot(dataset1, model.predict(dataset1), color='blue')
    labelXandY = label.split(' ')
    plt.xlabel(labelXandY[0])
    plt.ylabel(labelXandY[2])
    plt.title(label)
    plt.show()

def gatherInformation(X, y, model):
    # print(X)
    # print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
    model.fit(X_train, y_train)
    y_prod = model.predict(X_test)

    # print(y_prod)
    # print(y_test)
    return X_train, X_test, y_train, y_test

def linReg(X, y):
    X = X.flatten() if hasattr(X, "flatten") else X
    mean_x = sum(X) / len(X)
    mean_y = sum(y) / len(y)
    numerator = sum([(x - mean_x) * (y - mean_y) for x, y in zip(X, y)]) # sumation formula
    denominator = sum([(x - mean_x) ** 2 for x in X])
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    return slope, intercept

def main():

    print(dataset['Brand'].unique())
    brandName = input("Give brand name: ")
    filteredBrand = dataset[dataset['Brand'].str.contains(brandName, case=False, na=False)]


    print(filteredBrand['Model'].unique())
    modelName = input("Give model name: ")
    filteredModel = filteredBrand[filteredBrand['Model'].str.contains(modelName, case=False, na=False)]

    print(filteredModel['Year'].unique())
    filterByYear = input("Filter by year: ")
    filteredYear = filteredModel[filteredModel['Year'] == int(filterByYear)]

    X = filteredYear.iloc[:, [6]].values  # Gathers the feature set
    y = filteredYear.iloc[:, -1].values    # Gathers the target set
    
    # printReferenceTable(filteredYear['Mileage'], filteredYear['Price'], False, 'Mileage vs Price')

    # print('MILEAGE: ', X)
    # print(f"Shape of X: {X.shape}")
    # print(f"Shape of y: {y.shape}")
    # model = linReg(X, y)
    # print(model)
    # model = LinearRegression()
    # print(model)
    X_train, X_test, y_train, y_test = gatherInformation(X, y, model)
    # printReferenceTable(X_train, y_train, True, 'Mileage vs Price (Training set)')
    # printReferenceTable(X_test, y_test, True, 'Mileage vs Price (Test set)')

    filterByMiles = input("Filter by miles: ")
    price = model.predict([[int(filterByMiles)]])
    print(f'Price of car with {filterByMiles} miles: ', price)
    
    # error? the difference is the actual values and the predicted values: y_test and y_prod

    # print("Mean squared error: ", mean_squared_error(y_test, y_prod))
    # print("R2 score: ", r2_score(y_test, y_prod))

    # print('Slope: ', model.coef_)
    # print('Intercept: ', model.intercept_)

if __name__ == "__main__":
    main()
