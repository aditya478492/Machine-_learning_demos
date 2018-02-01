import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("Salary_Data.csv");
X=dataset.iloc[:,:-1].values;
Y=dataset.iloc[:,1].values;

#creating training and test data sets
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0);

#model for learning
from sklearn.linear_model import LinearRegression
regressor=LinearRegression();
regressor.fit(X_train,Y_train);

#predicting test data
Y_pred=regressor.predict(X_test);

#plotting a graph
plt.scatter(X_test,Y_test,color='red');
plt.plot(X_train,regressor.predict(X_train),color='blue');
plt.xlabel('Years of experience');
plt.ylabel('Salary');
plt.show()