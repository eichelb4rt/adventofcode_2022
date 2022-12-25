import ast
from typing import Optional


def correct_order(left: list | int, right: list | int) -> Optional[bool]:
    # both ints
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    # both lists
    if type(left) == list and type(right) == list:
        min_len = min(len(left), len(right))
        for i in range(min_len):
            ordered = correct_order(left[i], right[i])
            # inputs are the same, continue with next input
            if ordered is None:
                continue
            # we got a result, pass down that result
            return ordered
        # at least 1 side ran out of items
        # left side ran out of items
        if len(left) < len(right):
            return True
        # right side ran out of items
        if len(left) > len(right):
            return False
        # lists are same length and no comparison makes decision about order
        return None
    # 1 int, 1 list
    else:
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return correct_order(left, right)


def indices_correct_sum(input_file: str) -> int:
    with open(input_file, 'r') as f:
        packets_str = [packet.splitlines() for packet in f.read().split("\n\n")]
    packets = [(ast.literal_eval(left), ast.literal_eval(right)) for left, right in packets_str]

    correct_indices = [idx for idx, packet in enumerate(packets, 1) if correct_order(*packet)]
    return sum(correct_indices)


def main():
    assert indices_correct_sum("test_input.txt") == 13
    answer = indices_correct_sum("input.txt")
    print(f"Sum of correct indices: {answer}")


if __name__ == "__main__":
    main()
