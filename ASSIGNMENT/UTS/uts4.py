# MUHAMMAD FAISAL HAMZAH 211402132
# BERAT 58KG == 127.27lb, Tinggi 165cm == 5.5ft
import math

class BMI:
  # Properti 
  def __init__(self, weight, height):
    self.weight = weight
    self.height = height

  # Metode 
  def BMI_Value(self):
    return self.weight * 0.453592 / (self.height * 0.3048) ** 2

  def __eq__(self, other):
    return self.weight == other.weight and self.height == other.height


bmi1 = BMI(127.27, 5.5)
bmi2 = BMI(160, 6.0)

# Memanggil metode BMI_Value

print(bmi1.BMI_Value())

print(bmi2.BMI_Value())  

# Membandingkan objek BMI

print(bmi1 == bmi2)  # Print False
