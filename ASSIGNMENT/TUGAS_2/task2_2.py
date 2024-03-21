#NAMA :  MUHAMMAD FAISAL HAMZAH
#NIM  :  211402132

total = 0.00

while True:
    angka = float(input("Masukkan angka: "))
    if angka < 0:
        break
    total += angka

# Format total dengan dua digit setelah desimal
total_str = "{:.2f}".format(total)

# Cetak total
print("Total: " + total_str)   