from collections.abc import Callable

def load_input(filename: str) -> list[list[str]]:
    matrix: list[list[str]] = list(list())
    with open(filename, "r") as fb:
        for line in fb:
            row = list(line.rstrip())
            assert(len(row) == 140)
            matrix.append(row)
        assert(len(matrix) == 140)
    return matrix

def find_e(word_grid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(word_grid[row])
    if col + 1 >= length or col + 2 >= length or col + 3 >= length:
        return False
    try:
        X: str = 'X'
        M: str = word_grid[row][col + 1]
        A: str = word_grid[row][col + 2]
        S: str = word_grid[row][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except Exception as e:
        return False

def find_w(word_grid: list[list[str]], row: int, col: int) -> bool:
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row][col - 1]
        A: str = word_grid[row][col - 2]
        S: str = word_grid[row][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_n(word_grid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row - 1][col]
        A: str = word_grid[row - 2][col]
        S: str = word_grid[row - 3][col]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_s(word_grid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(word_grid)
    if row + 1 >= length or row + 2 >= length or row + 3 >= length:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row + 1][col]
        A: str = word_grid[row + 2][col]
        S: str = word_grid[row + 3][col]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_nw(word_grid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row - 1][col - 1]
        A: str = word_grid[row - 2][col - 2]
        S: str = word_grid[row - 3][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_ne(word_grid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    length = len(word_grid[row])
    if col + 1 >= length or col + 2 >= length or col + 3 >= length:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row - 1][col + 1]
        A: str = word_grid[row - 2][col + 2]
        S: str = word_grid[row - 3][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_sw(word_grid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(word_grid)
    if row + 1 >= length or row + 2 >= length or row + 3 >= length:
        return False
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row + 1][col - 1]
        A: str = word_grid[row + 2][col - 2]
        S: str = word_grid[row + 3][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_se(word_grid: list[list[str]], row: int, col: int) -> bool:
    row_length: int = len(word_grid)
    col_length: int = len(word_grid[row])
    if row + 1 >= row_length or row + 2 >= row_length or row + 3 >= row_length:
        return False
    if col + 1 >= col_length or col + 2 >= col_length or col + 3 >= col_length:
        return False
    try: 
        X: str = 'X'
        M: str = word_grid[row + 1][col + 1]
        A: str = word_grid[row + 2][col + 2]
        S: str = word_grid[row + 3][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_xmas_count(word_grid: list[list[str]]) -> int:
    count: int = 0
    funcs: list[Callable] = [
        find_n,
        find_s,
        find_e,
        find_w,
        find_nw,
        find_ne,
        find_sw,
        find_se
    ]
    for idx_row, row in enumerate(word_grid):
        for idx_col, col in enumerate(row):
            if col == 'X':
                for f in funcs:
                    if f(word_grid, idx_row, idx_col):
                        count = count + 1
    return count

def main() -> None:
    word_grid: list[list[str]] = load_input('puzzle-input-1.txt')
    count: int = find_xmas_count(word_grid)
    print(count)

if __name__ == "__main__":
    main()