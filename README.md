# Multivariate_Time_Series_Sentinel5P
Research 

In this work we analyse remote sensing environmental data and make ground level prediction we it. 

We also apply geometric image correction to the remote sensing imagery. 


The repository is composed of 6 stages: 

1.	Dowloading Data API

To ensure optimal performance and ease of use, we recommend utilising a cloud system, such as Google Drive, to query and store new data. This is especially useful when attempting to download information for a long period of time. The data will be downloaded in NetCDF format, and it is important to specify the desired period in the file download.py.

To properly utilize the system, it is necessary to install the following packages:

•	harp-image-preprocess
•	sentinelsat

To run the command line from a Colab notebook, for example, the snippet will look something like this:

 <img width="320" alt="image" src="https://user-images.githubusercontent.com/71643605/208252655-4a727baf-e43b-4e64-8c56-4373dcc2127c.png">

	
-f is the path to the folder we want to store the data. 

 <img width="619" alt="image" src="https://user-images.githubusercontent.com/71643605/208252685-2e8c7cdf-8dca-4321-add1-374db0fedde3.png">


2.	Pre-processing and Visualisation

‘This Jupyter notebook, named 'Chapter_3_2_Data_Preprocessing.ipynb', processes large NetCDF files by extracting relevant features from the 'Product' group and saving them as a CSV file on google drive (name: final_data_May20_Sept22.csv). The resulting CSV can be used for the rest of the experiment. 

Before running this notebook, make sure to download the necessary satellite-related packages: 


<img width="320" alt="image" src="https://user-images.githubusercontent.com/71643605/208252689-6a764309-8031-45fc-87bb-d4ceca6a8d39.png">


3.	LSTM

Long Short-Term Memory (LSTM) is a type of recurrent neural network that is commonly used in natural language processing and time series forecasting. It is specifically designed to remember important information from long periods of time, while still being able to learn new information.

To use LSTM in TensorFlow, you will need to install the TensorFlow library and import it into your code.

 <img width="330" alt="image" src="https://user-images.githubusercontent.com/71643605/208252700-57285fb4-4504-41ec-a604-656461750173.png">


4.	NeuralProphet

NeuralProphet is a Python package for time series forecasting using deep learning. It is an extension of the Prophet package, which is a popular open-source library for time series forecasting developed by Facebook. NeuralProphet uses a neural network-based approach for forecasting, which can potentially provide more accurate forecasts for complex time series.

5.	Regression 

•	PyCaret

PyCaret is an open-source, low-code machine learning library in Python that aims to make the process of training and deploying machine learning models easier and more efficient. It provides a range of tools and functions for tasks such as data preparation, feature selection, model training, model evaluation, and model deployment.

Required Packages:

 <img width="320" alt="image" src="https://user-images.githubusercontent.com/71643605/208252708-fbe147e6-add9-4e6f-847a-9c1acf7e0143.png">


•	XGBoost with Scikit-learn

XGBoost (eXtreme Gradient Boosting) is an open-source library for implementing gradient boosting algorithms in Python.

 <img width="320" alt="image" src="https://user-images.githubusercontent.com/71643605/208252715-0954e71c-a9e2-430e-86f5-e8337e201e8b.png">



6.	Geometric Correction and Visualisation
We can run the experiment from the file Chapter_4.4.2_Correction.ipynb. The data used are available in the folder Data: onsample_sep1.csv and new_grid.csv.
