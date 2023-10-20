# Build-a-ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker

This repository contains image classification model for classification of images of motorcycle and bicycle.
The images for training the model are taken from CIFAR-100 dataset.
THe model trained to classify images in two classes is then deployed using AWS endpoints.
Finally, an orchestrated workflow of 3 lambda functions is created which invoke 3 lambda function in order to get encoded image data then to classiy the image data and lastly defining output based on threshold confidance.


### 1. Data Staging
The image data is downloaded and extracted from cifar.tar.gz This dataset file is hosted at https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz
The data is transformed into usable format and uploaded to S3 bucket.

### 2. Model training and deployement
Train the model and deploy the model by creating a AWS sagemaker endpoint

### 3. Creating lambda functions and a workflow using step function
The lambda functions are created to create a workflow which can be used to input a image and classify image then decide if prediction is good or not based on threeshold confidance.

first lambda function downloads image from S3 bucket and serializes image data using base64 encoding.

second lambda function uses the output of first lambda function as input to image classifier model and predicts inference for the image. This is further given as input to third lambda function.

third lambda function gets inference as input i.e. a two element list giving probability of a class. It filters the low confidence predictions based on threshold value of output provided by us. We have used 0.8 as threshold.


The workflow of three lambda functions is orchestrated using step function. There we will need to provide input for first lambda function and further lambda functions will be invoked in a flow by output of previuos lambda function.
Step function workflows are easy for integration with other services of AWS. Hence it becomes easy to add a flow of steps in a pipeline.
