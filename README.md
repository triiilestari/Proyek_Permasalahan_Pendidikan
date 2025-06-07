# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan studi mereka atau dropout. Tingginya tingkat dropout dapat berdampak negatif terhadap citra, efektivitas, dan keberlanjutan institusi pendidikan. Oleh karena itu, manajemen Jaya Jaya Institut memiliki kebutuhan strategis untuk mengidentifikasi secara dini siswa yang berpotensi dropout, agar dapat diberikan intervensi atau bimbingan yang sesuai sebelum terlambat.

Sebagai bagian dari transformasi digital berbasis data, Jaya Jaya Institut telah menyediakan dataset performa siswa yang dapat dimanfaatkan untuk membangun solusi berbasis kecerdasan buatan (AI). Mereka ingin mengembangkan sistem prediktif yang mampu mengidentifikasi secara dini potensi siswa yang akan mengalami dropout, sehingga intervensi dapat diberikan secara tepat waktu. Selain itu, mereka juga membutuhkan dashboard berbasis AI yang tidak hanya menyajikan visualisasi data, tetapi juga mampu memberikan insight untuk mendukung pengambilan keputusan oleh pihak akademik.

### Permasalahan Bisnis
Permasalahan bisnis yang akan diselesaikan melalui proyek ini adalah:

1. Mengidentifikasi Faktor-faktor Utama yang Mempengaruhi Dropout

    Menentukan faktor-faktor yang menyebabkan mahasiswa droput, seperti jumlah mata kuliah yang disetujui setiap semester, nilai setiap semester, status penerima beasiswa, umur saat pendaftaran dan lain sebagainya. Hal ini penting untuk membantu pihak kampus memahami akar masalah dan fokus pada aspek yang paling perlu diperbaik.

2. Menentukan Pola Perilaku Mahasiswa yang Cenderung Dropout

    Melihat pola atau kebiasaan mahasiswa yang sering terjadi sebelum mereka memutuskan untuk berhenti kuliah. Melalui ini kampus bisa mengenali lebih awal siapa saja mahasiswa yang berisiko dropout, sehingga bisa langsung diberikan pendampingan atau dukungan.

3. Menyediakan Alat Bantu Berupa Business Dashboard

    Membuat tampilan visual yang mudah dipahami untuk membantu pihak kampus memantau data dan kondisi mahasiswa. Dashboard ini untuk memudahkan pengambilan keputusan berbasis data secara cepat, tanpa harus menganalisis data mentah secara manual.

4. Item Rekomendasi Tindakan berdasarkan Faktor Utama Tersebut

    Memberikan saran langkah atau tindakan yang bisa diambil kampus berdasarkan faktor-faktor utama yang ditemukan. Kampus bisa langsung bertindak dengan strategi yang tepat, seperti membuat program bimbingan akademik atau dukungan psikologis, untuk mencegah dropout.

Dengan menyelesaikan permasalahan ini, kampus diharapkan dapat:

- Menurunkan tingkat mahasiswa yang dropout setiap semester.
- Mendeteksi secara dini mahasiswa yang berisiko tidak menyelesaikan studi.
- Mengambil keputusan yang lebih cepat dan tepat berdasarkan data.
- Meningkatkan kualitas layanan akademik dan pendampingan mahasiswa.


### Cakupan Proyek
Proyek ini bertujuan untuk menganalisis status rate di Jaya Jaya Maju dan memberikan solusi untuk mengurangi tingkat droput dengan cara yang lebih efektif. Cakupan proyek meliputi:
1. Data Understanding - mengalisis data mahasiswa:
    - Analisis dataset `student's_performance.csv` untuk memahami karakteristik setiap mahasiswa
    - Memproses data mahasiswa terkait status rate, termasuk faktor-faktor akademik, finansial, sosial ekonomi dan kebutuhan khusus, dan demografis
    - Menggunakan teknik analisis statistik dan machine learning untuk mengidentifikasi faktor utama yang mempengaruhi dropout
2. Data Preparation - menyiapkan data untuk pemodelan:
    - Membersihkan dan memproses data agar siap digunakan untuk analisis lebih lanjut
    - Analisis korelasi antara variabel seperti jumlah mata kuliah yang disetujui setiap semester, nilai semester, beasiswa dan fitur-fitur lainnya
    - Visualisasi tren dan pola di berbagai fitur yang mempengaruhi dropout
    - Seleksi fitur yang mempengaruhi status untuk pembelajaran model
3. Membangun Model Prediktif:
    - Membangun model prediktif untuk mengidentifikasi mahasiswa dengan risiko tinggi dropout berdasarkan pola-pola yang ditemukan dalam data
    - Menggunakan teknik seperti Support Vector Machine (SVM), K-Nearest Neighbor (KNN), Naive Bayes (NB), dan Random Forest (RF) untuk memprediksi status
    - Melakukan evaluasi pada model-model yang telah dibangun untuk menentukan model yang paling sesuai untuk prediksi status di Jaya Jaya Maju
