
def load_input(filename: str) -> tuple[list[int], list[int]]:
    list_a: list[int] = []
    list_b: list[int] = []
    with open(filename, "r") as fb:
        for line in fb:
            # Collapse multiple consequtive spaces and then split on space
            a, b = [int(x) for x in ' '.join(line.rstrip().split()).split()]
            assert(isinstance(a, int))
            assert(isinstance(b, int))
            list_a.append(a)
            list_b.append(b)
    assert(len(list_a) > 0)
    assert(len(list_a) == len(list_b))
    return (list_a, list_b)

def calculate_sum_difference(list_a: list[int], list_b: list[int]) -> int:
    assert(len(list_a) > 0)
    assert(len(list_a) == len(list_b))
    return sum([ abs(x[0] - x[1]) for x in zip(list_a, list_b) ])

def main() -> None:
    list_a, list_b = load_input('puzzle-input-1.txt')
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    print(calculate_sum_difference(list_a, list_b))


if __name__ == "__main__":
    main()