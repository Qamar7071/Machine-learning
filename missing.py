import pandas as pd
data = {
    'Name': ['Ali', 'Ahmed', 'Sara', 'Hina', 'Usman', None, 'Ayesha', 'Bilal', None, 'Zara'],

    'Age': [21, None, 22, 23, None, 24, None, 25, 26, None],

    'Salary': [50000, 60000, None, None, 80000, 75000, None, 90000, None, 85000],

    'Department': ['IT', None, 'HR', 'Finance', 'IT', 'HR', None, 'Finance', 'IT', None],

    'Experience_Years': [1, 2, None, 3, 4, None, 2, None, 5, None],

    'Performance_Score': [None, 80, 75, None, 90, 85, None, 88, None, 92]
}
pf=pd.DataFrame(data)
print(pf)
print("sum or persontage of missing values")
print(pf.isnull().sum())
drop_value=pf.dropna()
print("\nAfter Dropping Missing Rows")
print(drop_value)
pf['Name']=pf['Name'].fillna(pf['Name'].mode()[0])
pf['Age'] = pf['Age'].fillna(pf['Age'].mean())
pf['Salary']=pf['Salary'].fillna(pf['Salary'].mean())
pf['Department']=pf['Department'].fillna(pf['Department'].mode()[0])
print(pf)
pf.to_csv("Student_Marks_Dataset (1).csv")
pf.to_excel( "Student_Marks_Dataset (2).xlsx")
pf.info()