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

def find_last_file_id(representation: list[Union[int, None]]) -> Union[int, None]:
    for id in reversed(representation):
        if id is not None:
            return id
    return None

def get_file_size(representation: list[Union[int, None]], file_id: int) -> int:
    file_size: int = len([x for x in representation if x == file_id])
    return file_size

def get_file_idx(representation: list[Union[int, None]], file_id: int) -> Union[int, None]:
    for idx, val in enumerate(representation):
        if val == file_id: return idx
    return None

def large_enough_free_space(representation: list[Union[int, None]], file_idx: int, file_size: int) -> Union[int, None]:
    max_idx: int = len(representation)
    for idx, val in enumerate(representation):

        if val is None:
            sufficient = True
            for forward in range(file_size):
                if representation[idx + forward] is not None:
                    sufficient = False
            if sufficient: return idx

        if idx + 1 >= file_idx or (idx + file_size >= max_idx):
            break

    return None

def compact(block_representation: list[Union[int, None]]) -> list[Union[int, None]]:
    working_list = copy.deepcopy(block_representation)
    file_id: Union[int, None] = find_last_file_id(working_list)
    if file_id is not None:
        for idx in reversed(range(file_id + 1)):
            file_size: int = get_file_size(working_list, idx)
            file_idx: Union[int, None] = get_file_idx(working_list, idx)
            if file_idx is not None:
                insertion_idx: Union[int, None] = large_enough_free_space(working_list, file_idx, file_size)
                if insertion_idx is None: continue
                for move_idx in range(insertion_idx, insertion_idx + file_size):
                    working_list[move_idx] = idx
                for clear_idx in range(file_idx, file_idx + file_size):
                    working_list[clear_idx] = None
    return working_list

def checksum(compacted_list: list[Union[int, None]]) -> int:
    mulitplied: list[int] = []
    for idx, val in enumerate(compacted_list):
        if val is not None:
            mulitplied.append(idx * val)
    return sum(mulitplied)

def main() -> None:
    dense_representation: list[int] = load('puzzle-input-2.txt')
    block_representation: list[Union[int, None]] = generate_block_representation(dense_representation)
    compacted: list[Union[int, None]] = compact(block_representation)
    chksum: int = checksum(compacted)
    print(chksum)
        

if __name__ == "__main__":
    main()