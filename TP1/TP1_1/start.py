class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_kelvin(self, celsius):
        """Convert Celsius to Kelvin."""
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15


def ask_to_continue():
    """Ask user if they want to continue."""
    answer = input("Do another conversion? (Y/N): ").strip().upper()
    return answer == "Y"


def main():
    converter = TemperatureConverter()
    continue_conversion = True

    while continue_conversion:
        print("\nMenu:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Convert Celsius to Kelvin")
        print("4. Convert Kelvin to Celsius")

        choice = input("Please select an option (1, 2, 3, or 4): ").strip()

        if choice == "1":
            celsius = input("Enter temperature in Celsius: ")
            try:
                celsius_value = float(celsius)
                fahrenheit = converter.celsius_to_fahrenheit(celsius_value)
                print(f"{celsius_value:.2f} Celsius is {fahrenheit:.2f} Fahrenheit.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "2":
            fahrenheit = input("Enter temperature in Fahrenheit: ")
            try:
                fahrenheit_value = float(fahrenheit)
                celsius = converter.fahrenheit_to_celsius(fahrenheit_value)
                print(f"{fahrenheit_value:.2f} Fahrenheit is {celsius:.2f} Celsius.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "3":
            celsius = input("Enter temperature in Celsius: ")
            try:
                celsius_value = float(celsius)
                kelvin = converter.celsius_to_kelvin(celsius_value)
                print(f"{celsius_value:.2f} Celsius is {kelvin:.2f} Kelvin.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "4":
            kelvin = input("Enter temperature in Kelvin: ")
            try:
                kelvin_value = float(kelvin)
                if kelvin_value < 0:
                    print("Kelvin cannot be negative. Please enter a valid temperature.")
                    continue
                celsius = converter.kelvin_to_celsius(kelvin_value)
                print(f"{kelvin_value:.2f} Kelvin is {celsius:.2f} Celsius.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        else:
            print("Invalid selection. Please choose option 1, 2, 3, or 4.")

        continue_conversion = ask_to_continue()


if __name__ == "__main__":
    main()
