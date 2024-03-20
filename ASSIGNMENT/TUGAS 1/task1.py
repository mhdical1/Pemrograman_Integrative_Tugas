# SOAL NO 1

#NAMA : MUHAMMAD FAISAL HAMZAH
#NIM  : 211402132

# Mengukur gaji bulanan dari gaji tahunan

def gajibulanan():
    print("=== Menghitung Gaji Bulanan ===")
    print("\n")

    nama = input("Masukkan Nama Anda: ")
    gaji_tahunan = int(input("Masukkan Gaji Tahunan Anda: "))

    print("\n")

    gaji_bulanan = round(gaji_tahunan / 12, 0)

    print("Nama :", nama)
    print("Gaji Bulanan: Rp.", gaji_bulanan)

    print("\n")
    print("=+=+=+= Thank You =+=+=+=")
    print("\n")

if __name__ == "__main__":
    gajibulanan()