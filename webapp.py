import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import time  # For progress bar demonstration

def load_data():
    data = load_iris()
    return pd.DataFrame(data.data, columns=data.feature_names), data.target, data.target_names

df, target, target_names = load_data()

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
    sepal_width = st.sidebar.slider('Sepal width', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
    petal_length = st.sidebar.slider('Petal length', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
    petal_width = st.sidebar.slider('Petal width', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

model = RandomForestClassifier()
model.fit(df, target)
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Class labels and their corresponding index number')
st.write(target_names)

st.subheader('Prediction')
st.write(target_names[prediction][0])  # Get the class label

st.subheader('Prediction Probability')
st.write(prediction_proba)

st.subheader('Display Image')
st.image('car.jpg', use_column_width=True)

st.subheader('Play Audio')
st.audio("audio.mp3")

st.subheader('Play Video')
st.video("Cartoon.mp4")

st.subheader('Progress and Status')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.subheader('Data Visualization')
st.line_chart(df)

