class BMI:
    def __init__(self):
        self.weight = float(input("Masukkan berat (kg): "))
        self.height = float(input("Masukkan tinggi (m): "))

    def BMI_Value(self):
        return round(self.weight / (self.height ** 2), 2)

# Contoh penggunaan kelas
person = BMI()
print("BMI: ", person.BMI_Value())