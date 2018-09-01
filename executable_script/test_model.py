import pandas as pd

data = pd.read_csv('train_E6oV3lV.csv')
data['word_count'] = data['tweet'].apply(lambda x: len(str(x).split(" ")))
data['char_count'] = data['tweet'].str.len()
print(data.head())
data.to_csv('dump.csv')
