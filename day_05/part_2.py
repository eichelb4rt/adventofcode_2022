import os
from dataclasses import dataclass


Stack = list[str]


@dataclass
class Move:
    amount: int
    from_stack: int
    to_stack: int

    def __repr__(self) -> str:
        return f"move {self.amount} from {self.from_stack} to {self.to_stack}"


class Crane:
    def __init__(self, stacks: list[Stack]):
        self.stacks = stacks

    def execute(self, move: Move):
        # move the crates on a magic invisible stack
        help_stack: Stack = []
        for _ in range(move.amount):
            # stack_index is stack_id - 1
            top_crate = self.stacks[move.from_stack - 1].pop()
            help_stack.append(top_crate)
        # and move them from the magic invisible stack to the destination, so that order is kept
        for _ in range(move.amount):
            # stack_index is stack_id - 1
            top_crate = help_stack.pop()
            self.stacks[move.to_stack - 1].append(top_crate)

    def top_crates(self) -> str:
        return "".join(self.stacks[i][-1] for i in range(len(self.stacks)))


def get_stacks(stacks_encoding: str) -> list[Stack]:
    lines = stacks_encoding.splitlines()
    stack_numbers = [int(number) for number in lines[-1].split("   ")]
    # create a new stack for every stack number
    stacks: list[Stack] = [[] for _ in stack_numbers]
    # read them from bottom up
    stacks_lines = lines[:-1]
    stacks_lines.reverse()
    for line in stacks_lines:
        # push all the crates in the line on the respective stack
        for i in range(len(stacks)):
            # crate id is always at position 4 * i + 1
            crate_id = line[4 * i + 1]
            # there could be no crate at that position
            if crate_id != " ":
                stacks[i].append(crate_id)
    return stacks


def get_moves(moves_encoding: str) -> list[Move]:
    # remove move, from, to (just leave 1 space between the numbers)
    moves_encoding = moves_encoding.replace("move ", "").replace("from ", "").replace("to ", "")
    lines = moves_encoding.splitlines()
    moves_infos = [line.split(" ") for line in lines]
    return [Move(int(move_info[0]), int(move_info[1]), int(move_info[2])) for move_info in moves_infos]


def get_top(input_file: str) -> str:
    with open(input_file, 'r') as f:
        stacks_encoding, moves_encoding = f.read().split(os.linesep * 2)
    stacks = get_stacks(stacks_encoding)
    moves = get_moves(moves_encoding)

    crane = Crane(stacks)
    for move in moves:
        crane.execute(move)
    return crane.top_crates()


def main():
    assert get_top("test_input.txt") == "MCD"
    answer = get_top("input.txt")
    print(f"The crates at the top of the stacks are the following: {answer}")


if __name__ == "__main__":
    main()
