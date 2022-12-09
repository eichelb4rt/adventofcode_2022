import numpy as np
from enum import Enum


class Directions(Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3


def iteration_order(grid_width: int, grid_height: int, direction: Directions) -> list[list[tuple[int, int]]]:
    """Returns the list of indices that represents the iteration order."""

    if direction == Directions.EAST:
        return [[(i, j) for j in range(grid_width)] for i in range(grid_height)]
    if direction == Directions.WEST:
        return [[(i, j) for j in reversed(range(grid_width))] for i in range(grid_height)]
    if direction == Directions.NORTH:
        return [[(i, j) for i in range(grid_height)] for j in range(grid_width)]
    if direction == Directions.SOUTH:
        return [[(i, j) for i in reversed(range(grid_height))] for j in range(grid_width)]


def visible_from(grid: np.ndarray[int], direction: Directions) -> np.ndarray[bool]:
    """Returns a bool map of which trees are visible from `direction`."""

    visible = np.full(grid.shape, False)
    grid_height, grid_width = grid.shape
    iterations = iteration_order(grid_width, grid_height, direction)
    for tree_line in iterations:
        # we haven't seen a tree in that line yet
        max_height = -1
        for tree_pos in tree_line:
            tree_height = grid[tree_pos]
            # all trees in that line are shorter than the current tree
            if max_height < tree_height:
                visible[tree_pos] = True
                max_height = tree_height
    return visible


def visible_trees(input_file: str) -> int:
    with open(input_file, 'r') as f:
        grid_str = f.read()
    grid = np.array([[
        int(height) for height in line
    ] for line in grid_str.splitlines()])

    # trees that are visible from any direction
    visible_grid = np.any([
        visible_from(grid, Directions.EAST),
        visible_from(grid, Directions.WEST),
        visible_from(grid, Directions.NORTH),
        visible_from(grid, Directions.SOUTH)
    ], axis=0)

    # count how many trees are visible
    return np.count_nonzero(visible_grid)


def main():
    assert visible_trees("test_input.txt") == 21
    answer = visible_trees("input.txt")
    print(f"The number of visible trees is: {answer}")


if __name__ == "__main__":
    main()
