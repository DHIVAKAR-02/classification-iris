import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

def iris_flower_prediction_app():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app
        
def iris():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris
        if iris_flower_prediction_app: return iris
        
def iris_flower():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris_flower
        if iris_flower_prediction_app: return iris_flower
        
def iris_flower_prediction():
        """iris_flower_prediction_app.st_ui().value"""
        global iris_flower_prediction
        if iris_flower_prediction_app: return iris_flower_prediction
        
def iris_flower_prediction_app_randomforestclassifier():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_randomforestclassifier
        if iris_flower_prediction_app: return iris_flower_prediction_app_randomforestclassifier
        
def iris_flower_prediction_app_ml():
        """iris_flower_prediction_app.st_ui().value"""
        global iris_flower_prediction_app_ml
        if iris_flower_prediction_app: return iris_flower_prediction_app_ml
        
        
def iris_flower_prediction_app_features():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_features
        

def iris_flower_prediction_app_iris():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_iris
        
def iris_flower_prediction_app_url():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_url        

        
def iris_flower_prediction_app_using_RandomForestClassifier():
        """iris_flower_prediction_app.iris_flower_prediction_app().value"""
        global iris_flower_prediction_app_using_RandomForestClassifier
        if iris_flower_prediction_app: return iris_flower_prediction_app_using_RandomForestClassifier

def st_ui():
    '''
    Streamlit UI
    '''
    st.set_page_config(
        page_title="Iris flower prediction dataset",
        page_icon="🍲",
        layout="wide",
        initial_sidebar_state="expanded"
    ) 
def ui():
    '''
    UI
    '''
    st.set_page_config(
        page_title="Iris flower prediction dataset",
        page_icon="🍲",
        layout="wide",
        initial_sidebar_state="expanded"
    )         

 
def iris_flower_prediction_app_machine_learning():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_machine_learning       
 
def iris_flower_prediction_app_nandhakumar():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_nandhakumar

def iris_flower_prediction_app_nandhakumar_s():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_nandhakumar_s
        
def iris_flower_prediction_app_midnight_hacker():
        """iris_flower_prediction_app.add_bg_from_url().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app_midnight_hacker

def add_bg_from_url():
    st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-photo/gray-calathea-lutea-leaf-patterned-background_53876-149681.jpg?w=740");
             background-attachment: fixed;
             background-size: cover}}
             </style>""",unsafe_allow_html=True)
add_bg_from_url()




st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")
st.info("Developed by NANDHAKUMAR S, SUJITH V, MOHAMED FARHUN M, DHIVAKAR S [Team MIDNIGHT HACKERS]", icon="©")
st.sidebar.header('User Input Parameters')
st.sidebar.image("iris1.jpg")
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
