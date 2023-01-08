from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes reliability."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()}, plus flagfall of ${SilverServiceTaxi.flagfall:.2f},"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + SilverServiceTaxi.flagfall
