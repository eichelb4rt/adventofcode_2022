import numpy as np

Position = tuple[int, int]


def can_move(from_height: str, to_height: str) -> bool:
    return ord(to_height) - ord(from_height) <= 1


def in_bounds(height_map: np.ndarray[str], pos: Position) -> bool:
    return 0 <= pos[0] and 0 <= pos[1] and pos[0] < height_map.shape[0] and pos[1] < height_map.shape[1]


def get_neighbours(height_map: np.ndarray[str], current: Position) -> list[Position]:
    # neighbours in all directions
    neighbours = [
        (current[0], current[1] - 1),
        (current[0], current[1] + 1),
        (current[0] - 1, current[1]),
        (current[0] + 1, current[1])
    ]
    # filter out of bounds neighbours
    neighbours = [neighbour for neighbour in neighbours if in_bounds(height_map, neighbour)]
    # print(neighbours)
    # filter neighbours we can't move to (that are too high)
    neighbours = [neighbour for neighbour in neighbours if can_move(height_map[neighbour], height_map[current])]
    return neighbours


def shortest_path(input_file: str) -> int:
    # read the height map
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    height_map = np.array([[c for c in line] for line in lines])
    # find out where we start and destination
    start = Position(np.argwhere(height_map == 'S')[0])
    destination = Position(np.argwhere(height_map == 'E')[0])
    possible_starts = [Position(position) for position in np.argwhere((height_map == 'S') | (height_map == 'a'))]
    # assign height to start and destination
    height_map[start] = 'a'
    height_map[destination] = 'z'
    # WFS
    found: list[Position] = []
    queue: list[Position] = [destination]
    next_queue: list[Position] = []
    # track how far we've walked from the start
    distance = 0
    while True:
        # mark found nodes
        found += queue
        # append new nodes to the queue
        for node in queue:
            # stop searching if we found an 'a'
            if node in possible_starts:
                return distance
            neighbours = get_neighbours(height_map, node)
            # append unique neighbours to next_queue
            next_queue += [neighbour for neighbour in neighbours if neighbour not in next_queue and neighbour not in found]
        # prepare next step
        queue = next_queue
        next_queue = []
        distance += 1


def main():
    assert shortest_path("test_input.txt") == 29
    answer = shortest_path("input.txt")
    print(f"The least number of steps: {answer}")


if __name__ == "__main__":
    main()
