"""
BMI Calculator CLI Application

This program calculates Body Mass Index (BMI) based on
the user's weight and height.

BMI Formula:
BMI = weight (kg) / height² (m)
"""

def get_positive_number(prompt):

    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a value greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"
    
def main():
    print("=== BMI Calculator ===")

    # Get user inputs
    weight = get_positive_number("Enter your weight (kg): ")
    height = get_positive_number("Enter your height (m): ")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Determine BMI category
    category = get_bmi_category(bmi)

    # Display result
    print("\nResult")
    print("----------------")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()