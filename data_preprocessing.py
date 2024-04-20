import pandas as pd
from main import data

dataset = pd.DataFrame(data)
#print(dataset)

print(dataset.isnull().sum())