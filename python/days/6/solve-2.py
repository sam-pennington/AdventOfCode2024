import copy

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
   
def path_guard_looped(floor: list[list[str]]) -> tuple[list[tuple[int, int]], bool]:
    steps: list[tuple[int, int]] = []

    guard_position: tuple[int, int] = find_start(floor)
    assert(guard_position is not None)
    guard_direction: int = DIRECTION_NORTH

    extents: tuple[int, int] = get_extents(floor)

    next_step: tuple[int, int] = None

    aborted: bool = False
    while ((next_step is None) or (in_bounds(extents, next_step))) and not aborted:
        if next_step is not None: 
            steps.append(next_step)
            guard_position = next_step
        next_step, guard_direction = calculate_step(floor, extents, guard_position, guard_direction)
        if len(steps) > 100000:
            aborted = True

    return (steps, aborted)

def add_obstruction(floor: list[list[str]], position: tuple[int, int]) -> list[list[str]]:
    copied: list[list[str]] = copy.deepcopy(floor)
    if not copied[position[0]][position[1]] == '#':
        copied[position[0]][position[1]] = '#'
        return copied
    return None
    
def main() -> None:
    """ One small step beyond totally naive, get the initial route and then use that as the set of potential positions for obstructions """
    
    floor: list[list[str]] = load('puzzle-input-2.txt')

    guard_position: tuple[int, int] = find_start(floor)
    direct_front: tuple[int, int] = (guard_position[0] + MOVE_NORTH[0], guard_position[1] + MOVE_NORTH[1])

    initial_path_steps: list[tuple[int, int]] = []
    initial_path_steps, _ = path_guard_looped(floor)
    initial_path_steps = set(initial_path_steps)
    max_iterations: int = len(initial_path_steps)

    looped: list[tuple[int, int]] = []

    iterations: int = 0

    for step in initial_path_steps:
        iterations = iterations + 1
        if iterations % 10 == 0:
            print(f"Iteration: {iterations} of {max_iterations}", end="\r")

        row_modify: int = step[0]
        col_modify: int = step[1]

        # Direct in front of the guard or the guard itself
        if (row_modify == direct_front[0] and col_modify == direct_front[1]) or (row_modify == guard_position[0] and col_modify == guard_position[1]):
            continue

        modified_floor: list[list[str]] = add_obstruction(floor, (row_modify, col_modify))
        if modified_floor is not None:
            if path_guard_looped(modified_floor)[1]:
                looped.append((row_modify, col_modify))

    print(f"Iteration: {max_iterations} of {max_iterations}", end="\r")
    print()
    print(f"There are {len(looped)} positions for loops")


if __name__ == "__main__":
    main()