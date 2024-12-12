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
differences = [abs(a - b) for a, b in zip(column1_sorted, column2_sorted)]

print("Total difference:", sum(differences))