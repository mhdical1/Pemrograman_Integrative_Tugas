#Soal No 4

#NAMA : MUHAMMAD FAISAL HAMZAH
#NIM  : 211402132

# Membaca input angka
num = int(input("Masukkan angka: "))

# Menginisialisasi variabel sum
sum = 0

# Menghitung jumlah dari angka-angka dari 1 sampai num
for i in range(1, num + 1):
    sum += i

# Menampilkan hasil
print("Jumlah dari angka-angka dari 1 sampai", num, "adalah:", sum)