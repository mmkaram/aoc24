with open("input.txt", "r") as file:
    reports = [line.strip() for line in file]

reports = [list(map(int, report.split())) for report in reports]
def isIncreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def isDecreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

def is_delta_valid(report):
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(report):
    return (isIncreasing(report) or isDecreasing(report)) and is_delta_valid(report)

def can_fix_by_removing_one(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# Main logic
good = 0
for report in reports:
    if is_safe(report) or can_fix_by_removing_one(report):
        good += 1

print(good)

