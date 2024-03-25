#Muhammad Faisal Hamzah 211402132
# Mengambil Angka (int) dari file teks

# Membuka file teks
with open("input.txt", "r") as file:
  total = 0
  # Membaca per baris
  for line in file:
    # Mengambil Angka(int) dari baris
    number = int(line)

    # Menambahkan angka ke jumlah
    total += number

# Mencetak jumlah bilangan dengan pemisah koma dan tiga digit
print("Jumlah bilangan: " + format(total, ","))