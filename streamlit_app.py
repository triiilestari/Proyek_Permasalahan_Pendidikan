import pickle
from typing import List
import copy

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


def load_model(path: str):
    """Load a trained scikit‑learn model from a pickle / joblib file."""
    with open(path, "rb") as f:
        return pickle.load(f)
    
marital_status_map = {1: 'Single',2: 'Married',3: 'Widowed',4: 'Divorced',5: 'Legally Separated',6: 'In a Common-Law Marriage'}
attendance_map = {1: 'Daytime', 0: 'Evening'}
gender_map = {0: 'Male', 1: 'Female'}
application_mode_map = {1 : "1st phase - general contingent",2 : "Ordinance No. 612/93",5 : "1st phase - special contingent (Azores Island)",7 : "Holders of other higher courses",10 : "Ordinance No. 854-B/99",15 : "International student (bachelor)",16 : "1st phase - special contingent (Madeira Island)", 17 : "2nd phase - general contingent",18 : "3rd phase - general contingent",26 : "Ordinance No. 533-A/99, item b2) (Different Plan)",27 : "Ordinance No. 533-A/99, item b3 (Other Institution)",39 : "Over 23 years old",42 : "Transfer",43 : "Change of course",44 : "Technological specialization diploma holders",51 : "Change of institution/course",53 : "Short cycle diploma holders", 57 : "Change of institution/course (International)"}
course_map = {33: 'Biofuel Production Technologies',171: 'Animation and Multimedia Design',8014: 'Social Service (evening attendance)',9003: 'Agronomy',9070: 'Communication Design',9085: 'Veterinary Nursing',9119: 'Informatics Engineering',9130: 'Equinculture',9147: 'Management',9238: 'Social Service',9254: 'Tourism',9500: 'Nursing',9556: 'Oral Hygiene',9670: 'Advertising and Marketing Management',9773: 'Journalism and Communication',9853: 'Basic Education',9991: 'Management (evening attendance)'}
pre_qual_map = {1 : "Secondary education",2 : "Higher education - bachelor's degree",3 : "Higher education - degree",4 : "Higher education - master's",5 : "Higher education - doctorate",6 : "Frequency of higher education",9 : "12th year of schooling - not completed",10 : "11th year of schooling - not completed",12 : "Other-11th year of schooling",14 : "10th year of schooling",15 : "10th year of schooling - not completed",19 : "Basic education 3rd cycle (9th/10th/11th year) or equiv.",38 : "Basic education 2nd cycle (6th/7th/8th year) or equiv.",39 : "Technological specialization course",40 : "Higher education - degree (1st cycle)",42 : "Professional higher technical course",43 : "Higher education - master (2nd cycle)"}
mother_qual = {1 : "Secondary Education - 12th Year of Schooling or Eq.",2 : "Higher Education - Bachelor's Degree",3 : "Higher Education - Degree",4 : "Higher Education - Master's",5 : "Higher Education - Doctorate",6 : "Frequency of Higher Education",9 : "12th Year of Schooling - Not Completed",10 : "11th Year of Schooling - Not Completed",11 : "7th Year (Old)",12 : "Other - 11th Year of Schooling",14 : "10th Year of Schooling",18 : "General commerce course",19 : "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",22 : "Technical-professional course",26 : "7th year of schooling",27 : "2nd cycle of the general high school course",29 : "9th Year of Schooling - Not Completed",30 : "8th year of schooling",34 : "Unknown",35 : "Can't read or write",36 : "Can read without having a 4th year of schooling",37 : "Basic education 1st cycle (4th/5th year) or equiv.",38 : "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",39 : "Technological specialization course",40 : "Higher education - degree (1st cycle)",41 : "Specialized higher studies course",42 : "Professional higher technical course",43 : "Higher Education - Master (2nd cycle)",44 : "Higher Education - Doctorate (3rd cycle)"}
father_qual = {1 : "Secondary Education - 12th Year of Schooling or Eq.",2 : "Higher Education - Bachelor's Degree",3 : "Higher Education - Degree",4 : "Higher Education - Master's",5 : "Higher Education - Doctorate",6 : "Frequency of Higher Education",9 : "12th Year of Schooling - Not Completed",10 : "11th Year of Schooling - Not Completed",11 : "7th Year (Old)",12 : "Other - 11th Year of Schooling",13 : "2nd year complementary high school course",14 : "10th Year of Schooling",18 : "General commerce course",19 : "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",20 : "Complementary High School Course",22 : "Technical-professional course",25 : "Complementary High School Course - not concluded",26 : "7th year of schooling",27 : "2nd cycle of the general high school course",29 : "9th Year of Schooling - Not Completed",30 : "8th year of schooling",31 : "General Course of Administration and Commerce",33 : "Supplementary Accounting and Administration",34 : "Unknown",35 : "Can't read or write",36 : "Can read without having a 4th year of schooling",37 : "Basic education 1st cycle (4th/5th year) or equiv.",38 : "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",39 : "Technological specialization course",40 : "Higher education - degree (1st cycle)",41 : "Specialized higher studies course",42 : "Professional higher technical course",43 : "Higher Education - Master (2nd cycle)",44 : "Higher Education - Doctorate (3rd cycle)"}
nationality_map = {1: 'Portuguese',2: 'German',6: 'Spanish',11: 'Italian',13: 'Dutch',14: 'English',17: 'Lithuanian',21: 'Angolan',22: 'Cape Verdean',24: 'Guinean',25: 'Mozambican',26: 'Santomean',32: 'Turkish',41: 'Brazilian',62: 'Romanian',100: 'Moldova (Republic of)',101: 'Mexican',103: 'Ukrainian',105: 'Russian',108: 'Cuban',109: 'Colombian'}
maps = {1: "Yes", 0 : "No"}


