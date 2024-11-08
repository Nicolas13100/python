import tkinter as tk
from tkinter import messagebox

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

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Set window size
        window_width = 300
        window_height = 170

        # Get screen dimensions to center the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate x and y coordinates for centering the window
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the geometry of the window (widthxheight+x+y)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


        self.converter = TemperatureConverter()

        # Label and Entry for input temperature
        self.label_input = tk.Label(root, text="Enter Temperature:")
        self.label_input.grid(row=0, column=0, padx=10, pady=10)

        self.entry_temp = tk.Entry(root)
        self.entry_temp.grid(row=0, column=1, padx=10, pady=10)

        # Buttons for conversion options
        self.btn_c_to_f = tk.Button(root, text="Celsius to Fahrenheit", command=self.convert_c_to_f)
        self.btn_c_to_f.grid(row=1, column=0, padx=10, pady=5)

        self.btn_f_to_c = tk.Button(root, text="Fahrenheit to Celsius", command=self.convert_f_to_c)
        self.btn_f_to_c.grid(row=1, column=1, padx=10, pady=5)

        self.btn_c_to_k = tk.Button(root, text="Celsius to Kelvin", command=self.convert_c_to_k)
        self.btn_c_to_k.grid(row=2, column=0, padx=10, pady=5)

        self.btn_k_to_c = tk.Button(root, text="Kelvin to Celsius", command=self.convert_k_to_c)
        self.btn_k_to_c.grid(row=2, column=1, padx=10, pady=5)

        # Label to display the result
        self.label_result = tk.Label(root, text="Result:")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def convert_c_to_f(self):
        """Convert Celsius to Fahrenheit."""
        try:
            celsius = float(self.entry_temp.get())
            fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
            self.label_result.config(text=f"{celsius:.2f} Celsius is {fahrenheit:.2f} Fahrenheit.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

    def convert_f_to_c(self):
        """Convert Fahrenheit to Celsius."""
        try:
            fahrenheit = float(self.entry_temp.get())
            celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
            self.label_result.config(text=f"{fahrenheit:.2f} Fahrenheit is {celsius:.2f} Celsius.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

    def convert_c_to_k(self):
        """Convert Celsius to Kelvin."""
        try:
            celsius = float(self.entry_temp.get())
            kelvin = self.converter.celsius_to_kelvin(celsius)
            self.label_result.config(text=f"{celsius:.2f} Celsius is {kelvin:.2f} Kelvin.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

    def convert_k_to_c(self):
        """Convert Kelvin to Celsius."""
        try:
            kelvin = float(self.entry_temp.get())
            if kelvin < 0:
                messagebox.showerror("Invalid Input", "Kelvin cannot be negative.")
                return
            celsius = self.converter.kelvin_to_celsius(kelvin)
            self.label_result.config(text=f"{kelvin:.2f} Kelvin is {celsius:.2f} Celsius.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")


def tp1_1_tkinter_app():
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()


