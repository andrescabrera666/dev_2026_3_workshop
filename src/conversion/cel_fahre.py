class Conversion:

    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32



conversion = Conversion()

# Probar las conversiones
print(conversion.celsius_a_fahrenheit(0))
print(conversion.celsius_a_fahrenheit(100))
print(conversion.celsius_a_fahrenheit(37))
print(conversion.celsius_a_fahrenheit(-273.15))
print(conversion.celsius_a_fahrenheit(25.5))