# Membuat semua reverse
reverse_marital_status_map = {v: k for k, v in marital_status_map.items()}
reverse_attendance_map = {v: k for k, v in attendance_map.items()}
reverse_gender_map = {v: k for k, v in gender_map.items()}
reverse_application_mode_map = {v: k for k, v in application_mode_map.items()}
reverse_course_map = {v: k for k, v in course_map.items()}
reverse_pre_qual_map = {v: k for k, v in pre_qual_map.items()}
reverse_mother_qual = {v: k for k, v in mother_qual.items()}
reverse_father_qual = {v: k for k, v in father_qual.items()}
reverse_nationality_map = {v: k for k, v in nationality_map.items()}
reverse_maps = {v: k for k, v in maps.items()}

other = {"Marital_status" : marital_status_map, "Daytime_evening_attendance" : attendance_map, "Gender" : gender_map, 
         "Application_mode": application_mode_map, "Course" :course_map, "Previous_qualification" : pre_qual_map, "Mothers_qualification" :mother_qual , 
         "Fathers_qualification" : father_qual, "Nacionality" : nationality_map}

reverse_other = {"Marital_status" : reverse_marital_status_map, "Daytime_evening_attendance" : reverse_attendance_map, "Gender" : reverse_gender_map, 
         "Application_mode": reverse_application_mode_map, "Course" :course_map, "Previous_qualification" : reverse_pre_qual_map, "Mothers_qualification" :mother_qual , 
         "Fathers_qualification" : reverse_father_qual, "Nacionality" : reverse_nationality_map}

column_yes_no = ["Debtor", 'Displaced', 'Tuition_fees_up_to_date', "Scholarship_holder", "International", "Educational_special_needs"]
mean = {
    "Application_order": 1.727848,
    "Previous_qualification_grade": 132.613314,
    "Admission_grade": 126.978119,
    "Age_at_enrollment": 23.265145,
    "Curricular_units_1st_sem_credited": 0.709991,
    "Curricular_units_1st_sem_enrolled": 6.270570,
    "Curricular_units_1st_sem_evaluations": 8.299051,
    "Curricular_units_1st_sem_approved": 4.706600,
    "Curricular_units_1st_sem_grade": 10.640822,
    "Curricular_units_1st_sem_without_evaluations": 0.137658,
    "Curricular_units_2nd_sem_credited": 0.541817,
    "Curricular_units_2nd_sem_enrolled": 6.232143,
    "Curricular_units_2nd_sem_evaluations": 8.063291,
    "Curricular_units_2nd_sem_approved": 4.435805,
    "Curricular_units_2nd_sem_grade": 10.230206,
    "Curricular_units_2nd_sem_without_evaluations": 0.150316,
    "Unemployment_rate": 11.566139,
    "Inflation_rate": 1.228029,
    "GDP": 0.001969
    }

def get_user_input(feature_names: List[str]):
    """Render sidebar widgets for each feature and return values as DataFrame."""
    inputs = {}
    visual = {}
    st.sidebar.header("📝 Manual Feature Input")
    for feat in feature_names:
        if feat.lower().startswith(("debtor", 'displaced', 'tuition_fees_up_to_date', "scholarship_holder", "international", "educational_special_needs")):
            inputs[feat] = st.sidebar.selectbox(f"{feat}", ["No", "Yes"], index=0)
            visual[feat] = inputs[feat]
            key = next((k for k, v in maps.items() if v == inputs[feat]), None)
            inputs[feat] = key
        elif feat in other.keys():
            inputs[feat] = st.sidebar.selectbox(f"{feat}", other[feat].values(), index=0)
            visual[feat] = inputs[feat]
            key = next((k for k, v in other[feat].items() if v == inputs[feat]), None)
            inputs[feat] = key
        else:
            inputs[feat] = st.sidebar.number_input(feat, value=mean[feat])
            visual[feat] = inputs[feat]

    # convert to single‑row DataFrame matching training columns
    return pd.DataFrame([inputs]), pd.DataFrame([visual])


