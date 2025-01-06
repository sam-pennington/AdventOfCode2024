
import itertools

def load_input(filename: str) -> tuple[list[int], dict[int, int]]:
    list_a: list[int] = []
    list_b: list[int] = []
    with open(filename, "r") as fb:
        for line in fb:
            a: int = None
            b: int = None
            # Collapse multiple consequtive spaces and then split on space
            a, b = [int(x) for x in ' '.join(line.rstrip().split()).split()]
            assert(isinstance(a, int))
            assert(isinstance(b, int))
            list_a.append(a)
            list_b.append(b)
    assert(len(list_a) > 0)
    assert(len(list_a) == len(list_b))
    frequency_set: dict[int, int] = { k: len(list(v)) for k, v in itertools.groupby(sorted(list_b)) }
    return (list_a, frequency_set)

def calculate_similarity(list_a: list[int], frequency_set: dict[int, int]) -> int:
    return sum([(x * frequency_set.get(x, 0)) for x in list_a])

def main() -> None:
    list_a, frequency_set = load_input('puzzle-input-2.txt')
    list_a = sorted(list_a)
    print(calculate_similarity(list_a, frequency_set))


if __name__ == "__main__":
    main()