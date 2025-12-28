import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠 House Price prediction using ML')
st.image('https://i.pinimg.com/originals/46/cb/a9/46cba9f93a3d437db6d42f4bcd1a5f5f.gif')
df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('🏠 Select House Feature')
st.sidebar.image('https://i.pinimg.com/originals/46/cb/a9/46cba9f93a3d437db6d42f4bcd1a5f5f.gif')
all_value = []
for i in X:
  min_value = int(X[i].min())
  max_value = int(X[i].max())
  ans = st.sidebar.slider(f'Select {i} Value',min_value,max_value)
  all_value.append(ans)

# st.write(all_value)
  

