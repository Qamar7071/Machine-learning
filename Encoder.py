import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    "Name": ["Ali","Sara","Ahmed","Hina","Bilal","Ayesha"],
    "Gender": ["Male","Female","Male","Female","Male","Female"],
    "Department": ["IT","HR","Finance","IT","HR","Finance"],
    "City": ["Lahore","Karachi","Islamabad","Lahore","Karachi","Islamabad"]
}
df = pd.DataFrame(data)
lab_data=df.copy()
lab=LabelEncoder()
lab_data["Name Encoder"]=lab.fit_transform(lab_data["Name"])
lab_data["Gender Encoder"]=lab.fit_transform(lab_data["Gender"])
lab_data["Department Encoder"]=lab.fit_transform(lab_data["Department"])
lab_data["City Encoder"]=lab.fit_transform(lab_data["City"])
print(lab_data)


