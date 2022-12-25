"""
guitar
Estimate: 10 minutes
Actual:   13 minutes
"""
import time


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        now_year = time.localtime(time.time())[0]
        return now_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
