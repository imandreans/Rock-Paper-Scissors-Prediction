**Explore my project on Streamlit:** [Rock Paper Scissors Prediction](https://rock-paper-sciapprs-prediction-das.streamlit.app/)
# Overview
## Data
This dataset contains 2188 images, specifically 712 images of paper pose, 726 images of rock pose, and 750 images of scissors pose. The size of each image is 300 × 200, with RGB color, and the background image is green.
![04l5I8TqdzF9WDMJ](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/ea1b1d8e-af54-4ab7-b52a-b1b3f78f6475)
![0Flw60Z2MAWWKn6S](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/6da7b213-9255-4be0-af30-0d179ddea096)
![02vG75hQW9Vp4oTl](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/914edcd8-ea6f-4832-99fc-ee7bee80b929)
## Objective
The creator of this dataset used a green screen to remove the background easily and take the hand pose only. How does the model classify input with differences, like position and size of hand pose?
# Data Augmentation
Use Data Augmentation to make changes to training data. That way, the model can be used to predict a variety of images.
| Before | After |
| ----------- | ------ |
| ![00nKV8oHuTGi20gq](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/224b0c39-2182-4ea4-93c1-cc2e3f762632)|![zoom-skewed-flip 1](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/2be3c28b-d161-4a3b-a370-048ee2a48162)|
# Modeling
The convolutional Neural Network (CNN) is used to classify rock-paper-scissors hand pose. CNN has convolutional layers to get a pattern from the input image. This pattern is called feature maps.

![conv_layer1](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/f5992d04-e15a-4fc4-bc5d-56e6af15984d)

But, instead of a Fully connected layer, this CNN model uses Global Max Pooling to prevent overfitting by getting the maximum pixel value from each feature map and sending it directly to the output layer. Another layer is global average pooling, which takes the average pixel value of each feature map.

Lastly, to get a model with good performance, the model checkpoint is used to get the desirable model. The model with a great monitored metric score compared to the model from the previous method will be saved.

# Result
## Training Performance
![Accuracy](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/9ca76cb1-1428-4618-9fb8-ad6b77cf3b4c)

The graph displays how well the model learned during training. In the second round, it got a 92% accuracy on new data, and in the fourth round, it hit 90% on the training data. 

## Confusion Matrix

### Model from the last epoch

**Model from last epoch** reach **98%** validation accuracy and **97%** on training accuracy(accuracy: 0.9726, val_accuracy: 0.9886).
![Untitled](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/a282433b-6219-4642-b194-1a6268317eb6)

### Model with the highest validation accuracy score
**Saved model** reach **99%** on validation accuracy and **96%** on training accuracy (accuracy: 0.9665, val_accuracy: 0.9920).
![Untitled-1](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/b5768079-79d5-4847-88ed-aa1b773e90e6)

## Analyze
Even though the saved model has the highest validation accuracy, when we compare each model's confusion matrix, **the model from the last epoch has the most correct guesses than saved models on training data.**

Model from last epoch correct guesses on training data:
**(Paper:420, Rock:420, Scissors:444)**

Saved Model from last epoch correct guesses on training data:
**(Paper:409, Rock:430, Scissors:422)**
<br><br>
In validation data, **saved model guess correctly more on paper and rock.** while **model from last epoch only guesses correctly more on scissors**.
<br><br>
Model from last epoch correct guesses on validation data:
**(Paper:279, Rock:287, Scissors:300)**

Saved Model from last epoch correct guesses on validation data:
**(Paper: 282, Rock:289, Scissors:298)**

## Chosen Model
From the performance,**the difference between training and validation accuracy is lower on a model from the last epoch than on a saved model**.
<br><br>
The difference in the accuracy of each model:

**Saved model:** |0.9665 - 0.9920| = 0.0255

**Model from the last epoch:** |0.9726 - 0.9886| = 0.016
<br><br>
High difference accuracy on the saved model might indicate overfitting. Therefore, **the model from the last epoch is chosen to predict unfamiliar data.**

# Citation
A Rock-Paper-Scissors game using computer vision and machine learning on Raspberry Pi.
By Julien de la Bruère-Terreault (drgfreeman@tuta.io). https://github.com/DrGFreeman/rps-cv/tree/master

https://arxiv.org/abs/1312.4400v3
