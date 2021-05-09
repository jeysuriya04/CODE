# CONVERTING MACHINE LEARNING MODEL INTO TENSORFLOWLITE FORMAT
TensorFlow Lite inference typically follows the following steps:

Loading a model

You must load the .tflite model into memory, which contains the model's execution graph.

Transforming data

Raw input data for the model generally does not match the input data format expected by the model. For example, you might need to resize an image or change the image format to be compatible with the model.

Running inference

This step involves using the TensorFlow Lite API to execute the model. It involves a few steps such as building the interpreter, and allocating tensors, as described in the following sections.

Interpreting output

When you receive results from the model inference, you must interpret the tensors in a meaningful way that's useful in your application.

For example, a model might return only a list of probabilities. It's up to you to map the probabilities to relevant categories and present it to your end-user.



# MULTIPLE LINEAR REGRESSION:

multiple linear regression (MLR), also known simply as multiple regression, is a statistical technique that uses several explanatory variables to predict the outcome of a response variable. The goal of multiple linear regression (MLR) is to model the linear relationship between the explanatory (independent) variables and response (dependent) variable.

![image](https://user-images.githubusercontent.com/53963913/117569877-5087ab80-b0e5-11eb-91c2-3620dc836f8f.png)


# CONVERTING THE ML FILE INTO .TFLITE :
![image](https://user-images.githubusercontent.com/53963913/117569928-993f6480-b0e5-11eb-8d5f-ca9889b1c26c.png)

# code
import tensorflow as tf

#Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) # path to the SavedModel directory
tflite_model = converter.convert()

#Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)
(here i had uploaded a code consist of the required files like asset files, java files , xml files and gradle files)
