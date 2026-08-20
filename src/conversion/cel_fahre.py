class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.

        Args:
            celsius (float): Temperatura en grados Celsius

        Returns:
            float: Temperatura en grados Fahrenheit

        Fórmula: F = (C x 9/5) + 32

        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9/5) + 32