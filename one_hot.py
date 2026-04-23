import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Name": ["Ali","Sara","Ahmed","Hina","Bilal","Ayesha"],
    "Gender": ["Male","Female","Male","Female","Male","Female"],
    "Department": ["IT","HR","Finance","IT","HR","Finance"],
    "City": ["Lahore","Karachi","Islamabad","Lahore","Karachi","Islamabad"]
}

df = pd.DataFrame(data)

Encode=pd.get_dummies(df[['Gender','Department','City']]).astype(int)
print(df)
print(Encode)

