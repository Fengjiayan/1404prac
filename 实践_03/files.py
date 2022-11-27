# Step 1
name = input("What's your name: ")
file = open("name.txt", "w")
print(name, file=file)

# Step 2
file = open("name.txt", "r")
name = file.read().strip()
print(f"Your name is {name}")

# Step 3
file = open("numbers.txt", "r")
number1 = int(file.readline())
number2 = int(file.readline())
print(f"Sum of {number1} and {number2} is {number1 + number2}.")

# Step 4
file = open("numbers.txt", "r")
for line in file.readlines():
    print(line.strip())
