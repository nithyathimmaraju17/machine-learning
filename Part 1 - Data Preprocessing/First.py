import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
set1 = pd.read_csv('Data.csv')
x1 = set1.iloc[:,:-1].values
y1 = set1.iloc[:,3].values

#Missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'most_frequent',axis = 0 )
imputer = imputer.fit(x1[:, 1:3])
x1[:, 1:3] = imputer.transform(x1[:, 1:3]) 

#LabeleEncoder, Encoding categorical 
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_x= LabelEncoder()
x1[:, 0] =label_x.fit_transform(x1[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x1= onehotencoder.fit_transform(x1).toarray()

# Splitting dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x1,y1,test_size = 0.2,random_state = 0)
 
#feature selection
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
