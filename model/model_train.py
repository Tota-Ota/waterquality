import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('dataset\data_cleaned.csv')

X = df[['ph', 'Turbidity']]
y = df.drop(columns=['ph', 'Turbidity'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

#Example
input_values = [[7.0, 5.6]]
output_values = model.predict(input_values)
print("Predicted Water Quality Parameters:", output_values)
