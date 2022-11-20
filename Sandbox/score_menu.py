def main():
    display_menu()
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_input_score()
        elif choice == "P":
            print("Score Result: " + get_score_result(score))
        elif choice == "S":
            print_score_stars(score)
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()
    print("Goodbye!")


def display_menu():
    print("""(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit""")


def get_input_score():
    score = int(input("Please input a score[0-100]: "))
    while score < 0 or score > 100:
        score = int(input("Please input a score[0-100]: "))
    return score


def get_score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def print_score_stars(score):
    for i in range(score):
        print("*", end="")
    print()


main()
