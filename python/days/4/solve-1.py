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

def find_e(wordGrid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(wordGrid[row])
    if col + 1 >= length or col + 2 >= length or col + 3 >= length:
        return False
    try:
        X: str = 'X'
        M: str = wordGrid[row][col + 1]
        A: str = wordGrid[row][col + 2]
        S: str = wordGrid[row][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except Exception as e:
        return False

def find_w(wordGrid: list[list[str]], row: int, col: int) -> bool:
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row][col - 1]
        A: str = wordGrid[row][col - 2]
        S: str = wordGrid[row][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_n(wordGrid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row - 1][col]
        A: str = wordGrid[row - 2][col]
        S: str = wordGrid[row - 3][col]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_s(wordGrid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(wordGrid)
    if row + 1 >= length or row + 2 >= length or row + 3 >= length:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row + 1][col]
        A: str = wordGrid[row + 2][col]
        S: str = wordGrid[row + 3][col]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_nw(wordGrid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row - 1][col - 1]
        A: str = wordGrid[row - 2][col - 2]
        S: str = wordGrid[row - 3][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_ne(wordGrid: list[list[str]], row: int, col: int) -> bool:
    if row - 1 < 0 or row - 2 < 0 or row - 3 < 0:
        return False
    length = len(wordGrid[row])
    if col + 1 >= length or col + 2 >= length or col + 3 >= length:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row - 1][col + 1]
        A: str = wordGrid[row - 2][col + 2]
        S: str = wordGrid[row - 3][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_sw(wordGrid: list[list[str]], row: int, col: int) -> bool:
    length: int = len(wordGrid)
    if row + 1 >= length or row + 2 >= length or row + 3 >= length:
        return False
    if col - 1 < 0 or col - 2 < 0 or col - 3 < 0:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row + 1][col - 1]
        A: str = wordGrid[row + 2][col - 2]
        S: str = wordGrid[row + 3][col - 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_se(wordGrid: list[list[str]], row: int, col: int) -> bool:
    row_length: int = len(wordGrid)
    col_length: int = len(wordGrid[row])
    if row + 1 >= row_length or row + 2 >= row_length or row + 3 >= row_length:
        return False
    if col + 1 >= col_length or col + 2 >= col_length or col + 3 >= col_length:
        return False
    try: 
        X: str = 'X'
        M: str = wordGrid[row + 1][col + 1]
        A: str = wordGrid[row + 2][col + 2]
        S: str = wordGrid[row + 3][col + 3]
        return 'XMAS' == ''.join([X, M, A, S])
    except:
        return False
    
def find_xmas_count(wordGrid: list[list[str]]) -> int:
    count: int = 0
    funcs: Callable[[list[list[str]], int, int], bool] = [
        find_n,
        find_s,
        find_e,
        find_w,
        find_nw,
        find_ne,
        find_sw,
        find_se
    ]
    for idx_row, row in enumerate(wordGrid):
        for idx_col, col in enumerate(row):
            if col == 'X':
                for f in funcs:
                    if f(wordGrid, idx_row, idx_col):
                        count = count + 1
    return count

def main() -> None:
    wordGrid: list[list[str]] = load_input('puzzle-input-1.txt')
    count: int = find_xmas_count(wordGrid)
    print(count)

if __name__ == "__main__":
    main()