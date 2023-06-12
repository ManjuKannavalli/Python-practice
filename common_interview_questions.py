# 1. Create 3 dictionaries with 3 key value pairs and convert them to pandas dataframe

dict_1 = {'feature_1':1,'feature_2':2,'feature_3':3}
dict_2 = {'feature_1':4,'feature_2':5.5,'feature_3':6}
dict_3 = {'feature_1':7,'feature_2':8.2,'feature_3':9}

import pandas as pd

df = pd.DataFrame([dict_1, dict_2, dict_3])
print(df.head())