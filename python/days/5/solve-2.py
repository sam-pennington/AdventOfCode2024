import math

def load_input(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, "r") as fb:
        precendenceRules = []
        updates = []
        precendenceLoading = True
        for line in fb:
            if len(line.strip()) == 0:
                precendenceLoading = False
            elif precendenceLoading:
                precendenceRules.append(line.rstrip())
            else:
                updates.append([int(x.strip()) for x in line.rstrip().split(',')])
        return (precendenceRules, updates)
    
def parse_rules(raw: list[str]) -> dict[int, list[int]]:
    result: dict[int, dict[str, list[int]]] = {}
    for l in raw:
        a: int = None
        b: int = None
        a, b = [int(x) for x in l.split("|")]
        if result.get(a) is None:
            result[a] = [b]
        else:
            result[a].append(b)

    return result

def validate_update(rules: dict[int, list[int]], update: list[int]) -> bool:
    page_set: set[int] = set()
    for i in update:
        for mustBeBefore in rules.get(i, []):
            if mustBeBefore in page_set:
                return False
        page_set.add(i)
    return True

def correct_update(rules: dict[int, list[int]], update: list[int]) -> list[int]:
    ordered: list[int] = []
    for numberToInsert in update:
        inserted: bool = False
        befores: set[int] = set(rules.get(numberToInsert, []))
        for idx, alreadyInseted in enumerate(ordered):
            if alreadyInseted in befores:
                ordered.insert(idx, numberToInsert)
                inserted = True
                break
        if not inserted: 
            ordered.append(numberToInsert)
    return ordered

def main() -> None:
    rawPrecendenceRules, rawUpdates = load_input('puzzle-input-2.txt')
    parsedRules: dict[int, list[int]] = parse_rules(rawPrecendenceRules)
    sum: int = 0
    for update in rawUpdates:
        if not validate_update(parsedRules, update):
            corrected: list[int] = correct_update(parsedRules, update)
            mid: int = math.floor(len(corrected) // 2)
            val: int = corrected[mid]
            sum = sum + val
    print(sum)

if __name__ == "__main__":
    main()