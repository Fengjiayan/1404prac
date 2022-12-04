"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    rows = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        rows.append(parts)
        print("----------")
    input_file.close()
    return rows


def print_data(datas):
    """print datas."""
    for data in datas:
        print(f"{data[0]} is taught by {data[1]} and has {data[2]} students")


main()