import streamlit as st 
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder


def load_model():
    with  open("/Users/vijju/Desktop/projects/data_science/9thfeb_model.ipynb/student_lr_model.pkl",'rb') as file:
        model,scaler,le=pickle.load(file)
    return model,scaler,le

def preprocesssing_input_data(data, scaler, le):
    data['Extracurricular Activities']= le.transform([data['Extracurricular Activities']])[0]
    df = pd.DataFrame([data])
    df_transformed = scaler.transform(df)
    return df_transformed

def predict_data(data):
    model,scaler,le = load_model()
    processed_data = preprocesssing_input_data(data,scaler,le)
    prediction = model.predict(processed_data)
    return prediction

def main():
    st.title("student performnce perdiction")
    st.write("enter your data to get a prediction for your performance")
    
    hour_sutdied = st.number_input("Hours studied",min_value = 1, max_value = 10 , value = 5)
    prvious_score = st.number_input("previous score",min_value = 40, max_value = 100 , value = 70)
    extra = st.selectbox("extra curri activity" , ['Yes',"No"])
    sleeping_hour = st.number_input("sleeping hours",min_value = 4, max_value = 10 , value = 7)
    number_of_peper_solved = st.number_input("number of question paper solved",min_value = 0, max_value = 10 , value = 5)
    
    if st.button("predict-your_score"):
        user_data = {
            "Hours Studied":hour_sutdied,
            "Previous Scores":prvious_score,
            "Extracurricular Activities":extra,
            "Sleep Hours":sleeping_hour,
            "Sample Question Papers Practiced":number_of_peper_solved
        }
        prediction = predict_data(user_data)
        st.success(f"your prediciotn result is {prediction}")
    
if __name__ == "__main__":
    main()
    
# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
# from sklearn.preprocessing import StandardScaler, LabelEncoder

# # def preprocessing_input_data(data, standard, le):
# #     binary_mapping = {'yes': 1, 'no': 0}
# #     data['Extracurricular Activities'] = le.transform([data['Extra_activities']])  # Corrected transformation
# #     df = pd.DataFrame([data])
# #     df_transformed = standard.transform(df)
# #     return df_transformed
# def preprocessing_input_data(data, Standard, le):
#     data["Extracurricular Activities"] = le.fit_transform(df['Extracurricular Activities'])
#     df = pd.DataFrame([data])
#     df_transformed = standard.transform(df)
#     return df_transformed



# def load_model():
#     with open('/Users/vijju/Desktop/projects/data_science/9thfeb_model.ipynb/student_lr_model.pkl', 'rb') as file:
#         model, standard, le = pickle.load(file)
#     return model, standard, le



# def predict_data(data):
#     model, standard, le = load_model()
#     processed_data = preprocessing_input_data(data, standard, le)
#     prediction = model.predict(processed_data)
#     return prediction    

# def main():
#     st.title('Student Performance Prediction')
#     st.write("Enter your data to get a prediction for your performance")

#     Total_hours = st.number_input("Hours_studies", min_value=5, max_value=24, step=5)
#     prev_score = st.number_input("Previous score", min_value=40, max_value=100, step=1)
#     Extra_activities = st.selectbox("Extracurricular Activities", ['yes', 'no'])
#     sleeping_hours = st.number_input("Sleeping hours", min_value=0, max_value=5, step=1)
#     number_of_papers_solved = st.number_input("Number of papers solved", min_value=0, max_value=10, step=1)
    
#     if st.button("Final Prediction"):
#         user_data = {'Total_hours': Total_hours, 
#                     'prev_score': prev_score, 
#                     'Extra_activities': Extra_activities, 
#                     'sleeping_hours': sleeping_hours, 
#                     'number_of_papers_solved': number_of_papers_solved
#                     }
#         prediction = predict_data(user_data)
#         st.write("The prediction is ", prediction)

# if __name__ == '__main__':
#     main()
