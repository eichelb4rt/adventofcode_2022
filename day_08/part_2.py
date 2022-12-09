import itertools
import numpy as np
from enum import Enum


class Directions(Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3


def iteration_order(grid_width: int, grid_height: int, position: tuple[int, int], direction: Directions) -> list[tuple[int, int]]:
    """Returns the list of indices that represents the iteration order."""

    position_i, position_j = position
    if direction == Directions.EAST:
        # go forward by 1 until the end of the array
        return [(position_i, j) for j in range(position_j + 1, grid_width)]
    if direction == Directions.WEST:
        # go back by 1 until the start of the array
        return [(position_i, j) for j in range(position_j - 1, -1, -1)]
    if direction == Directions.NORTH:
        # go forward by 1 until the end of the array
        return [(i, position_j) for i in range(position_i + 1, grid_height)]
    if direction == Directions.SOUTH:
        # go back by 1 until the start of the array
        return [(i, position_j) for i in range(position_i - 1, -1, -1)]


def viewing_distance(grid: np.ndarray[int], position: tuple[int, int], direction: Directions) -> int:
    grid_height, grid_width = grid.shape
    own_height = grid[position]

    seen_trees = 0
    tree_line = iteration_order(grid_width, grid_height, position, direction)
    for tree_pos in tree_line:
        # we can see the tree because we could see over all the trees before
        seen_trees += 1
        tree_height = grid[tree_pos]
        # if a tree is >= our tree, that's all the trees we can see.
        if tree_height >= own_height:
            break
    return seen_trees


def scenic_score(grid: np.ndarray[int], position: tuple[int, int]) -> int:
    return np.prod([
        viewing_distance(grid, position, Directions.EAST),
        viewing_distance(grid, position, Directions.WEST),
        viewing_distance(grid, position, Directions.NORTH),
        viewing_distance(grid, position, Directions.SOUTH)
    ])


def max_scenic_score(input_file: str) -> int:
    with open(input_file, 'r') as f:
        grid_str = f.read()
    grid = np.array([[
        int(height) for height in line
    ] for line in grid_str.splitlines()])

    # calculate scenic score for every tree
    scenic_scores = np.empty(grid.shape, dtype=int)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            scenic_scores[i, j] = scenic_score(grid, position=(i, j))

    # find the best one
    return np.max(scenic_scores)


def main():
    assert max_scenic_score("test_input.txt") == 8
    answer = max_scenic_score("input.txt")
    print(f"The number of visible trees is: {answer}")


if __name__ == "__main__":
    main()
