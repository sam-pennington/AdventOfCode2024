import copy

def load_reports(filename: str) -> list[list[int]]:
    reports: list[list[int]] = None
    with open(filename, "r") as fb:
        reports = [[int(level) for level in line.rstrip().split()] for line in fb]
    assert(reports is not None)
    return reports

def report_safe(report: list[int]) -> bool:
    increasing: bool = None
    for idx, level in enumerate(report):
        if idx == 0: continue
        if level == report[idx - 1]: return False
        levelIncreasing: bool = level > report[idx - 1]
        if increasing is None: increasing = levelIncreasing
        if increasing != levelIncreasing: return False
        delta: int = abs(level - report[idx - 1])
        if delta < 1 or delta > 3: return False
    return True

def naive_dampen(report: list[int]) -> bool:
    if report_safe(report): return True
    for idx in range(len(report)):
        moderatedReport = copy.copy(report)
        moderatedReport.pop(idx)
        if report_safe(moderatedReport): return True
    return False

def main() -> None:
    reports: list[list[int]] = load_reports('puzzle-input-2.txt')
    safeCount: int = sum([1 if naive_dampen(report) else 0 for report in reports])
    print(safeCount)

if __name__ == "__main__":
    main()