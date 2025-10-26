while True:
    value = float(input("Enter the number (in gallon) you want to convert: "))

    if value < 0:
        break
    else:
        value_converted = value * 3.785
        print("your value convert to liters is: ", value_converted)
