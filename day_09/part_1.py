import numpy as np
from enum import Enum


N_DIMENSIONS = 2


class Directions(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


# direction and number of steps in that direction
Move = tuple[Directions, int]


def to_move(line: str) -> Move:
    direction, steps = line.split(" ")
    return (Directions(direction), int(steps))


def pull_tail(head_pos: np.ndarray, tail_pos: np.ndarray) -> None:
    diff = head_pos - tail_pos
    # if we're still touching, don't move the tail
    if np.all(np.abs(diff) <= 1):
        return
    # move max of 1 for every direction where we're different
    tail_pos += np.sign(diff)


def move_head(head_pos: np.ndarray, direction: Directions) -> None:
    # positions stored as [x, y]
    if direction == Directions.LEFT:
        head_pos[0] -= 1
    elif direction == Directions.RIGHT:
        head_pos[0] += 1
    elif direction == Directions.UP:
        head_pos[1] += 1
    elif direction == Directions.DOWN:
        head_pos[1] -= 1


def n_positions_visited(input_file: str) -> int:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    moves = [to_move(line) for line in lines]

    # start stacked on (0, 0)
    head_pos = np.zeros(N_DIMENSIONS, dtype=int)
    tail_pos = head_pos.copy()

    # save positions we visited
    visited_positions: set[tuple[int, int]] = set()
    visited_positions.add(tuple(tail_pos))

    # execute the moves
    for direction, n_steps in moves:
        for _ in range(n_steps):
            move_head(head_pos, direction)
            pull_tail(head_pos, tail_pos)
            visited_positions.add(tuple(tail_pos))
    return len(visited_positions)


def main():
    assert n_positions_visited("test_input.txt") == 13
    answer = n_positions_visited("input.txt")
    print(f"Number of positions visited: {answer}")


if __name__ == "__main__":
    main()
