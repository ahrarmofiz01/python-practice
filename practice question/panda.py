import pandas as pd
pd.__version__
df=pd.DataFrame([1,2,3],columns=['column_number'])
print(type(df))
print(df)
data={
    'name':['alice','bob','charlie'],
    'age':[25,30,35],
    'salary':[50000,60000,70000]
}
df=pd.DataFrame(data)
print(df)
print(df.head(1))#top rows
print(df.shape)
print(df.columns)
df.rename(columns={'name': 'NAME'},inplace=True)
print(df.NAME)
print(df)
print(df.info)
print(df.describe())
#save and load data from csv
df.to_csv('test_data.csv')
df=pd.read_csv('test_data.csv')
print(df[['NAME']])
print(df.loc[df.salary>=50000])