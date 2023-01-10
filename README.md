# Project Title

Sales Forecasting using Machine Learning

## Introduction

This project aims to forecast sales using machine learning techniques, with the goal of predicting future product demand based on past sales data in order to optimize production and inventory management.

## Data

The dataset used for this project contains historical sales data for various products. It includes six columns such as information on date of sale (week, month, year), product_id, advertising_spend, and sales. The `week` and `month` columns represent the week and month in which the sales occurred, and the `year` column represents the year in which the sales occurred. The `product_id` column represents the unique identifier for the product that was sold, and the `advertising_spend` column represents the amount of money spent on advertising for the product. The `sales` column represents the number of units of the product that were sold.

When this data is used with the code provided in the forcast_sale.py file, the resulting model will be trained to predict the number of sales based on the week, month, year, product_id, and advertising_spend of each sale. The model will then be tested on a separate set of data to evaluate its performance.

## Data Preparation

The first step in this project was to clean and preprocess the data. This included handling missing values, and converting data types.

## Model selection and Results

A variety of machine learning models were evaluated for this task including linear regression and random forest. Through experimentation and cross-validation, the linear regression model was found to be the best performer. Hence, it's usage in this project. 

For example, random forest achieved a `MAE of 125.5`, which means that, on average, the model's predictions were off by 125.5 units of sales. However, a lower MAE would be a better fit of the model and a higher accuracy of the predictions. Therefore, with linear regression model it achieved a `MAE of 57.14`. Compared to the score of random forest's model output (125.5), 57.14 is considered to be very good.

## Dependencies

* Python 3.6+
* pandas
* numpy
* scikit-learn

## Usage
The main file to run is `forecase_sales.py`. The dataset `sales_data.csv` is also required to run this file. The file can be run on command line by typing `python forcast_sales.py`

## Note

It is important to note that this is a simplified example and for educational purposes. In a real-world scenario, you will have to do more preprocessing, cleaning and feature engineering on your data. Also, you will have to choose and experiment with other models, check cross validation and fine-tune the parameters to optimize the performance. Additionally, you may need to gather more data and run more tests to ensure the model generalizes well to new unseen data.

However, the main insight from this project is that it is possible to use machine learning techniques, such as Linear Regression, to predict future product demand based on past sales data. By training a model on historical data and evaluating its performance on a separate testing set, you can get a sense of how well the model is able to make predictions and identify any areas for improvement.

In general, this type of project could be useful for a manufacturing company that wants to better understand and forecast product demand in order to optimize production and inventory management. By using data-driven techniques to predict demand, the company can make more informed decisions about how much of each product to produce and when to produce it, which can help to reduce waste, lower costs, and increase efficiency.
