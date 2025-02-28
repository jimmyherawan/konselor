import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and label encoder
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

# Title of the app
st.title("Sistem Rekomendasi Pendekatan Psikologi")

# Instructions
st.write("""
Silakan isi jawaban Anda untuk setiap pertanyaan berikut.
Gunakan slider untuk memilih nilai antara 0 (tidak pernah) hingga 3 (selalu).
""")

# List of questions
questions = [
    "Q1: Menjadi marah karena hal-hal kecil/sepele",
    "Q2: Mulut terasa kering",
    "Q3: Tidak dapat melihat hal yang positif dari suatu kejadian",
    "Q4: Merasakan gangguan dalam bernapas (napas cepat, sulit bernapas)",
    "Q5: Merasa sepertinya tidak kuat lagi untuk melakukan suatu kegiatan",
    "Q6: Cenderung bereaksi berlebihan pada situasi",
    "Q7: Kelemahan pada anggota tubuh",
    "Q8: Kesulitan untuk relaksasi/bersantai",
    "Q9: Cemas yang berlebihan dalam suatu situasi namun bisa lega jika hal/situasi itu berakhir",
    "Q10: Pesimis",
    "Q11: Mudah merasa kesal",
    "Q12: Merasa banyak menghabiskan energi karena cemas",
    "Q13: Merasa sedih dan depresi",
    "Q14: Tidak sabaran",
    "Q15: Kelelahan",
    "Q16: Kehilangan minat pada banyak hal (misal: makan, ambulasi, sosialisasi)",
    "Q17: Merasa diri tidak layak",
    "Q18: Mudah tersinggung",
    "Q19: Berkeringat (misal: tangan berkeringat) tanpa stimulasi oleh cuaca maupun latihan fisik",
    "Q20: Ketakutan tanpa alasan yang jelas",
    "Q21: Merasa hidup tidak berharga",
    "Q22: Sulit untuk beristirahat",
    "Q23: Kesulitan dalam menelan",
    "Q24: Tidak dapat menikmati hal-hal yang saya lakukan",
    "Q25: Perubahan kegiatan jantung dan denyut nadi tanpa stimulasi oleh latihan fisik",
    "Q26: Merasa hilang harapan dan putus asa",
    "Q27: Mudah marah",
    "Q28: Mudah panik",
    "Q29: Kesulitan untuk tenang setelah sesuatu yang mengganggu",
    "Q30: Takut diri terhambat oleh tugas-tugas yang tidak biasa dilakukan",
    "Q31: Sulit untuk antusias pada banyak hal",
    "Q32: Sulit mentoleransi gangguan-gangguan terhadap hal yang sedang dilakukan",
    "Q33: Berada pada keadaan tegang",
    "Q34: Merasa tidak berharga",
    "Q35: Tidak dapat memaklumi hal apapun yang menghalangi anda untuk menyelesaikan hal yang sedang Anda lakukan",
    "Q36: Ketakutan",
    "Q37: Tidak ada harapan untuk masa depan",
    "Q38: Merasa hidup tidak berarti",
    "Q39: Mudah gelisah",
    "Q40: Khawatir dengan situasi saat diri Anda mungkin menjadi panik dan mempermalukan diri sendiri",
    "Q41: Gemetar",
    "Q42: Sulit untuk meningkatkan inisiatif dalam melakukan sesuatu"
]

# Create a form to collect user input
answers = []
for i, question in enumerate(questions):
    answer = st.slider(question, 0, 3, 0)
    answers.append(answer)

# Predict button
if st.button("Prediksi Rekomendasi"):
    # Convert input to DataFrame
    input_data = pd.DataFrame([answers])

    # Predict using the model
    prediction = model.predict(input_data)[0]
    result = label_encoder.inverse_transform([prediction])[0]

    # Display the result
    st.success(f"Rekomendasi Pendekatan: **{result}**")
