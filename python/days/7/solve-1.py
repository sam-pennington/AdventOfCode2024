import operator
import itertools

def load(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename, "r") as fb:
        result: list[tuple[int, list[int]]] = []
        for line in fb:
            left, right = line.rstrip().split(':')
            numbers: list[int] = [int(x) for x in right.split()]
            result.append((int(left), numbers))
        return result
    
def valid(bundle: tuple[int, list[int]]) -> bool:
    operators = list(itertools.product(["+", "*"], repeat=len(bundle[1]) - 1))

    for permutation in operators:
        operand_a: int = bundle[1][0]
        result = -1
        for idx, op in enumerate(permutation):
            operand_b = bundle[1][idx+1]
            result: int = operator.add(operand_a, operand_b) if op == '+' else operator.mul(operand_a, operand_b)
            operand_a = result
        if result == bundle[0]:
            return True
        
    return False

def main() -> None:
    parsed_values = load('puzzle-input-1.txt')
    valid_results: list[int] = []
    for bundle in parsed_values:
        if valid(bundle):
            valid_results.append(bundle[0])
    print(sum(valid_results))

if __name__ == "__main__":
    main()