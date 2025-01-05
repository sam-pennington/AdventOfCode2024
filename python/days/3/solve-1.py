import re

def load_input(filename: str) -> str:
    with open(filename, "r") as fb:
        return fb.read().replace('\n', '')
    
def valid_hits(input: str) -> list[str]:
    return re.findall(r"mul\(\d+,\d+\)", input)

def parse_expression(exp: str) -> int:
    numbers: list[str] = re.findall(r"\d+", exp)
    return int(numbers[0]) * int(numbers[1])

def main() -> None:
    result: int = sum([parse_expression(e) for e in valid_hits(load_input('puzzle-input-1.txt'))])
    print(result)

if __name__ == "__main__":
    main()