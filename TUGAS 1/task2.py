# Soal No 2
# Membaca angka bulat dan membaginya dengan 3

def menghitunghasilbagi3():
    print("=== Menghitung Hasil Bagi 3 Dalam Bentuk Desimal ===")
    print("\n")

    number = int(input("Masukkan angka bulat: "))

    print("\n")

    result = round(number / 3, 3)

    print("Hasil bagi 3: {:.3f}".format(result))

    print("\n")
    print("=+=+=+= Thank You =+=+=+=")
    print("\n")

if __name__ == "__main__":
    menghitunghasilbagi3()