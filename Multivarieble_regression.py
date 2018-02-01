import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('50_Startups.csv');
X=dataset.iloc[:,:-1].values;
Y=dataset.iloc[:,4].values;

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder();
X[:,3]=labelencoder.fit_transform(X[:,3]);
onehotencoder=OneHotEncoder(categorical_features=[3]);
X=onehotencoder.fit_transform(X).toarray();

X=X[:,1:6];

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_opt,Y,test_size=0.2,random_state=0);

from sklearn.linear_model import LinearRegression
regressor=LinearRegression();
regressor.fit(X_train,Y_train);
Y_pred=regressor.predict(X_test);

import statsmodels.formula.api as sm
#adding intercept to the matrix
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1);
X_opt=X[:,[0,1,2,3,4,5]];
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit();
regressor_OLS.summary()

#remove the first independent varieble with highest p-value
X_opt=X[:,[0,1,3,4,5]];
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit();
regressor_OLS.summary()

X_opt=X_opt[:,[0,2,3,4]];
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit();
regressor_OLS.summary()

X_opt=X_opt[:,[0,1,3]];
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit();
regressor_OLS.summary()

X_opt=X_opt[:,[0,1]];
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit();
regressor_OLS.summary()

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_opt,Y,test_size=0.2,random_state=0);

from sklearn.linear_model import LinearRegression
regressor=LinearRegression();
regressor.fit(X_train,Y_train);
Y_pred=regressor.predict(X_test);

