from employee_info import print_employee_info
from user_input import get_employee_info

if __name__ == "__main__":
    name, nip, golongan, gaji_dasar, honor_lembur, jumlah_lembur = get_employee_info()
    print_employee_info(name, nip, golongan, gaji_dasar, honor_lembur, jumlah_lembur)