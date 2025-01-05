
def load_input(filename: str) -> tuple[list[int], list[int]]:
    listA: list[int] = []
    listB: list[int] = []
    with open(filename, "r") as fb:
        for line in fb:
            a: int = None
            b: int = None
            # Collapse multiple consequtive spaces and then split on space
            a, b = [int(x) for x in ' '.join(line.rstrip().split()).split()]
            assert(isinstance(a, int))
            assert(isinstance(b, int))
            listA.append(a)
            listB.append(b)
    assert(len(listA) > 0)
    assert(len(listA) == len(listB))
    return (listA, listB)

def calculate_sum_difference(listA: list[int], listB: list[int]) -> int:
    assert(len(listA) > 0)
    assert(len(listA) == len(listB))
    return sum([ abs(x[0] - x[1]) for x in zip(listA, listB) ])

def main() -> None:
    listA, listB = load_input('puzzle-input-1.txt')
    listA = sorted(listA)
    listB = sorted(listB)
    print(calculate_sum_difference(listA, listB))


if __name__ == "__main__":
    main()