import math

def load_input(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, "r") as fb:
        precendence_rules = []
        updates = []
        precendence_loading = True
        for line in fb:
            if len(line.strip()) == 0:
                precendence_loading = False
            elif precendence_loading:
                precendence_rules.append(line.rstrip())
            else:
                updates.append([int(x.strip()) for x in line.rstrip().split(',')])
        return (precendence_rules, updates)
    
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
        for must_be_before in rules.get(i, []):
            if must_be_before in page_set:
                return False
        page_set.add(i)
    return True

def correct_update(rules: dict[int, list[int]], update: list[int]) -> list[int]:
    ordered: list[int] = []
    for number_to_insert in update:
        inserted: bool = False
        befores: set[int] = set(rules.get(number_to_insert, []))
        for idx, already_inserted in enumerate(ordered):
            if already_inserted in befores:
                ordered.insert(idx, number_to_insert)
                inserted = True
                break
        if not inserted: 
            ordered.append(number_to_insert)
    return ordered

def main() -> None:
    rawprecendence_rules, raw_updates = load_input('puzzle-input-2.txt')
    parsed_rules: dict[int, list[int]] = parse_rules(rawprecendence_rules)
    sum: int = 0
    for update in raw_updates:
        if not validate_update(parsed_rules, update):
            corrected: list[int] = correct_update(parsed_rules, update)
            mid: int = math.floor(len(corrected) // 2)
            val: int = corrected[mid]
            sum = sum + val
    print(sum)

if __name__ == "__main__":
    main()