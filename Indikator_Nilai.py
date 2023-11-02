# # Meminta pengguna untuk memasukkan nilai
nilai = float(input("Masukkan nilai Anda: "))

# Mengevaluasi nilai
if nilai >= 90:
    grade = 'A'
    keterangan = 'Sangat Bagus'
elif nilai >= 80:
    grade = 'B'
    keterangan = 'Baik'
elif nilai >= 70:
    grade = 'C'
    keterangan = 'Cukup'
elif nilai >= 60:
    grade = 'D'
    keterangan = 'Kurang'
else:
    grade = 'E'
    keterangan = 'Sangat Kurang'

# Menampilkan hasil penilaian
print(f"Nilai Anda adalah {nilai}")
print(f"Grade: {grade}")
print(f"Keterangan: {keterangan}")
