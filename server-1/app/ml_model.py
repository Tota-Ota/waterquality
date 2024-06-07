import os
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


def Predict( ph, Turbidity ):

    file_path = os.environ['DATA_CSV']

    warnings.filterwarnings(action='ignore', category=UserWarning, message="X does not have valid feature names")

    df = pd.read_csv(file_path)

    X = df[['ph', 'Turbidity']]

    y = df.drop(columns=['ph', 'Turbidity'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, y_train)

    # Predict

    input_values = [[ ph, Turbidity ]]

    output = model.predict(input_values).tolist()[0]

    output[-1] *= 100

    output[-2] /= 100

    output[1] /= 100


    offsets = [60, 0, 3.5, 125, 0, 10, 0, 0, 0]

    for i in range(len(output)):
        output[i] = round(output[i], 1) - offsets[i]

    return output

