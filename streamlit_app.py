import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('./document_result/data_status.csv')

# Fitur penting
important_features = [
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Tuition_fees_up_to_date",
    "Age_at_enrollment",
    "Previous_qualification_grade", 
    "Admission_grade"
]

# App title
st.title("Eksplorasi Interaktif Fitur Mahasiswa")

st.markdown("""
Gunakan sidebar untuk memilih fitur yang ingin **difilter**, dan lihat data serta grafik berdasarkan hasil filter.  
Cocok untuk eksplorasi potensi dropout berdasarkan data historis mahasiswa.
""")

# Sidebar filter interaktif
st.sidebar.header("🔍 Pengaturan Filter")

# Pilih fitur mana yang ingin difilter
selected_features_for_filter = st.sidebar.multiselect(
    "Pilih fitur yang ingin difilter:",
    important_features,
    default=important_features[:3]  # default 3 pertama
)

# Mulai dengan semua data
filtered_data = data.copy()

# Loop fitur dan tampilkan slider hanya untuk fitur yang dipilih
for feature in selected_features_for_filter:
    if data[feature].dtype in ['int64', 'float64']:
        min_val = float(data[feature].min())
        max_val = float(data[feature].max())
        selected_range = st.sidebar.slider(
            f"{feature}", min_val, max_val, (min_val, max_val)
        )
        filtered_data = filtered_data[
            (filtered_data[feature] >= selected_range[0]) &
            (filtered_data[feature] <= selected_range[1])
        ]
    else:
        unique_vals = data[feature].unique()
        selected_vals = st.sidebar.multiselect(
            f"{feature}", options=unique_vals, default=list(unique_vals)
        )
        filtered_data = filtered_data[filtered_data[feature].isin(selected_vals)]

# Section - Data Output
tampilkan_fitur = important_features
tampilkan_fitur.extend(["Status", "Probability"])
filtered_data = filtered_data[important_features]
st.markdown("#### **📋 Data Mahasiswa (Setelah Filter)**")
st.write(f"Jumlah mahasiswa ditampilkan: **{filtered_data.shape[0]}**")
st.dataframe(filtered_data)

# Section - Grafik perbandingan Graduate vs Dropout
st.markdown("#### **🎓 Jumlah Graduate vs Dropout**")

# Asumsikan kolom target adalah 'Status'
if 'Status' in filtered_data.columns:
    status_counts = filtered_data['Status'].value_counts()

    fig_status, ax_status = plt.subplots(figsize=(8, 6))
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="Set2", ax=ax_status)
    ax_status.set_ylabel("Jumlah Mahasiswa")
    ax_status.set_xlabel("Status")
    ax_status.set_title("Jumlah Graduate vs Dropout")
    st.pyplot(fig_status)
else:
    st.warning("Kolom 'Status' tidak ditemukan di data.")

# Section - Visualisasi
st.markdown("#### **📊 Visualisasi Distribusi Fitur**")

# Pilih fitur untuk divisualisasikan
selected_feature_plot = st.selectbox(
    "Pilih fitur yang ingin divisualisasikan:",
    important_features
)

# Tampilkan histogram
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(filtered_data[selected_feature_plot], kde=True, ax=ax, color="skyblue")
ax.set_title(f"Distribusi: {selected_feature_plot}")
st.pyplot(fig)

# Optional - Summary statistik
st.markdown("#### **📈 Statistik Ringkas**")
st.write(filtered_data[important_features].describe())

# Section - Download
st.markdown("---")
csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Data sebagai CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)
