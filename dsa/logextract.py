
from datetime import datetime


def extractErrorLogs(logs):

    my_log = []
    for i, log in enumerate(logs):
        status = log[2]
        _time = datetime.strptime(log[0] + " " + log[1], "%d-%m-%Y %H:%M")

        if status == "ERROR" or status == "CRITICAL":
            log.insert(0, i)
            log.insert(1, _time)
            my_log.append(log)

    return [element[2:] for element in sorted(my_log, key=lambda x: x[1])]


print(extractErrorLogs([
    ["01-01-2023", "14:00", "ERROR", "failed"],
    ["01-01-2023", "14:00", "CRITICAL", "failed"],
    ["01-01-2023", "15:00", "INFO", "established"],
    ["01-01-2023", "01:30", "ERROR", "failed"]
]))

