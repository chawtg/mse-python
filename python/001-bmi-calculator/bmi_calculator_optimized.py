"""
BMI Calculator CLI Application

Calculates BMI based on the user's weight and height.
"""

def is_float(value):
    try:
        return float(value)
    except ValueError:
        return False


def input_float(prompt):
    while True:
        value = is_float(input(prompt))

        if value is not False:
            return value

        print("Please enter a number.")


class BMICalculator:

    def get_data(self):
        self.weight = input_float(
            "Please enter your weight in kilograms: "
        )

        self.height = input_float(
            "Please enter your height in centimetres: "
        ) / 100

    def calculate(self):
        return round(self.weight / (self.height ** 2), 2)


def main():
    print("\n" + "=" * 42)
    print("Hello, let's calculate your BMI.")

    calculator = BMICalculator()

    print()
    calculator.get_data()

    bmi = calculator.calculate()

    print(f"Your BMI is {bmi}")
    print("=" * 42)


if __name__ == "__main__":
    main()