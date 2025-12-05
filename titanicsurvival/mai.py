import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
train_data=pd.read_csv("data/train.csv")
test_data=pd.read_csv("data/test.csv")
print(train_data.info())
print(train_data.shape)
print(train_data.columns)
print(train_data["Sex"].value_counts())
train_data["Died"]=1-train_data["Survived"]
train_data.groupby("Sex")[["Survived", "Died"]].sum().plot(
kind="bar",figsize=(10,5),stacked=True)
#plt.show()
figure=plt.figure(figsize=(10,5))
plt.hist([train_data[train_data["Survived"]==1]["Fare"],train_data[train_data["Survived"]==0]["Fare"]],stacked=True, bins=50, label=["Survived","Died"])
plt.xlabel("Fare")
plt.ylabel("No of Passengers")
plt.legend()
plt.show()
df1=train_data.drop(["Name","Ticket","Cabin","PassengerId","Died"], axis=1)
print(df1.head(10))
df1.Sex=df1.Sex.map({"female":0,"male":1})
df1.Embarked=df1.Embarked.map({"S":0,"Q":1,"C":2,"nan":"Nan"})
print(df1.head())
mean_age_men=df1[df1["Sex"]==1]["Age"].mean()
mean_age_women=df1[df1["Sex"]==0]["Age"].mean()
print(df1.isnull().sum())
df1.loc[(df1.Age.isnull())&(df1["Sex"]==0),"Age"]=mean_age_women
df1.loc[(df1.Age.isnull())&(df1["Sex"]==1),"Age"]=mean_age_men
print(df1.isnull().sum())
df1.dropna(inplace=True)
print(df1.isnull().sum())
df1.Age=(df1.Age-min(df1.Age))/(max(df1.Age)-min(df1.Age))
df1.Fare=(df1.Fare-min(df1.Fare))/(max(df1.Fare)-min(df1.Fare))
print(df1.describe)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
train_X,test_X,train_y,test_y=train_test_split(
    df1.drop(["Survived"],axis=1),
    df1.Survived,
    test_size=0.2,
    random_state=0,
    stratify=df1.Survived
)
lrmod=LogisticRegression()
lrmod.fit(train_X,train_y)
y_predict=lrmod.predict(test_X)
print(accuracy_score(test_y,y_predict))
cma=confusion_matrix(test_y,y_predict)
#sns.heatmap(cma,annot=True)
df2=test_data.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
df2.Sex=df2.Sex.map({"female":0,"male":1})
df2.Embarked=df2.Embarked.map({"S":0,"Q":1,"C":2,"nan":"Nan"})
print(df2.isnull().sum())
mean_age_men2=df2[df2["Sex"]==1]["Age"].mean()
mean_age_women2=df2[df2["Sex"]==0]["Age"].mean()
df2.loc[(df2.Age.isnull())&(df2["Sex"]==0),"Age"]=mean_age_women
df2.loc[(df2.Age.isnull())&(df2["Sex"]==1),"Age"]=mean_age_men
df2["Fare"]=df2["Fare"].fillna(df2["Fare"].mean())
df2.Age=(df2.Age-min(df2.Age))/(max(df2.Age)-min(df2.Age))
df2.Fare=(df2.Fare-min(df2.Fare))/(max(df2.Fare)-min(df2.Fare))
prediction=lrmod.predict(df2)
print(prediction)
submission=pd.DataFrame({"PassengerId":test_data["PassengerId"],"Survived":prediction})
submission.to_csv("submission.csv",index=False)
prediction_df=pd.read_csv("submission.csv")
sns.countplot(x="Survived",data=prediction_df)
plt.title("Predicted Survival Counts")
plt.xlabel("Survived (1 = Yes, 0 = No)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()