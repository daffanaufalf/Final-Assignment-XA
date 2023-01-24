from exception_handling import handle_exception
from user_input import get_employee_info

# Prosedur untuk mencetak informasi gaji karyawan
@handle_exception
def print_employee_info(name, nip, golongan, gaji_dasar, honor_lembur, jumlah_lembur):
    golongan_gaji = {
        'A': 5000000,
        'B': 3000000,
        'C': 1000000
    }
    total_honor_lembur = honor_lembur * jumlah_lembur
    total_gaji = golongan_gaji[golongan] + gaji_dasar + total_honor_lembur
    print("Total honor lembur\t: ", total_honor_lembur)
    print("Total gaji seluruhnya\t: ", total_gaji)
    print("Keterangan\t\t:  Golongan Kerja\t :", golongan, "\n\t\t\t   Gaji Dasar\t\t :", gaji_dasar, "\n\t\t\t   Total Honor Lembur\t :", total_honor_lembur, "\n\t\t\t   Total Gaji Seluruhnya :", total_gaji)