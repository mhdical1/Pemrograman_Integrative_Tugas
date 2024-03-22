class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        # Calculate BMI using the formula: weight / (height * height)
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        # Override the equals method to compare weight and height of two BMI objects
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Example usage:
if __name__ == "__main__":
    person1 = BMI(70, 1.75)  # Weight: 70 kg, Height: 1.75 meters
    person2 = BMI(80, 1.80)  # Weight: 80 kg, Height: 1.80 meters

    print("BMI for person 1:", person1.BMI_Value())
    print("BMI for person 2:", person2.BMI_Value())

    # Comparing BMI objects
    print("Are person1 and person2 equal?", person1 == person2)
