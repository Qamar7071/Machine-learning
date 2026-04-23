import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = pd.read_csv('file', sep='|')

data.columns = data.columns.str.strip()

pf = pd.DataFrame(data)

print("Original Data")
print(pf)

print("Null Values")
print(pf.isnull().sum())

la_data = pf.copy()

encode = LabelEncoder()

la_data["Gender Encoder"] = encode.fit_transform(la_data["Gender"])
la_data["Department Encoder"] = encode.fit_transform(la_data["Department"])
onehot=pd.get_dummies(la_data[['Gender','Department','City']]).astype(int)
print("After Encoding")
print(la_data)
print('after onehot')
print(onehot)
std=StandardScaler()
st=std.fit_transform(pf)
print(st)
