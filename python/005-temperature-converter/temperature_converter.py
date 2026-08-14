class TemperatureConverter:
    """Converts temperatures between Fahrenheit and Celsius."""

    INVALID_INPUT_MESSAGE = (
        "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."
    )

    def convert(self, temperature_input):
        """
        Convert a temperature based on its C or F prefix.
        """
        temperature_input = temperature_input.strip()

        if len(temperature_input) < 2:
            raise ValueError(self.INVALID_INPUT_MESSAGE)

        prefix = temperature_input[0]
        value_text = temperature_input[1:]

        if prefix not in ("C", "F"):
            raise ValueError(self.INVALID_INPUT_MESSAGE)

        try:
            temperature = float(value_text)
        except ValueError:
            raise ValueError(self.INVALID_INPUT_MESSAGE)

        if prefix == "F":
            celsius = self._fahrenheit_to_celsius(temperature)
            return (
                f"{temperature_input} degrees Fahrenheit is converted "
                f"to {celsius:.2f} degrees Celsius"
            )

        fahrenheit = self._celsius_to_fahrenheit(temperature)
        return (
            f"{temperature_input} degrees Celsius is converted "
            f"to {fahrenheit:.2f} degrees Fahrenheit"
        )

    def _fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5 / 9

    def _celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32