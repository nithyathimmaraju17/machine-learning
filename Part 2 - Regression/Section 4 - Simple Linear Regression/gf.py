import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
set = pd.read_csv('Salary_Data.csv')
x = set.iloc[:,:-1].values
y = set.iloc[:,3].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)