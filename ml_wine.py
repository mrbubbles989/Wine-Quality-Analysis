# Import necessary libraries and modules
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px

# Load red wine data
df = pd.read_csv("C:/Python/Learning/winequality-red.csv")

#Visualizing the data
# See the number of rows and columns
print("Rows, columns: " + str(df.shape))

# See the first 5 rows
df.head()

# Missing Values 
print(df.isna().sum()))

# Making a histogram of 'quality' variable
fig= = px.histogram(df,x='quality')
fig.show()

# Making a diagram showing weights that would affect the quality of the wine
corr = df.corr()
matplotlib.pyplot.subplots(figsize=15,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
            annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

# Create Classification version of target variable
df['goodquality'] = [1 if x >= 7 else 0 for x in df['quality']]

# Seperate feature variables and targe variable
X = df.drop(['quality', 'goodquality'], axis = 1)
y = df['goodquality']

# See proportion of good vs bad wines 
df['goodquality'].value_counts()

# Normalize feature variables 
from sklearm.preprocessing import StandardScaler
X_features = X
X = StandardScaler().fit_transform(X)

# Splitting the data

