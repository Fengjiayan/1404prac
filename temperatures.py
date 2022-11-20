def celsius_to_fahrenheit(temp):
    return temp * 1.8 + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) / 1.8


temp_celsius = float(input("Please input the celsius temperature: "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print("Fahrenheit temperature is:", temp_fahrenheit)
temp_fahrenheit = float(input("Please input the fahrenheit temperature: "))
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print("Celsius temperature is:", temp_celsius)
