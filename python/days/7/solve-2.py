import operator
import itertools

def load(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename, "r") as fb:
        result: list[tuple[int, list[int]]] = []
        for line in fb:
            left: str = None
            right: list[str] = None
            left, right = line.rstrip().split(':')
            numbers: list[int] = [int(x) for x in right.split()]
            result.append((int(left), numbers))
        return result
    
def valid(bundle: tuple[int, list[int]]) -> bool:
    operators: list[str] = list(itertools.product(["+", "*", "||"], repeat=len(bundle[1]) - 1))

    for permutation in operators:
        operand_a: int = bundle[1][0]
        operand_b: int = None
        for idx, op in enumerate(permutation):
            operand_b = bundle[1][idx+1]
            result: int = None
            if op == '+':
                result = operator.add(operand_a, operand_b)
            elif op == '*':
                result = operator.mul(operand_a, operand_b)
            else:
                op_a_as_str: str = str(operand_a)
                op_b_as_str: str = str(operand_b)
                result = int(op_a_as_str + op_b_as_str)
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