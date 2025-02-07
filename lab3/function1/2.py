def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Example usage:
f = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {fahrenheit_to_celsius(f):.2f}")
