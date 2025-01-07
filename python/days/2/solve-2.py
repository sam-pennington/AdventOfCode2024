import copy
from typing import Union

def load_reports(filename: str) -> list[list[int]]:
    reports: Union[list[list[int]], None] = None
    with open(filename, "r") as fb:
        reports = [[int(level) for level in line.rstrip().split()] for line in fb]
    assert(reports is not None)
    return reports

def report_safe(report: list[int]) -> bool:
    increasing: Union[bool, None] = None
    for idx, level in enumerate(report):
        if idx == 0: continue
        if level == report[idx - 1]: return False
        level_increasing: bool = level > report[idx - 1]
        if increasing is None: increasing = level_increasing
        if increasing != level_increasing: return False
        delta: int = abs(level - report[idx - 1])
        if delta < 1 or delta > 3: return False
    return True

def naive_dampen(report: list[int]) -> bool:
    if report_safe(report): return True
    for idx in range(len(report)):
        moderated_report = copy.copy(report)
        moderated_report.pop(idx)
        if report_safe(moderated_report): return True
    return False

def main() -> None:
    reports: list[list[int]] = load_reports('puzzle-input-2.txt')
    safe_count: int = sum([1 if naive_dampen(report) else 0 for report in reports])
    print(safe_count)

if __name__ == "__main__":
    main()