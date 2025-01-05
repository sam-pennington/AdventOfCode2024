import re

def load_input(filename: str) -> str:
    with open(filename, "r") as fb:
        return fb.read().replace('\n', '')
    
def valid_hits(input: str) -> list[str]:
    return re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", input)

def parse_expression(exp: str) -> int:
    numbers: list[str] = re.findall(r"\d+", exp)
    return int(numbers[0]) * int(numbers[1])

def is_do(expression: str) -> bool:
    return expression == 'do()'

def is_dont(expression: str) -> bool:
    return expression == 'don\'t()'

def execute_machine(expressions: list[str]):
    enabled: bool = True
    result: list[int] = []
    for exp in expressions:
        if is_do(exp): enabled = True
        elif is_dont(exp): enabled = False
        elif enabled: result.append(parse_expression(exp))
    return result

def main() -> None:
    result: int = sum(execute_machine(valid_hits(load_input('puzzle-input-2.txt'))))
    print(result)


if __name__ == "__main__":
    main()