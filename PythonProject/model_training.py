import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib



labels = ["nothing","up","down","left","right"]
data = pd.read_csv("C:\\Users\\laurm\\Desktop\\changerates_fixed_data.csv",header=None)
print(data.head())
print(data.shape)
print(data.info())
print(data.dtypes)
y = data[40]
X = data.drop(40, axis = 1)
print(y)
X_train,X_test,y_train,y_test=train_test_split(
    X,y, 
    train_size = 0.80, 
    random_state = 48)

print(X_train)
print(y_train)

# LogisticRegression with One Vs Rest Mulit Class and High Regularization 
lr_ovr = LogisticRegression(C=0.01, multi_class='ovr')

# Fitting and Predicting
lr_ovr.fit(X_train, y_train)
y_pred = lr_ovr.predict(X_test)

joblib.dump(lr_ovr, 'C:\\Users\\laurm\\Desktop\\brainwave_model.pkl')


print("Accuracy Score        : ",accuracy_score(y_test, y_pred))
print("Classification Report : \n", classification_report(y_test, y_pred))

# lr_ovr = joblib.load('C:\\Users\\laurm\\Desktop\\brainwave_model.pkl')
# new_test_data = pd.read_csv("C:\\Users\\laurm\\Desktop\\ModelTesting\\changerates_test_data.csv",header=None)
# new_pred = lr_ovr.predict(new_test_data)
# print(new_pred)


