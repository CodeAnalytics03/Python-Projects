def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(celsius):
    return (celsius * 9 / 5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit * 5 / 9) - 32

def kg_to_lbs(kg):
    return kg * 2.205

def lbs_to_kg(lbs):
    return lbs / 2.205

print("===================================")
print("Welcome to the Unit Converter!")
print("===================================")
while True:
    print("===================================")
    print("Select the conversion you want to perform:")
    print("===================================")
    print("🌍Unit Converter")
    print("===================================")
    print("1. Kilometers to Miles" )
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("===================================")

    choice = input("Choose conversion (1-6) : ")

    try:
        if choice == '1':
            km = float(input("Enter Kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")

        elif choice == '2':
            miles = float(input("Enter Miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")

        elif choice == '3':
            celsius = float(input("Enter Celsius: "))
            print(f"{celsius} °C = {c_to_f(celsius):.2f} °F")

        elif choice == '4':
            fahrenheit = float(input("Enter Fahrenheit: "))
            print(f"{fahrenheit} °F = {f_to_c(fahrenheit):.2f} °C") 

        elif choice == '5':
            kg = float(input("Enter Kilograms: "))
            print(f"{kg} kg = {kg_to_lbs(kg):.2f} lbs")

        elif choice == '6':
            lbs = float(input("Enter Pounds: "))
            print(f"{lbs} lbs = {lbs_to_kg(lbs):.2f} kg")

        # elif choice not in ['1', '2', '3', '4', '5', '6']:
        #     print("Invalid choice. Please select a number between 1 and 6.")
        #     continue

        elif choice == 'q':
            print("Thank You for using the Unit Converter. GoodBye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")