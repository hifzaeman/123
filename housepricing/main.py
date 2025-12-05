import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
data=fetch_california_housing(as_frame=True)
df=data.frame
print(df.head(10))
print(df.describe())
print(df.isnull().sum())
X=df.drop("MedHouseVal",axis=1)
y=df["MedHouseVal"]
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scalar=StandardScaler()
X_train_scaled=scalar.fit_transform(X_train)
X_test_scaled=scalar.transform(X_test)
linmodel=LinearRegression()
linmodel.fit(X_train_scaled,y_train)
y_pred_lin=linmodel.predict(X_test_scaled)
rmse_lin=np.sqrt(mean_squared_error(y_test,y_pred_lin))
mae_lin=mean_absolute_error(y_test,y_pred_lin)
print(f"Linear Regression rmse {rmse_lin}")
print(f"Linear Regression mae {mae_lin}")
rf_model=RandomForestRegressor(n_estimators=200,
                                random_state=42)
rf_model.fit(X_train,y_train)
y_pred_rf=rf_model.predict(X_test)
rmse_rf=np.sqrt(mean_squared_error(y_test,y_pred_rf))
mae_rf=mean_absolute_error(y_test,y_pred_rf)
print(f"Linear Regression rmse {rmse_rf}")
print(f"Linear Regression mae {mae_rf}")
x_model=XGBRegressor(n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
    )
x_model.fit(X_train, y_train)
y_pred_x=x_model.predict(X_test)
rmse_x=np.sqrt(mean_squared_error(y_test, y_pred_x))
mae_x=mean_absolute_error(y_test, y_pred_x)
print(f"XGB Regression rmse {rmse_x}")
print(f"XGB Regression mae {mae_x}")