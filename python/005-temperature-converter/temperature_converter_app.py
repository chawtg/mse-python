from temperature_converter import TemperatureConverter


class TemperatureConverterApp:
    """Runs the temperature converter application."""

    def __init__(self):
        self.converter = TemperatureConverter()

    def run(self):
        """Start the temperature converter."""
        temperature_input = input("Enter temperature: ")

        try:
            result = self.converter.convert(temperature_input)
            print(result)
        except ValueError as error:
            print(error)