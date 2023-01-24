# Modul untuk menangani kondisi pengecualian (exception)
def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("Terjadi kesalahan: ", e)
    return wrapper