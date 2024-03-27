import pandas as pd
from sklearn.impute import KNNImputer

data = pd.read_csv("Z:\waterquality\dataset\water_potability.csv")

imputer = KNNImputer()
data_imputed = imputer.fit_transform(data)
data = pd.DataFrame(data_imputed, columns=data.columns)
data.to_csv("dataset\data_cleaned.csv", index=False)

