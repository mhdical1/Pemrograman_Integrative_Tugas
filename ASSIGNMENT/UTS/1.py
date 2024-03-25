
#Muhammad Faisal Hamzah 211402132

import datetime


# Mengambil angka (integer)

num = int(input("Masukkan Angka: "))

# Menentukan jumlah hari dalam satu tahun

year = datetime.date.today().year

days_in_year = datetime.date(year, 12, 31).timetuple().tm_yday


# Membagi bilangan dengan jumlah hari dalam satu tahun

result = num / days_in_year


# Membulatkan hasil

result = round(result, 11)

print("Hasil pembagian adalah:", result)
