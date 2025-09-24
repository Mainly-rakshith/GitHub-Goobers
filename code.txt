def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def convert_menu():
    while True:
        print("\nUnit Converter")
        print("1) Celsius to Fahrenheit")
        print("2) Fahrenheit to Celsius")
        print("3) Kilometers to Miles")
        print("4) Miles to Kilometers")
        print("0) Back")
        choice = input("Select: ").strip()

        if choice == "1":
            c = float(input("Celsius: "))
            print(f"Fahrenheit: {c_to_f(c)}")
        elif choice == "2":
            f = float(input("Fahrenheit: "))
            print(f"Celsius: {f_to_c(f)}")
        elif choice == "3":
            km = float(input("Kilometers: "))
            print(f"Miles: {km_to_miles(km)}")
        elif choice == "4":
            m = float(input("Miles: "))
            print(f"Kilometers: {miles_to_km(m)}")
        elif choice == "0":
            return
        else:
            print("Invalid choice")
