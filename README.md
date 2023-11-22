**Explore my project on Streamlit:** [Rock Paper Scissors Prediction](https://rock-paper-sciapprs-prediction-das.streamlit.app/)
# Overview
## Data
This dataset contains 2188 images, specifically 712 images of paper pose, 726 images of rock pose, and 750 images of scissors pose. The size of each image is 300 × 200, with RGB color, and the background image is green.

![paper pose](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/ea1b1d8e-af54-4ab7-b52a-b1b3f78f6475)
![rock pose](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/6da7b213-9255-4be0-af30-0d179ddea096)
![scissors pose](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/914edcd8-ea6f-4832-99fc-ee7bee80b929)
## Objective
Make a model that can classify a rock-paper-scissors hand pose with Convolutional Neural Network.
# Data Augmentation
Use Data Augmentation to make changes to training data. That way, the model can be used to predict a variety of images. The table below shows an example of an image before and after data augmentation.

The dataset is also grayscaled to reduce the complexity of color dimensions. Not only that, the input image background doesn't have to be green to be classified easily.

| Before | After Augmentation | After Grayscale |
| ------- | ------ |------ |
| ![rock pose before augmentation](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/224b0c39-2182-4ea4-93c1-cc2e3f762632)|![rock pose after augmentation](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/2be3c28b-d161-4a3b-a370-048ee2a48162)| ![grayzoom-skewed-flip 1](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/859e2bfe-06f4-4adc-87ef-a594e0a7176d)
|

# Modeling
The convolutional Neural Network (CNN) is used to classify rock-paper-scissors hand pose. CNN has convolutional layers to get a pattern from the input image. This pattern is called feature maps. The image below contains an example of feature maps with a rock hand pose.

![conv2d](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/c5018beb-fb9a-4f45-9cdb-ff87083274e5)

But, instead of a Fully connected layer, this CNN model uses Global Max Pooling to prevent overfitting by getting the maximum pixel value from each feature map and sending it directly to the output layer. Another layer is global average pooling, which takes the average pixel value of each feature map.

Lastly, to get a model with good performance, the model checkpoint is used to get the desirable model. The model with a great monitored metric score compared to the model from the previous method will be saved.

# Result
## Training Performance
![Accuracy performance](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/9ca76cb1-1428-4618-9fb8-ad6b77cf3b4c)

The graph above displays how well the model learned during training. In the second round, it got a 92% accuracy on new data, and in the fourth round, it hit 90% on the training data. 

## Confusion Matrix

### Model from the last epoch

**Model from last epoch** reach **98%** validation accuracy and **97%** on training accuracy (accuracy: 0.9726, val_accuracy: 0.9886). The heatmap below shows the rest of the classified data.
![confusion-matrix](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/a282433b-6219-4642-b194-1a6268317eb6)

### Model with the highest validation accuracy score
**Saved model** reach **99%** on validation accuracy and **96%** on training accuracy (accuracy: 0.9665, val_accuracy: 0.9920). The heatmap below shows the rest of the classified data.
![confusion-matrix-1](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/b5768079-79d5-4847-88ed-aa1b773e90e6)

## Analyze
Even though the saved model has the highest validation accuracy, when we compare each model's confusion matrix, **the model from the last epoch has the most correct guesses than saved models on training data.**

Model from last epoch correct guesses on training data:
**(Paper:420, Rock:420, Scissors:444)**

Saved Model from last epoch correct guesses on training data:
**(Paper:409, Rock:430, Scissors:422)**

In validation data, **saved model guess correctly more on paper and rock.** while **model from last epoch only guesses correctly more on scissors**.

Model from last epoch correct guesses on validation data:
**(Paper:279, Rock:287, Scissors:300)**

Saved Model from last epoch correct guesses on validation data:
**(Paper: 282, Rock:289, Scissors:298)**

## Chosen Model
From the performance,**the difference between training and validation accuracy is lower on a model from the last epoch than on a saved model**.

The difference in the accuracy of each model:

**Saved model:** |0.9665 - 0.9920| = 0.0255

**Model from the last epoch:** |0.9726 - 0.9886| = 0.016

High difference accuracy on the saved model might indicate overfitting. Therefore, **the model from the last epoch is chosen to predict unfamiliar data.**
## Predict Unfamiliar data
The image below shows scissors pose with different hands, transparent background, and position is guessed correctly.
![Predict-unfamiliar-image](https://github.com/imandreans/Rock-Paper-Scissors-Prediction/assets/69078720/a6def887-1f58-4c4b-be78-30eb8b30606a)

# Citation
de la Bruère-Terreault, J. (2017). A Rock-Paper-Scissors game using computer vision and machine learning on Raspberry Pi. GitHub repository. https://github.com/DrGFreeman/rps-cv/tree/master

Lin, M., Chen, Q., & Yan, S. (2014, March 4). Network in Network. arXiv.org. https://doi.org/10.48550/arXiv.1312.4400 
