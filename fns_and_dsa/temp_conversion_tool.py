FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_value = input("Enter the temperature to convert: ")
        temp_value = float(temp_value)
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if scale == "C":
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp}°F")
        elif scale == "F":
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp}°C")
        else:
            print("Invalid input. Please speccify 'C' for Celsius or 'F' for fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value")

if __name__ == "__main__":
    main()