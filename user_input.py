# Fungsi untuk mengambil input dari user
def get_employee_info():
    name = input("Masukkan nama karyawan\t:  ")
    nip = input("Masukkan NIP\t\t:  ")
    golongan = input("Masukkan golongan kerja\t:  ")
    gaji_dasar = int(input("Masukkan gaji dasar\t:  "))
    honor_lembur = int(input("Masukkan honor lembur\t:  "))
    jumlah_lembur = int(input("Masukkan jumlah lembur\t:  "))
    return name, nip, golongan, gaji_dasar, honor_lembur, jumlah_lembur