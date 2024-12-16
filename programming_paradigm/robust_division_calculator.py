def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")