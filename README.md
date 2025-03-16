# Student_study_app
🎓 Student Performance Prediction App
📋 Project Overview
This application predicts student performance based on various input factors such as study hours, previous scores, extracurricular activities, sleeping hours, and the number of question papers solved. The goal is to help students and educators gain insights into performance outcomes and make data-driven decisions to improve academic success.

The application is built using Streamlit for the user interface, a Machine Learning model (Logistic Regression) for prediction, and MongoDB Atlas for storing user input and predictions securely in the cloud.

🚀 Key Features
Interactive Web Interface using Streamlit to collect user input and display predictions.
Machine Learning Model (Logistic Regression) trained and stored as a serialized .pkl file.
Data Preprocessing with Scikit-learn's StandardScaler and LabelEncoder.
Cloud Database Integration with MongoDB Atlas for real-time data storage and retrieval.
Secure Credential Handling using URL-encoded credentials to connect to MongoDB.
Automated Predictions saved along with user inputs for future analysis.
🧰 Technologies Used
Category	Tools & Technologies
Programming Language	Python
Frontend	Streamlit
Machine Learning	Scikit-learn (Logistic Regression), Pickle
Database	MongoDB Atlas (Cloud-hosted MongoDB)
Libraries	Pandas, NumPy, StandardScaler, LabelEncoder
Model Serialization	Pickle
Cloud & Connectivity	PyMongo for MongoDB Connection
💻 How It Works
1. User Input via Streamlit App
Users enter key parameters:
Hours Studied
Previous Scores
Extracurricular Activities (Yes/No)
Sleep Hours
Number of Sample Question Papers Practiced
2. Preprocessing & Model Prediction
Inputs are transformed using pre-trained StandardScaler and LabelEncoder.
Processed data is passed to the Logistic Regression model to predict performance.
3. Display and Save Predictions
The predicted result is displayed on the Streamlit app.
User input and prediction are stored in MongoDB Atlas for future use and analysis.
🏗️ File Structure
bash
Copy
Edit
├── app.py                    # Main Streamlit application file
├── student_lr_model.pkl      # Serialized ML model with Scaler and Encoder
└── README.md                 # Project documentation
🔑 MongoDB Connectivity
Secure Connection using PyMongo and URL-encoded credentials:
python
Copy
Edit
username = urllib.parse.quote_plus("your_username")
password = urllib.parse.quote_plus("your_password")
uri = f"mongodb+srv://{username}:{password}@cluster0.aolvk.mongodb.net/admin?retryWrites=true&w=majority"
Data is stored in the "student" database under the "student_pred" collection.
Each prediction result is inserted along with input data for tracking and improvement.
🏁 How to Run the App
⚙️ Prerequisites:
Python 3.x installed.
Required libraries installed:
bash
Copy
Edit
pip install streamlit pandas numpy scikit-learn pymongo
▶️ Run the App:
bash
Copy
Edit
streamlit run app.py
📊 Sample Input & Output
Input Parameter	Example Value
Hours Studied	5
Previous Scores	70
Extracurricular Activities	Yes
Sleep Hours	7
Sample Question Papers Practiced	5
Output Example:

csharp
Copy
Edit
Your prediction result is: 85
📦 Future Enhancements
Add visualizations and analytics dashboard for educators.
Integrate model retraining pipeline based on new data collected.
Improve user authentication and data security.
Deploy application on cloud (AWS EC2, Heroku, or Streamlit Cloud).
