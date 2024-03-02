#Soal No 5
# Program ini membaca angka-angka sampai -1 dimasukkan dan menghitung jumlah dari semua angka yang dimasukkan.

def hitung_jumlah():
   jumlah = 0
   while True:
       angka = input("Masukkan angka (-1 untuk berhenti): ")
       if angka == "-1":
           break
       try:
           angka = int(angka)
           jumlah += angka
       except ValueError:
           print("Input tidak valid. Harap masukkan angka atau -1 untuk berhenti.")
   return jumlah

# Menampilkan hasil
print("Jumlah dari semua angka yang dimasukkan adalah:", hitung_jumlah())