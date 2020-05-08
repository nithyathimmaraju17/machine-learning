import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Salary_Data.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

#splitting the dataset
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain, ytrain)

#predicting test set result
ypred = regressor.predict(xtest)

#visualising the training set
plt.scatter(xtrain, ytrain, color = 'red')
plt.plot(xtrain, regressor.predict(xtrain), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()