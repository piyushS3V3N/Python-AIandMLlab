'''
    Import the required libraries for Linear Regression
    -> Pandas : to load CSV file
    -> skleanr.linear_model : to use LinearRegression Module
    -> sklearn.model_selection : to splite the data into training and testing dataset.
    -> sklearn.metrics : to calculate mean_absolute_error, mean_squared_error, median_absolute_error and r2_score 
    -> matplotlib.pyplot : to plot the output.
'''

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
import matplotlib.pyplot as pt

'''
    Load the "boston.csv" dataset file using pandas read_csv() Method
'''
boston = pd.read_csv('Boston.csv')
'''
    Get the reuired rows values 
    (splitting in values as it would make it easier to later on use to plot the prediction values)
'''
y = boston[["medv"]].values
x = boston[["lstat"]].values

'''
    Split data in 2 Category
    test_data : 
    train_data : 
'''
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

'''
    Initialize the object for LinearRegression Class with default values
'''
lr = LinearRegression()
'''
    Fit the x_train and y_train values
'''
lr.fit(x_train,y_train)
'''
    predict the value using x_test value for above trained model
'''
y_pred = lr.predict(x_test)

'''
    now plot the values first scatter plot the training vales
    then we draw the plot for our prediction values
'''
pt.scatter(x,y,c='r')
pt.scatter(y_test, y_pred, color='k')

print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred), 2)) 
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred), 2)) 
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred), 2)) 
print("Explain variance score =", round(sm.explained_variance_score(y_test, y_pred), 2)) 

pt.show()


