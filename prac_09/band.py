class Band:
    """Band Class"""

    def __init__(self, name):
        """Constructor of the band with a name"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to band"""
        if musician is not None:
            self.musicians.append(musician)

    def play(self):
        """Musicians play their instruments"""
        return "\n".join([musician.play() for musician in self.musicians])

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

