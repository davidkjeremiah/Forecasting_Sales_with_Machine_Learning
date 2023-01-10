# Forcasting Sales with Machine Learning

## Import needed libraries
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

## Load Data
# read in the data
df = pd.read_csv('sales_data.csv')

df.head()

## Select the features and target variables
X = df[['week', 'month', 'year', 'product_id', 'advertising_spend']]
y = df['sales']

## Split the data into training and testing sets
# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Create the model
# model = RandomForestRegressor()
model = LinearRegression()

## Train the model
model.fit(X_train, y_train)

## Make Predictions on the testing set
y_pred = model.predict(X_test)

print(y_pred)
print(X_test)
print(y_test)

## Calculate the model's performance
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae: .2f}')



