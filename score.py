"""Practical Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    score_result = get_score_result(score)
    print(score_result)
    random_score = random.randint(0, 100)
    print("Random Score: " + str(random_score))
    random_score_result = get_score_result(random_score)
    print(random_score_result)


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


main()
