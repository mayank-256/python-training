def tempconv():
    print("select (a) for fahrenheit to celsius and (b) for celcius to fahrenheit.")
    x = input("Enter your choice: ")
    if x == "a":
        c = int(input("Enter a temperature in Celsius: "))
        f = (c * (9/5)) + 32
        print(f"{c}C is equal to {f}F in fahrenheit.")
    elif x == "b":
        f = int(input("Enter a temperature in Fahrenheit: "))
        c = (f-32) * (5/9)
        print(f"{f}F is equal to {c}C in Celsius.")

tempconv()