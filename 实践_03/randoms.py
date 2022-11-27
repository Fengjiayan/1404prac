import random

print(random.randint(5, 20))  # line 1
# output: 8
# I can see the smallest number is 5, the largest number is 20.

print(random.randrange(3, 10, 2))  # line 2
# output: 9
# I can see the smallest number is 3, the largest number is 9.
# As the step is 2, so it can't produce 4 in this code

print(random.uniform(2.5, 5.5))  # line 3
# output: 4.437103825949992
# I can see the smallest number is 2.5, the largest number is smaller but close to 5.5.

# produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
