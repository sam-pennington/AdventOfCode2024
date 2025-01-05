
def load_reports(filename: str) -> list[list[int]]:
    reports: list[list[int]] = None
    with open(filename, "r") as fb:
        reports = [[int(level) for level in line.rstrip().split()] for line in fb]
    assert(reports is not None)
    return reports

def report_safe(report: list[int]) -> tuple[bool, str]:
    increasing: bool = None
    for idx, level in enumerate(report):
        if idx == 0: continue
        if level == report[idx - 1]: return (False, "Duplicate Values")
        levelIncreasing: bool = level > report[idx - 1]
        if increasing is None: increasing = levelIncreasing
        if increasing != levelIncreasing: return (False, "Discrepency in direction")
        delta: int = abs(level - report[idx - 1])
        if delta < 1 or delta > 3: return (False, f"Delta: {delta} for {level} and {report[idx - 1]} outside tolerance")
    return (True, "Safe")

def main() -> None:
    reports: list[list[int]] = load_reports('puzzle-input-1.txt')
    safeCount: int = sum([1 if report_safe(report)[0] else 0 for report in reports])
    print(safeCount)

if __name__ == "__main__":
    main()