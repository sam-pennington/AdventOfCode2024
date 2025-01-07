from typing import Union
import copy

def load(filename: str) -> list[int]:
    with open(filename, 'r') as fb:
        return [int(x) for x in fb.read()]
            
def generate_block_representation(dense: list[int]) -> list[Union[int, None]]:
    id: int = 0
    free: bool = False
    result: list[Union[int, None]] = []
    for block in dense:
        for _ in range(block):
            result.append(None if free else id)
        id = id if free else id + 1
        free = not free
    return result

def find_leftmost_free(block_representation: list[Union[int, None]]) -> Union[int, None]:
    for idx, val in enumerate(block_representation):
        if val is None: return idx - 1
    return None

def compact(block_representation: list[Union[int, None]]) -> list[int]:
    working_list = copy.deepcopy(block_representation)
    last_inserted_index: Union[int, None] = find_leftmost_free(working_list)

    while last_inserted_index is not None:

        to_move: Union[int, None] = working_list.pop()

        while to_move is None:
            to_move = working_list.pop()

        representation_length: int = len(working_list)
        inserted: bool = False
        for idx in range(last_inserted_index, representation_length):
            if working_list[idx] is None:
                working_list[idx] = to_move
                inserted = True
                last_inserted_index = idx
                break

        if not inserted:
            last_inserted_index = None
            working_list.append(to_move)

    return [x for x in working_list if x is not None]
    
def checksum(compacted_list: list[int]) -> int:
    mulitplied: list[int] = []
    for idx, val in enumerate(compacted_list):
        mulitplied.append(idx * val)
    return sum(mulitplied)

def main() -> None:
    dense_representation: list[int] = load('puzzle-input-1.txt')
    block_representation: list[Union[int, None]] = generate_block_representation(dense_representation)
    compacted: list[int] = compact(block_representation)
    chksum: int = checksum(compacted)
    print(chksum)
        

if __name__ == "__main__":
    main()