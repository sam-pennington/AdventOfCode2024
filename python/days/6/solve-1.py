DIRECTION_NORTH: int = 0
DIRECTION_EAST: int = 1
DIRECTION_SOUTH: int = 2
DIRECTION_WEST: int = 3

MOVE_NORTH: tuple[int, int] = (-1, 0)
MOVE_EAST: tuple[int, int] = (0, 1)
MOVE_SOUTH: tuple[int, int] = (1, 0)
MOVE_WEST: tuple[int, int] = (0, -1)

MOVEMENT: dict[int, tuple[int, int]] = {
    DIRECTION_NORTH: MOVE_NORTH,
    DIRECTION_EAST: MOVE_EAST,
    DIRECTION_SOUTH: MOVE_SOUTH,
    DIRECTION_WEST: MOVE_WEST
}

def load(filename: str) -> list[list[str]]:
    floor: list[list[str]] = []
    with open(filename, "r") as fb:
        for line in fb:
            floor.append(list(line.rstrip()))
    return floor

def find_start(floor: list[list[str]]) -> tuple[int, int]:
    for row_idx, row in enumerate(floor):
        for col_idx, col in enumerate(row):
            if col == '^':
                return (row_idx, col_idx)
    return None

def get_extents(floor: list[list[str]]) -> tuple[int, int]:
    return (len(floor), len(floor[0]))

def in_bounds(extents: tuple[int, int], next: tuple[int, int]) -> bool:
    return (next[0] < extents[0] and next[0] >= 0) and (next[1] < extents[1] and next[1] >= 0)

def calculate_step(floor: list[list[str]], extents: tuple[int, int], guard_position: tuple[int, int], guard_direction: int) -> tuple[tuple[int, int], int]:
    movement: tuple[int, int] = MOVEMENT[guard_direction]
    next: tuple[int, int] = (guard_position[0] + movement[0], guard_position[1] + movement[1])
    if not in_bounds(extents, next): return (next, guard_direction)
    next_symbol: str = floor[next[0]][next[1]]
    if next_symbol == '#':
        guard_direction = (guard_direction + 1) % 4
        next = guard_position
    return (next, guard_direction)
   
def path_guard(floor: list[list[str]]) -> list[tuple[int, int]]:
    distinct_steps: set[tuple[int, int]] = set()

    guard_position: tuple[int, int] = find_start(floor)
    assert(guard_position is not None)
    guard_direction: int = DIRECTION_NORTH

    extents: tuple[int, int] = get_extents(floor)

    next_step: tuple[int, int] = None

    while (next_step is None) or (in_bounds(extents, next_step)):
        if next_step is not None: 
            distinct_steps.add(next_step)
            guard_position = next_step
        next_step, guard_direction = calculate_step(floor, extents, guard_position, guard_direction)
        
    return distinct_steps
    
def main() -> None:
    floor: list[list[str]] = load('puzzle-input-1.txt')
    guard_path_unique: set[tuple[int, int]] = path_guard(floor)
    print(len(guard_path_unique))


if __name__ == "__main__":
    main()