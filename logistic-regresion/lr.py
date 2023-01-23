import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as pt
import numpy as np
customer = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

customer.head()
x = customer[['tenure']].values
y = customer[['Churn']].values


log_model = LogisticRegression()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.35)
log_model.fit(x_train, y_train)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1,  max_iter=100, multi_class='warn', n_jobs=None, penalty='12', random_state=None, solver='warn', tol=0.0001, verbose=0, warm_start=False)

y_pred = log_model.predict(x_test)
pt.scatter(x,y)
pt.plot([n for n in  range(len(y_pred))],y_pred)
pt.show()

