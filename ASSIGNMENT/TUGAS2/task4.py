numbers = []

while True:
    number = int(input("Masukkan nilai: "))
    if number == -1:
        break
    numbers.append(number)

# Urutkan daftar angka
numbers.sort()

# Cetak daftar angka
print("Keluaran:")
for number in numbers:
    print(number)

# Hitung rata-rata
average = sum(numbers) / len(numbers)
print("Rata-rata: ", int(average))