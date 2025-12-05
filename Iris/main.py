import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import mean_absolute_error,mean_squared_error,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
data=load_iris()
# d=data.frame
# print(d.head(10))
# print(d.info())
# print(d.describe())
# print(d.isnull().sum())
x=data.data
y=data.target
print(data.DESCR)
iris_data=DataFrame(x,columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
iris_target=DataFrame(y,columns=['Species'])
def flower(num):
    if num==0:
        return "Setosa"
    elif num==1:
        return "Versocolour"
    else:
        return "Virginica"
iris_target["Species"]=iris_target["Species"].apply(flower)
data = pd.concat([iris_data, iris_target], axis=1)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)
iris_model=LogisticRegression()
iris_model.fit(X_train,y_train)
y_pred=iris_model.predict(X_test)
print(f"Accuracy is: {accuracy_score(y_test,y_pred)}")
k_model=KNeighborsClassifier()
k_model.fit(X_train,y_train)
k_pred=k_model.predict(X_test)
print(f"Accuracy with KNN{accuracy_score(y_test,k_pred)}")