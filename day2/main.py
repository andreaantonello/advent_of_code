# Initialize an empty matrix
matrix = []

# Open the file and read each line
with open('input.txt', 'r') as file:
    for line in file:
        # Split the line into a list of integers
        row = list(map(int, line.split()))
        # Append the row to the matrix
        matrix.append(row)

def check_range(list, lower_bound, upper_bound):
    # Check if all elements are within the range [lower_bound, upper_bound]
    return all(lower_bound <= abs(x) <= upper_bound for x in list)

class ReportAnalysis:
    def __init__(self, diffRange):
        self.reportLine = []
        self.difference = []
        self.diffRange = diffRange

    def processLine(self, reportLine):
        # Set reportLine and calculate the difference between consecutive elements
        self.difference = [reportLine[i + 1] - reportLine[i] for i in range(len(reportLine) - 1)]
        # print("Difference:", self.difference)

    def isIncreasing(self):
        for diff in self.difference:
            if diff <= 0:
                return False
        return True

    def isDecreasing(self):
        for diff in self.difference:
            if diff >= 0:
                return False
        # print("Line is decreasing")
        return True

    def checkValidity(self, reportLine):
        self.reportLine = reportLine
        self.processLine(self.reportLine)
        result = self.standardValidityCheck()
        if not result:
            result = self.dampener()
        return result

    def standardValidityCheck(self):
        if self.isDecreasing() or self.isIncreasing():
            if check_range(self.difference, self.diffRange[0], self.diffRange[1]):
                return True
        return False

    def dampener(self):
        result = False
        for i in range(len(self.reportLine)):
            # Create a new report with the i-th element removed
            modified_report = self.reportLine[:i] + self.reportLine[i + 1:]
            print("modified_report is", modified_report)
            self.processLine(modified_report)
            result = self.standardValidityCheck()
            if result:
                print("Got it!")
                return result

# Main algorithm
validCounter = 0
for row in matrix:
    diffRange = [1, 3]
    rep_anal = ReportAnalysis(diffRange)
    result = rep_anal.checkValidity(row)
    print("result is", result)
    if result:
        validCounter = validCounter + 1
print("Total valid reports are:", validCounter)