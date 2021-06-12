#IMPORTING THE LIBARIES AND DEPENDENCIES

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('diabetes.csv')
pd.read_csv

###Not Neccessary but if you want remove the'#'to print)

# printing the first 5 rows of the dataset 
#print (diabetes_dataset.head())

# number of rows and Columns in this dataset
#print (diabetes_dataset.shape)

# getting the statistical measures of the data
#print (diabetes_dataset.describe())

# Outcome: 0 -> Non-diabetic 1-> Diabetic

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

#Data Standardization

scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
#print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']
#print(X)
#print(Y)

#Train_Test_Split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
#print(X.shape, X_train.shape, X_test.shape)

#Training the Model

classifier = svm.SVC(kernel='linear')
#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

#Model Evaluation
#Accuracy Score

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)

# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)

#Making a Predictive System

input_data =(5,166,72,19,175,25.8,0.587,51) #(Positive)

#input_data = (1,85,66,29,0,26.6,0.351,31) #(Negative)



# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')
