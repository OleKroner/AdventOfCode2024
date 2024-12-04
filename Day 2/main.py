safe_reports = 0
safe_reportsV2 = 0

def is_report_safe(report: list[str]):
    previous_level = None
    order = None

    for level in report:
        lvl_num = int(level)

        if previous_level != None:
            if not 0 < abs(previous_level - lvl_num) < 4:
                return (False, report.index(level))
            
            if order == None:
                order = (previous_level - lvl_num) > 0
            else:
                if ((previous_level - lvl_num) > 0) != order:
                    return (False, report.index(level))

        previous_level = lvl_num
    
    return (True, 0)

with open("./input.txt", "r") as file:
    for line in file:
        report = line.split()

        report_result = is_report_safe(report)

        if report_result[0] is True:
            safe_reports += 1
            safe_reportsV2 += 1
        
        else:
            for i in range(len(report)):
                temp_report = report.copy()
                temp_report.pop(i)
                
                if is_report_safe(temp_report)[0]:
                    safe_reportsV2 += 1
                    break

print(safe_reports)
print(safe_reportsV2)