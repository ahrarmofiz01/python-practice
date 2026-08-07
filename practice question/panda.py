import pandas as pd
df = pd.read_csv("/Users/ahrarmofiz/Downloads/archive (6)/customer_churn_dataset-testing-master.csv")
print(df)
print(df.head(10))#top 10 rows
print(df.tail(5))#last 5 rows dikhata hai.
print(df.shape)