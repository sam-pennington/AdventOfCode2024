def load_input(filename: str) -> list[list[str]]:
    matrix: list[list[str]] = list(list())
    with open(filename, "r") as fb:
        for line in fb:
            row = list(line.rstrip())
            assert(len(row) == 140)
            matrix.append(row)
        assert(len(matrix) == 140)
    return matrix

def is_cross(wordGrid: list[list[str]], centre_row: int, centre_col: int) -> bool:
    row_length: int = len(wordGrid)
    col_length: int = len(wordGrid[centre_row])
    if centre_col - 1 < 0 or centre_col + 1 >= col_length or centre_row + 1 >= row_length or centre_row - 1 < 0:
        return False 
    tl: str = wordGrid[centre_row - 1][centre_col - 1]
    tr: str = wordGrid[centre_row - 1][centre_col + 1]
    bl: str = wordGrid[centre_row + 1][centre_col - 1]
    br: str = wordGrid[centre_row + 1][centre_col + 1]

    top_left_diag: bool = ''.join([tl, 'A', br]) == 'MAS'
    top_right_diag: bool = ''.join([tr, 'A', bl]) == 'MAS'
    bot_left_diag: bool = ''.join([bl, 'A', tr]) == 'MAS'
    bot_right_diag: bool = ''.join([br, 'A', tl]) == 'MAS'

    return sum([1 if x else 0 for x in [top_left_diag, top_right_diag, bot_left_diag, bot_right_diag]]) == 2

def find_xmas_count(wordGrid: list[list[str]]) -> int:
    count: int = 0
    for idx_row, row in enumerate(wordGrid):
        for idx_col, col in enumerate(row):
            if col == 'A':
                if is_cross(wordGrid, idx_row, idx_col):
                    count = count + 1
    return count

def main() -> None:
    wordGrid: list[list[str]] = load_input('puzzle-input-2.txt')
    print(find_xmas_count(wordGrid))


if __name__ == "__main__":
    main()