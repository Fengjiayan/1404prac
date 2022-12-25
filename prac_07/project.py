"""
project
Estimate: 20 minutes
Actual:   26 minutes
"""


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_complete(self):
        """Return True if the project is completed"""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """Return True if the project's priority is less than other's"""
        return self.priority < other.priority

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