def show_feature_importance(model, feature_names):
    if hasattr(model, "feature_importances_"):
        fi = pd.Series(model.feature_importances_, index=feature_names).sort_values(ascending=False)
        st.subheader("🔍 Feature Importance")
        fi_df = fi.reset_index().rename(columns={"index": "Feature", 0: "Importance"})
        chart = alt.Chart(fi_df.head(20)).mark_bar().encode(
            x=alt.X("Importance", title="Importance", scale=alt.Scale(type="linear")),
            y=alt.Y("Feature", sort="-x", title="Feature")
        )
        fi_df.to_csv("importance_new.csv", index=False)
        st.altair_chart(chart, use_container_width=True)
        st.dataframe(fi_df)
    else:
        st.info("Model does not expose `feature_importances_` attribute.")


st.set_page_config(page_title="Student Performance Predictor", layout="wide")
st.title("🎓 Student Status Prediction Prototype")
with st.expander("ℹ️ About this App & How to Use"):
    st.markdown("""
    Welcome to the **Student Status Prediction App**!  
    This interactive tool demonstrates a complete **machine learning workflow** to predict whether a student is likely to **dropout** or **graduate** their studies.

    #### What Can You Do Here?

    - **Upload your own dataset (.CSV)**  
    Upload a file containing student data with the same features used during model training — and get predictions in batch.

    - **Manually adjust input features**  
    Use the sidebar to tweak individual student attributes and receive **instant predictions** in real-time.


    #### How to Use

    1. Navigate to the sidebar.
    2. Choose between **Manual Input** or **Upload CSV**.
    3. Instantly see the prediction result — whether the student is predicted to **Graduate** or **Dropout**.
    """, unsafe_allow_html=True)



# Load model
MODEL_PATH = "RF_model.pkl"  # update path as needed

try:
    model = load_model(MODEL_PATH)
except FileNotFoundError:
    st.error(
        "Model file not found! Please place a pickled RandomForest model at `model_rf.pkl` "
        "or change the `MODEL_PATH` variable."
    )
    st.stop()

# Determine feature columns 
if hasattr(model, "feature_names_in_"):
    FEATURE_COLS = list(model.feature_names_in_)
else:
    # fallback: ask user
    FEATURE_COLS = st.sidebar.text_input(
        "Comma‑separated list of feature columns (model doesn't store names)",
        value="Curricular_units_2nd_sem_approved,Tuition_fees_up_to_date,Curricular_units_1st_sem_approved,Curricular_units_2nd_sem_grade,Curricular_units_2nd_sem_enrolled,Curricular_units_1st_sem_enrolled,Age_at_enrollment,Curricular_units_1st_sem_grade,Curricular_units_2nd_sem_evaluations,Scholarship_holder,Application_mode,Debtor,Admission_grade,Gender,Previous_qualification_grade,Curricular_units_2nd_sem_without_evaluations,Marital_status,Displaced"
    ).split(",")
    FEATURE_COLS = [c.strip() for c in FEATURE_COLS if c.strip()]

with st.expander("📊 Show feature importance"):
    show_feature_importance(model, FEATURE_COLS)

# --- Sidebar input mode 
input_mode = st.sidebar.radio(
    "Choose input method:", ["Upload CSV", "Manual input"], index=0
)
if input_mode == "Manual input":
    df_in, df_visual = get_user_input(FEATURE_COLS)
    st.write("### ✍️ Input data", df_visual.T)
elif input_mode == "Upload CSV":
    uploaded = st.sidebar.file_uploader("Upload CSV with feature columns", type=["csv"])
    if uploaded:
        df_visual = pd.read_csv(uploaded)
        df_in = copy.deepcopy(df_visual)
        st.write("### 📄 Uploaded data preview", df_visual.head())
        for key in df_in.columns:
            if key in reverse_other:
                print(key)
                print(reverse_other[key])
                df_in[key] = df_in[key].replace(reverse_other[key])
            elif key in column_yes_no:
                df_in[key] = df_in[key].replace(reverse_maps)

    else:
        st.info("Please upload a CSV file.")
        st.stop()
    
print(df_in)

# {0: 'Dropout', 1 : 'Enrolled', 2: 'Graduate'}
# df.loc[:, 'Status'] = df['Status'].replace({2: 1})
classes = list(model.classes_)
classes = ["Dropout", "Graduate"]
if st.button("🚀 Predict", use_container_width = True):
    if set(FEATURE_COLS).issubset(df_in.columns):
        predicted_proba = model.predict_proba(df_in[FEATURE_COLS])
        prediction = []
        probabilities = []
        for i, proba in enumerate(predicted_proba):
            index = np.argmax(proba)
            x_label = classes[index]
            prediction.append(x_label)
            probabilities.append(round(proba[index], 2))
        df_out = df_visual.copy()
        df_out["Predicted_Label"] = prediction
        df_out["Probability"] = probabilities
        st.write("### 🎯 Prediction results", df_out.T)
        csv = df_out.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data sebagai CSV",
            data=csv,
            file_name='prediction_result.csv',
            mime='text/csv'
        )
    else:
        missing = set(FEATURE_COLS) - set(df_in.columns)
        st.error(f"Input missing columns: {', '.join(missing)}")
