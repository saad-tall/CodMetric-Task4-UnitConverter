def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

conversion_functions = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius),
    "3": ("Kilometers to Miles", kilometers_to_miles),
    "4": ("Miles to Kilometers", miles_to_kilometers),
    "5": ("Kilograms to Pounds", kilograms_to_pounds),
    "6": ("Pounds to Kilograms", pounds_to_kilograms)
}

def display_menu():
    print("\n--- Unit Converter ---")
    for key, (label, _) in conversion_functions.items():
        print(f"{key}. {label}")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the Unit Converter. Goodbye!")
            break

        if choice in conversion_functions:
            try:
                value = float(input("Enter the value to convert: "))
                label, func = conversion_functions[choice]
                result = func(value)
                print(f"\nResult of {label}: {result:.2f}\n")
            except ValueError:
                print("Invalid number. Please enter a valid numeric value.")
        else:
            print("Invalid option. Please select a valid choice.")

if __name__ == "__main__":
    main()