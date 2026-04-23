import pandas as pd

data={
    'name':['Qamar','kamran','ali'],
    'age':[21,None,23],
    'salary':[230000,None,250000]
}

pf=pd.DataFrame(data)

print("Original Data")
print(pf)

print("\nMissing Values")
print(pf.isnull().sum())

drop_value=pf.dropna()
print("\nAfter Dropping Missing Rows")
print(drop_value)

pf['age'] = pf['age'].fillna(pf['age'].mean())
pf['salary'] = pf['salary'].fillna(pf['salary'].mean())

print("\nAfter Filling Missing Values With Mean")
print(pf)
