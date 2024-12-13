# Initialize two empty lists
column1 = []
column2 = []

# Open the file and process each line
with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        column1.append(num1)
        column2.append(num2)

column1_sorted = sorted(column1)
column2_sorted = sorted(column2)

# Puzzle 1
differences = [abs(a - b) for a, b in zip(column1_sorted, column2_sorted)]
print("Puzzle 1: Total difference:", sum(differences))

# Puzzle 2
score = 0
for item, value in enumerate(column1_sorted):
    occurrence = column2_sorted.count(value)
    score = score + occurrence*value
print("Puzzle 2: Total similarity score:", score)



