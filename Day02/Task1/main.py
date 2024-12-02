
def is_safe_report(report):
    increasing = report[1] - report[0] > 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if (increasing and diff <= 0) or (not increasing and diff >= 0) or abs(diff) > 3:
            return False
    return True

def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
    return count

with open('text.txt', 'r') as f:
    reports = [[int(num) for num in line.strip().split()] for line in f]

print(count_safe_reports(reports))