4. Pengembangan Business Dashboard:
    - Membuat dashboard interaktif yang menampilkan metrik-metrik penting terkait status rate, seperti faktor-faktor yang mempengaruhi, dan analisis demografis
    - Dashboard ini akan memungkinkan pihak kampus untuk memantau dan mengambil keputusan berbasis data secara real-time
5. Kesimpulan dan Rekomendasi
    - Menarik kesimpulan dari hasil analisis yang telah dilakukan dari tahap data understanding hingga hasil dashboard analisis
    - Memmberikan rekomendasi praktis untuk mengurangi status dropout

### Persiapan

**Sumber data**: Dataset yang digunakan dalam proyek ini adalah [Dataset Student's Performnace Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) sesuai dengan instruksi dari submission proyek ini.

**Setup environment**: Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
**- Menjalankan notebook Proyek_Permasalahan_HR.ipynb**
1. Instalasi Dependensi:

    - Pastikan semua dependensi yang dibutuhkan sudah terpasang. Anda dapat memeriksa daftar dependensi di dalam requirements.txt.
    - Untuk menginstal dependensi, jalankan perintah berikut di terminal atau command prompt:
        ```
        pip install -r requirements.txt
        ```
2. Menjalankan Notebook:
    - Buka file Proyek_Permasalahan_Pendidikan.ipynb menggunakan Google Colab atau Jupyter Notebook.
    - Jika menggunakan Google Colab, unggah file notebook ke dalam Google Drive dan buka melalui Google Colab.
    - Jika menggunakan Jupyter Notebook, jalankan perintah berikut untuk membuka file:
        ```
        jupyter notebook Proyek_Permasalahan_HR.ipynb
        ```
3. Menjalankan Semua Sel:
    - Jalankan seluruh isi notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
    - Di Google Colab atau Jupyter Notebook, pilih "Run All" untuk mengeksekusi seluruh sel notebook secara berurutan dan melihat hasilnya.

**- Cara Mengakses Dashboard di Looker Studio**:
1. Buka tautan berikut di browser: 
   [🔗 Akses Dashboard di Looker Studio](https://lookerstudio.google.com/reporting/bc633523-d51f-4e26-a7ef-cf42077274c4)  

2. Login menggunakan akun Google Anda: 
   - Pastikan akun yang digunakan memiliki izin akses ke dashboard
   - Jika Anda tidak memiliki akses, hubungi admin dashboard untuk diberikan izin.

3. Tunggu hingga dashboard selesai dimuat:   
   - Anda akan melihat berbagai visualisasi seperti grafik dan tabel

**- Menjalankan file python prototype sistem machine learning**:
1. Buka tautan berikut dibrowser untuk akses prototype streamlit community cloud:
    [🔗 Akses Prototype di Browser](https://blank-app-vdpsvbe3gtq.streamlit.app/)
    - Ubah-ubah fitur pengaturan untuk memaksimalkan analisis
2. Jalankan ini untuk running prototype secara lokal dengan streamlit:
    - Pastikan semua dependensi yang dibutuhkan sudah terpasang. Anda dapat memeriksa daftar dependensi di dalam requirements.txt.
    Untuk menginstal dependensi, jalankan perintah berikut di terminal atau command prompt:
        ```
        pip install -r requirements.txt
        ```
    - Jalankan streamlit dengan cara ini
        ```
        streamlit run streamlit_app.py
        ```
    - Fitur pada prototype meliputi 
        - Filter fitur penting mahasiswa
        - Grafik distribusi fitur
        - Perbandingan Graduate vs Dropout
        - Ringkasan Statistik
        - Download data filtered

## Business Dashboard
Dashboard interaktif dapat menyajikan hasil analisis dan prediksi status secara real-time, memberi pihak kampus wawasan cepat dan terukur. Elemen utama yang dapat dilihat dari dashboard meliputi:

1. Tren Status:
    - Visualisasi tren status mahasiswa berdasarkan berbagai faktor seperti Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Tuition_fees_up_to_date, Curricular_units_1nd_sem_approved, Curricular_units_1nd_sem_grade
    - Membantu pihak kampus mengidentifikasi pola yang berulang dan kelompok yang rentan dropout
2. Feature Importance:
    - Visualisasi kontribusi fitur utama seperti Curricular_units_2nd_sem_approved dan Curricular_units_2nd_sem_grade terhadap risiko dropout
    - Visualisasi infomasi lain terkait sebaran Tuition_fees_up_to_date
3. Informasi Prediksi Risiko:
    - Menampilkan tabel daftar prediksi mahasiswa dengan probabilitas dropout diatas 70%

**Tutorial Mengakses Dashboard**

Lakukan sesuai arahan pada poin Persiapan - Setup Environment pada bagian **Cara Mengakses Dashboard di Looker Studio** pada dokumen ini

## Conclusion

#### **1. Faktor-Faktor Penyebab Attrition**

Berdasarkan hasil analisis data dan model prediktif, berikut adalah faktor-faktor utama yang memengaruhi status kelulusan atau dropout mahasiswa:
1. **Curricular_units_2nd_sem_approved**
   - Jumlah mata kuliah yang disetujui pada semester 2 sangat berpengaruh terhadap keberhasilan mahasiswa.
2. **Curricular_units_2nd_sem_grade**
    - Nilai akademik di semester kedua mencerminkan pencapaian belajar dan konsistensi mahasiswa.
3. **Tuition_fees_up_to_date_1**
    - Status pembayaran uang kuliah menjadi indikator penting yang berkorelasi dengan risiko dropout.
4. **Curricular_units_2nd_sem_enrolled**
    - Jumlah mata kuliah yang diambil di semester 2 menunjukkan beban studi mahasiswa.
5. **Curricular_units_1st_sem_approved**
    - Capaian di semester pertama juga memberi dampak, meski lebih kecil dibanding semester kedua.

#### **2. Model Prediktif Terbaik**
Model terbaik yang digunakan dalam proyek ini adalah **Support Vector Classifier (SVC)**, dengan metrik performa weighted average sebagai berikut:
- **Accuracy**: 0.91
- **Precision**: 0.89
- **Recall**: 0.93
- **F1-Score**: 0.91

Model ini menunjukkan performa terbaik dibandingkan model lainnya seperti Random Forest, K-Nearest Neighbors (KNN), dan Naive Bayes.

#### **3. Jawaban terhadap Pertanyaan Bisnis**
1. **Apa faktor utama yang memengaruhi Status Mahasiswa?**

    Faktor utama adalah performa akademik pada semester kedua dan status pembayaran uang kuliah, khususnya:
    - Curricular_units_2nd_sem_approved
    - Curricular_units_2nd_sem_grade
    - Tuition_fees_up_to_date
  
2. **Bagaimana tingkat performa awal memengaruhi Status Mahasiswa?**
    -  Performa pada semester pertama (Curricular_units_1st_sem_grade, Curricular_units_1st_sem_approved) memiliki pengaruh sedang, dan nilai saat masuk (Admission_grade) berpengaruh kecil.
  
3. **Apa pola perilaku Mahasiswa dengan risiko keluar tinggi?**
    - Mahasiswa dengan sedikit mata kuliah yang disetujui di semester 2, nilai rendah, serta tunggakan pembayaran cenderung memiliki risiko dropout tinggi.
  
4. **Apakah kita memiliki alat bantu untuk memantau Status Mahasiswa?**
    - Ya, model prediktif yang dibangun dapat dijadikan dasar untuk dashboard monitoring risiko dropout, dengan kemungkinan integrasi ke sistem akademik.

#### **4. Karakteristik Umum Mahasiswa yang Melakukan Droput**
Berdasarkan analisis data, berikut adalah karakteristik umum mahasiswa yang melakukan dropout:

1. **Akademik:**
    - Menunjukkan performa buruk di semester 2 (nilai dan jumlah mata kuliah disetujui rendah).
    - Jumlah evaluasi lebih sedikit dibanding mahasiswa yang graduate.

2. **Faktor Finansial:**
    - Sering menunggak pembayaran SPP (tuition not up-to-date).
    - Tidak konsisten dalam proses akademik dari semester 1 ke 2.

3. **Sosial Ekonomi & Kebutuhan Khusus:**
    - Sebagian besar mahasiswa dropout tidak memiliki kebutuhan pendidikan khusus.
    - Status penerima beasiswa tidak menunjukkan pengaruh signifikan terhadap risiko dropout, namun tetap penting sebagai bentuk dukungan terhadap mahasiswa berprestasi.

4. **Demografis:**
    - Umur saat pendaftaran tidak terlalu berpengaruh, namun mahasiswa yang lebih muda cenderung lebih stabil.


### Rekomendasi Action Items untuk Institusi
**1. Intervensi Dini Berdasarkan Semester 2:**

- Fokus pada monitoring nilai dan capaian mata kuliah di semester kedua.
- Sistem alert otomatis untuk mahasiswa dengan pencapaian < 50% pada semester ini.
  
**2. Pendekatan Finansial:**
  
- Berikan opsi keringanan atau pengingat pembayaran kepada mahasiswa yang menunggak biaya kuliah.
  
**3. Dashboard Monitoring Dropout Risk:**
  
- Kembangkan dashboard berbasis model prediktif untuk digunakan oleh staf akademik dan bimbingan konseling.

  
**4. Kelas Remedial atau Pendampingan Akademik:**
  
- Khususnya ditujukan pada mahasiswa yang performanya rendah sejak semester pertama.

#### Lainnya:
- Berdasarkan prediksi dengan model SVC, Mahasiswa dengan status Enrolled saat ini yang berjumlah 794 menunjukkan hasil prediksi 602 Graduate dan 192 Dropout
- Untuk menghindari kejadian dropout secara masif, bisa dilakukan beberapa Rekomendasi Action Items sebagai strategi proaktif berbasis data serta penguatan sistem dukungan akademik dan finansial.
