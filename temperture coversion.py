temp = float(input("Enter temperature: "))
convert_to = input("Convert to (C)elsius or (F)ahrenheit? ")
if convert_to.lower() == "c":
     celsius = (temp - 32) * 5 / 9
     print(f"{temp}°F is equal to {celsius:.2f}°C")
elif convert_to.lower() == "f":
     fahrenheit= temp * 9 / 5 + 32
     print(f"{temp}°C is equal to {fahrenheit:.2f}°F")
else:
    print("Invalid input. Please enter 'C' or 'F'.")