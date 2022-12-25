import ast
import functools
import numpy as np

DIVIDER_PACKETS = [
    [[2]],
    [[6]]
]


def correct_order(left: list | int, right: list | int) -> int:
    # both ints
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        if left > right:
            return 1
        return 0
    # both lists
    if type(left) == list and type(right) == list:
        min_len = min(len(left), len(right))
        for i in range(min_len):
            ordered = correct_order(left[i], right[i])
            # inputs are the same, continue with next input
            if ordered == 0:
                continue
            # we got a result, pass down that result
            return ordered
        # at least 1 side ran out of items
        # left side ran out of items
        if len(left) < len(right):
            return -1
        # right side ran out of items
        if len(left) > len(right):
            return 1
        # lists are same length and no comparison makes decision about order
        return 0
    # 1 int, 1 list
    else:
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return correct_order(left, right)


def decoder_key(input_file: str) -> int:
    with open(input_file, 'r') as f:
        packets_str = f.read().replace("\n\n", "\n").splitlines()
    packets = [ast.literal_eval(packet_str) for packet_str in packets_str]
    # add divider packets
    packets += DIVIDER_PACKETS
    packets.sort(key=functools.cmp_to_key(correct_order))
    divider_positions = [idx for idx, packet in enumerate(packets, 1) if packet in DIVIDER_PACKETS]
    return np.prod(divider_positions)


def main():
    assert decoder_key("test_input.txt") == 140
    answer = decoder_key("input.txt")
    print(f"Sum of correct indices: {answer}")


if __name__ == "__main__":
    main()
