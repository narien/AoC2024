
def evaluateReport(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i+1])
            if diff < 1 or diff > 3:
                return False
        return True
    return False

def analyseReports(reports, allowModify):
    safeReports = 0

    for report in reports:
        if evaluateReport(report):
            safeReports += 1
            continue

        if allowModify:
            for i in range(len(report)):
                fixedReport = report[:i] + report[i + 1:]
                if evaluateReport(fixedReport):
                    safeReports += 1
                    break

    print("Number of safe", "(modified)" if allowModify else "", "reports: ", safeReports)

if __name__ == '__main__':
    reports = []

    with open('day2/input.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)
    
    analyseReports(reports, False)
    analyseReports(reports, True)

