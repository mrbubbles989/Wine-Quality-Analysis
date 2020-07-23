# Import necessary libraries and modules
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px

# Load red wine data
dataset_url = pd.read_csv('https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009?select=winequality-red.csv')

#Visualizing the data
# See the number of rows and columns
print("Rows, columns: " + str(df.shape))

# See the first 5 rows
df.head()
