import operator
from typing import Callable

def load(filename: str) -> list[list[str]]:
    result: list[list[str]] = []
    with open(filename, 'r') as fb:
        for line in fb:
            result.append(list(line.rstrip()))
    return result


def find_antenna(grid: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    result: dict[str, list[tuple[int, int]]] = {}
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if not col == '.':
                if col not in result:
                    result[col] = []
                result[col].append((row_idx, col_idx))
    return result

def calculate_vector(point_start: tuple[int, int], point_end: tuple[int, int]) -> tuple[int, int]:
    return (point_end[0] - point_start[0], point_end[1] - point_start[1])

def find_extents(grid: list[list[str]]) -> tuple[int, int]:
    max_row: int = len(grid)
    max_col: int = len(grid[0])
    return (max_row, max_col)

def in_bounds(extents: tuple[int, int], position: tuple[int, int]) -> bool:
    return (position[0] < extents[0] and position[0] >= 0) and (position[1] < extents[1] and position[1] >= 0)

def apply_vector(vector: tuple[int, int], position: tuple[int, int], op: Callable) -> tuple[int, int]:
    return (op(position[0], vector[0]), op(position[1], vector[1]))

def main() -> None:
    grid: list[list[str]] = load('puzzle-input-2.txt')
    antenna: dict[str, list[tuple[int, int]]] = find_antenna(grid)
    extents: tuple[int, int] = find_extents(grid)
    
    antinodes: set[tuple[int, int]] = set()
    for _, positions in antenna.items():
        num_positions: int = len(positions)
        # All Antenna are also antinodes
        antinodes.update(positions)
        for idx, position in enumerate(positions):
            for next in range(idx + 1, num_positions):
                vector: tuple[int, int] = calculate_vector(position, positions[next])

                anti_start: tuple[int, int] = apply_vector(vector, position, operator.sub)
                while in_bounds(extents, anti_start):
                    antinodes.add(anti_start)
                    anti_start = apply_vector(vector, anti_start, operator.sub)

                anti_end: tuple[int, int] = apply_vector(vector, positions[next], operator.add)
                while in_bounds(extents, anti_end):
                    antinodes.add(anti_end)
                    anti_end = apply_vector(vector, anti_end, operator.add)
      
    print(len(antinodes))
        

if __name__ == "__main__":
    main()