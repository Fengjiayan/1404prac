from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Main function."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_date = 0
    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choose = input(">>> ")
        if choose == "q":
            break
        elif choose == "c":
            current_taxi = choose_taxi(taxis)
        elif choose == "d":
            bill_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_date:.2f}")
    print(f"Total trip cost: ${bill_date:.2f}")
    print_taxis("Taxis are now:", taxis)


def print_taxis(print_statement, taxis):
    """Print taxis."""
    print(print_statement)
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi."""
    print_taxis("Taxis available:", taxis)
    try:
        choose = int(input("Choose taxi: "))
        if choose < 0 or choose >= len(taxis):
            raise ValueError()
        return taxis[choose]
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(taxi):
    """Drive the taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    try:
        distance = int(input("Drive how far? "))
        if distance < 0:
            raise ValueError()
        taxi.start_fare()
        taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
        return taxi.get_fare()
    except ValueError:
        print("Invalid Input")
    return 0


main()
