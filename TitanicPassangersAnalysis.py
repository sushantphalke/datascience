import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.model_selection import train_test_split
url = "https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic3.csv"
df = pd.read_csv(url)
df.head()
# Preprocessing the Data
# Display Some basic Information of the Dataset
# Describe the Datatset
df.describe()
# Display column names
df.columns
# Display Data type of each column
df.dtypes
# Find Number of missing values
column_names = df.columns
for column in column_names:
    print(column + " - " + str(df[column].isnull().sum()))
# Insights into the Data
#  ◾ The targeet variable is - "Survived".
#  ◾ Many columns dont contribute to the target variable like :
#  1. 'Ticket'
#  2. 'Boat'
#  3. 'body'
#  4. 'home.dest'
# These can be dropped from the datset.
# Also, the column 'Cabin' has many null values and thus cannot contribute to the output. This
# can also be dropped.
# Some columns do NOT have a null value, like:
# 1. 'PClass'
# 2. 'Sex'
# 3. 'SibSp'
# 4. 'Parch'
# 5. 'Fare'
#  ◾ There are a few missing values in the columns 'Age' and 'Embarked'. These can be imputed
# using different techniques.

#  ◾ Also we can create a new variable for 'total family size' from the the column 'SibSp' and
# 'Parch'.
# Removing Unecessary Columns
df = df.drop(columns=['ticket', 'cabin', 'boat', 'body', 'home.dest'])
df.head()
# Handling Null Values
df.isnull().sum()
# Input 'Embarked' with the majority class
df['embarked'].unique()
df['embarked'] = df['embarked'].fillna('S')
df.isnull().sum()
f_NaN_index = df['fare'][df['fare'].isnull()].index
print(f_NaN_index)
df['fare'].iloc[f_NaN_index] = df['fare'].median()
df.isnull().sum()
# Filling in Missing values for 'Age'
corr_matrix = df[['pclass', 'age', 'sibsp', 'parch', 'fare']].corr()
plt.figure(figsize=(7, 6))
sns.heatmap(data=corr_matrix, cmap='BrBG', annot=True, linewidths=0.2)
# From above, we can see that age has a negative relation with 'parch', 'sibsp', and 'pclass'. Therefore,
# we fill 'age' with median age of similar rows from 'pclass', 'sibsp' and 'parch'. In case there are no
# similar rows, we fill the median age of the entire dataset.
NaN_indexes = df['age'][df['age'].isnull()].index
print(NaN_indexes)
for i in NaN_indexes:
    pred_age = df['age'][((df.sibsp == df.iloc[i]["sibsp"])
                          & (df.parch == df.iloc[i]["parch"]))]
    if not np.all(pred_age):
        df['age'].iloc[i] = pred_age
    else:
        df['age'].iloc[i] = df['age'].median()
df.isnull().sum()
df.dtypes
# First, map 'sex' and 'embarked' to numerical values
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2})
df.dtypes
df.head()
df['title'] = df.name.str.extract(' ([A-Za-z]+)\.', expand=False)
df = df.drop(columns='name')
df.head()
