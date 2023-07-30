def main():
    choice = input("Type ""C"" to convert to Celsius or ""F"" to convert to Fahrenheit: ")
    if choice.lower() == 'c':
        degreesFahrenheit = float(input("Enter degrees in Fahrenheit: "))
        print(f"{convertToCelsius(degreesFahrenheit)} {chr(176)}C")
    elif choice.lower() == 'f':
        degreesCelsius = float(input("Enter degrees in Celsius: "))
        print(f"{convertToFahrenheit(degreesCelsius)} {chr(176)}F")
        
def convertToFahrenheit(degreesCelsius):
    """Converts from Celsius to Fahrenheit

    Args:
        degreesCelsius (float): User inputted Celsius value

    Returns:
        float: Conversion of Celsius to Fahrenheit
    """
    return round(degreesCelsius * (9/5) + 32, 2)
    

def convertToCelsius(degreesFahrenheit):
    """Converts from Fahrenheit to Celsius

    Args:
        degreesFahrenheit (float): User inputted Fahrenheit value

    Returns:
        float: Conversion of Fahrenheit to Celsius
    """
    return round((degreesFahrenheit - 32) * (5/9), 2)
   
    
    

if __name__ == "__main__":
    main()