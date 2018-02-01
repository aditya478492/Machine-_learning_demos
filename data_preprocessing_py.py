import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Data.csv');
x2 = dataset.iloc[:,:-1].values;
y = dataset.iloc[:,3].values;

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0);
imputer=imputer.fit(x2[:,1:3]);
x2[:,1:3]=imputer.transform(x2[:,1:3]);

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder();
labelencoder_X=labelencoder_X.fit(x2[:,0]);
x2[:,0]=labelencoder_X.transform(x2[:,0]);

onehotencoder=OneHotEncoder(categorical_features=[0]);
x2=onehotencoder.fit_transform(x2).toarray();

labelencoder_Y=LabelEncoder();
y=labelencoder_Y.fit_transform(y);

#Train and test datset division
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x2,y,train_size=0.2,random_state=0);

#Standardiztion
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler();
X_train=scaler.fit_transform(X_train);
X_test=scaler.fit(X_test);