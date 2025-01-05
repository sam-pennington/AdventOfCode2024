
import itertools

def load_input(filename: str) -> tuple[list[int], dict[int, int]]:
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
    frequencySet: dict[int, int] = { k: len(list(v)) for k, v in itertools.groupby(sorted(listB)) }
    return (listA, frequencySet)

def calculate_similarity(listA: list[int], frequencySet: dict[int, int]) -> int:
    return sum([(x * frequencySet.get(x, 0)) for x in listA])

def main() -> None:
    listA, frequencyListB = load_input('puzzle-input-2.txt')
    listA = sorted(listA)
    print(calculate_similarity(listA, frequencyListB))


if __name__ == "__main__":
    main()