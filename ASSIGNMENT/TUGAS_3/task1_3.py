# Baca file teks
with open("indata.txt", "r") as file:
    numbers = file.read().splitlines()

# Ubah string menjadi bilangan bulat
numbers = [int(number) for number in numbers]

# Hitung jumlah angka
total = sum(numbers)

# Cetak jumlah angka dengan dua digit desimal
print("{:.2f}".format(total))