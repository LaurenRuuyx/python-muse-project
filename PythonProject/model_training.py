import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

data = pd.read_csv("C:\\Users\\laurm\\Desktop\\shuffled_data - Copy.csv",header=None)
print(data.head())
print(data.shape)
print(data.info())
print(data.dtypes)
y = data[1200]
X = data.drop(1200, axis = 1)
print(y)
X_train,X_test,y_train,y_test=train_test_split(
    X,y, 
    train_size = 0.80, 
    random_state = 1)




