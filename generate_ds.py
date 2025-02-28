import pandas as pd
import numpy as np

# Fungsi untuk menghitung skor dan menentukan tingkat
def calculate_scores_and_recommendation(answers):
    # Pertanyaan untuk setiap kategori
    depresi_questions = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    kecemasan_questions = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    stress_questions = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]

    # Hitung skor total untuk setiap kategori
    skor_depresi = sum([answers[q - 1] for q in depresi_questions])
    skor_kecemasan = sum([answers[q - 1] for q in kecemasan_questions])
    skor_stress = sum([answers[q - 1] for q in stress_questions])

    # Tentukan tingkat berdasarkan skor
    def determine_level(score, thresholds):
        if score <= thresholds[0]:
            return "Normal"
        elif score <= thresholds[1]:
            return "Ringan"
        elif score <= thresholds[2]:
            return "Sedang"
        elif score <= thresholds[3]:
            return "Parah"
        else:
            return "Sangat Parah"

    tingkat_depresi = determine_level(skor_depresi, [9, 13, 20, 27])
    tingkat_kecemasan = determine_level(skor_kecemasan, [7, 9, 14, 19])
    tingkat_stress = determine_level(skor_stress, [14, 18, 25, 33])

    # Tentukan rekomendasi berdasarkan tingkat
    if (tingkat_depresi == "Normal" and
        tingkat_kecemasan == "Normal" and
        tingkat_stress in ["Normal", "Ringan", "Sedang"]):
        rekomendasi = "Konsultasi"
    elif (tingkat_depresi in ["Ringan", "Sedang"] and
          tingkat_kecemasan in ["Ringan", "Sedang"] and
          tingkat_stress in ["Sedang", "Parah"]):
        rekomendasi = "Konseling"
    elif (tingkat_depresi in ["Parah", "Sangat Parah"] or
          tingkat_kecemasan in ["Parah", "Sangat Parah"] or
          tingkat_stress == "Sangat Parah"):
        rekomendasi = "Psikoterapi"
    else:
        rekomendasi = "Evaluasi lebih lanjut"

    return skor_depresi, skor_kecemasan, skor_stress, tingkat_depresi, tingkat_kecemasan, tingkat_stress, rekomendasi

# Generate balanced dataset
np.random.seed(42)  # For reproducibility
num_samples_per_class = 50  # Jumlah data per kelas
num_questions = 42

# Fungsi untuk membuat data untuk satu kelas
def generate_data_for_class(rekomendasi_target, num_samples):
    data = []
    while len(data) < num_samples:
        answers = np.random.randint(0, 4, size=num_questions)
        _, _, _, tingkat_depresi, tingkat_kecemasan, tingkat_stress, rekomendasi = calculate_scores_and_recommendation(answers)
        
        # Hanya tambahkan data jika sesuai dengan target rekomendasi
        if rekomendasi == rekomendasi_target:
            skor_depresi, skor_kecemasan, skor_stress, _, _, _, _ = calculate_scores_and_recommendation(answers)
            row = list(answers) + [skor_depresi, skor_kecemasan, skor_stress, tingkat_depresi, tingkat_kecemasan, tingkat_stress, rekomendasi]
            data.append(row)
    return data

# Generate data untuk setiap kelas
data_konsultasi = generate_data_for_class("Konsultasi", num_samples_per_class)
data_konseling = generate_data_for_class("Konseling", num_samples_per_class)
data_psikoterapi = generate_data_for_class("Psikoterapi", num_samples_per_class)

# Gabungkan semua data
all_data = data_konsultasi + data_konseling + data_psikoterapi

# Create DataFrame
columns = [f"Q{i+1}" for i in range(num_questions)] + ["Skor_Depresi", "Skor_Kecemasan", "Skor_Stress", "Tingkat_Depresi", "Tingkat_Kecemasan", "Tingkat_Stress", "Rekomendasi"]
df = pd.DataFrame(all_data, columns=columns)

# Shuffle data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv("balanced_kuesioner_data.csv", index=False)

print("Balanced dataset generated and saved as 'balanced_kuesioner_data.csv'")
