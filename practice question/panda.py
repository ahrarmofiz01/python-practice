import pandas as pd
df = pd.read_csv("/Users/ahrarmofiz/Downloads/archive (6)/customer_churn_dataset-testing-master.csv")
#print(df)
#print(df.head(10))#top 10 rows
#print(df.tail(5))#last 5 rows dikhata hai.
print(df.shape)#DataFrame me kitni rows aur kitne columns hain.
print(df.columns)#saare column ke naam
df.info()#Data ki information print karta hai
print(df.describe())#Numeric columns ki summary deta hai.
print(df["Age"])
print(df[["Age", "Tenure"]])# multiple columns select krne kay leye
print(df[df["Age"] > 30])
print(df[df["Age"] > 30])
print(df[df["Churn"] == "Yes"])
print(df[df["Age"] > 50])