from sklearn.preprocessing import StandardScaler, MinMaxScaler, minmax_scale
from sklearn.model_selection import train_test_split
import  pandas as pd
data={
    'study_hrs':[1,2,3,4,5],
    'test_score':[50,60,70,80,90],
}
pf=pd.DataFrame(data)
std_scaler=StandardScaler()
std_scaled=std_scaler.fit_transform(pf)
print('std_scaled')
print(std_scaled)
max_scale=MinMaxScaler()
minmax_scaled=max_scale.fit_transform(pf)
print('minmax_scaled')
print(pd.DataFrame(minmax_scaled,columns=['study_hrs','test_score']))
X=pf[['study_hrs']]
y=pf['test_score']
X_train,X_test,Y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("train data")
print(X_train)
print("test data")
print(X_test)