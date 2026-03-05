import pandas as pd
from Linear_regression import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv('linear regression/homeprices.csv')
X=df.iloc[:,:-1]
y=df.iloc[:,(-1)]
print(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model1=LinearRegression()
model1.fit(X_train,y_train)
model1.predict(X)

