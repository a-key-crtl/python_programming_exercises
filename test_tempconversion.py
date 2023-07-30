from tempconversion import convertToFahrenheit, convertToCelsius

# tests celsius conversion
def test_celsius_conversion():
    assert convertToCelsius(0) == -17.78
    assert convertToCelsius(180) == 82.22
    assert convertToCelsius(convertToFahrenheit(15)) == 15
# tests fahrenheit conversion
def test_fahrenheit_conversion():
    assert convertToFahrenheit(0) == 32
    assert convertToFahrenheit(100) == 212