import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('Position_Salaries.csv');
X=dataset.iloc[:,1:2].values;
Y=dataset.iloc[:,2:3].values;

from sklearn.preprocessing import PolynomialFeatures
reg_poly=PolynomialFeatures(degree=4);
X_poly=reg_poly.fit_transform(X);
reg_poly.fit(X_poly,Y);

from sklearn.linear_model import LinearRegression
reg_lin=LinearRegression();
reg_lin.fit(X_poly,Y);

X_acc=np.arange(0.0,10,0.1);
X_acc=X_acc.reshape((len(X_acc)),1);
plt.scatter(X,Y,color='red')
plt.plot(X_acc,reg_lin.predict(reg_poly.fit_transform(X_acc)),color='blue')
plt.show()

reg_lin.predict(reg_poly.fit_transform(6.5))

