"""
guitars
Estimate: 18 minutes
Actual:   20 minutes
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    while True:
        guitar = get_input_guitar()
        if guitar is None:
            break
        guitars.append(guitar)
        print(guitar, "added.\n")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_input_guitar():
    name = input("Name: ").strip()
    if name == "":
        return
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


main()
