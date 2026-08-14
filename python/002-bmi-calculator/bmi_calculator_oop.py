"""
BMI Calculator CLI Application using OOP

This program calculates Body Mass Index (BMI) based on
the user's weight and height.

BMI Formula:
BMI = weight (kg) / height² (m²)
"""


class BMICalculator:

    def get_positive_number(self, prompt):
        while True:
            try:
                value = float(input(prompt))

                if value <= 0:
                    print("Please enter a value greater than zero.")
                else:
                    return value

            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal weight"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"

    def run(self):
        print("=== BMI Calculator ===")

        # Get user inputs
        weight = self.get_positive_number("Enter your weight (kg): ")
        height = self.get_positive_number("Enter your height (m): ")

        # Calculate BMI
        bmi = self.calculate_bmi(weight, height)

        # Determine BMI category
        category = self.get_bmi_category(bmi)

        # Display result
        print("\nResult")
        print("----------------")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        


def main():
    calculator = BMICalculator()
    calculator.run()
    mylist = [1,3,5,7,9,11]
    mylist[2:4] = [-3,-9,-11,-13]
    print(mylist)


if __name__ == "__main__":
    main()