# Simple Linear Regression

# Importing the libraries
import numpy as np
import keras
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
#tf.logging.set_verbosity(tf.logging.ERROR)

from tensorflow import keras
from tensorflow import lite

# Importing the dataset
dataset = pd.read_csv('C:/Users/user/Downloads/P14-Part2-Regression/P14-Part2-Regression/Section 6 - Simple Linear Regression/Python/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
io=tf.keras.layers.Dense(units=2,input_shape=[2])
io2=tf.keras.layers.Dense(units=2)
#io3=tf.keras.layers.Dense(units=3)
io4=tf.keras.layers.Dense(units=1)
model=tf.keras.Sequential([io,io2,io4])
model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(X_train, y_train)
# Predicting the Test set results
y_pred = model.predict(X_test)
#print(g)


kearas_file = "linear.h5"
tf.keras.models.save_model(model,kearas_file)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tfmodel = converter.convert()
open("linear.tflite","wb").write(tfmodel)



