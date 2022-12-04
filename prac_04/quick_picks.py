import random


picks_lines = int(input("How many quick picks? "))
for i in range(picks_lines):
    CONSTANTS = []
    for j in range(6):
        CONSTANTS.append(random.randint(1, 45))
        while CONSTANTS[-1] in CONSTANTS[:-1]:
            CONSTANTS[-1] = random.randint(1, 45)
    CONSTANTS = sorted(CONSTANTS)
    for number in CONSTANTS:
        print(f"{number:>3}", end="")
    print()