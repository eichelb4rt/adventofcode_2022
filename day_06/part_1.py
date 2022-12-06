START_OF_SIGNAL_LENGTH = 4


def start_of_signal(input_file: str) -> int:
    with open(input_file, 'r') as f:
        datastream = f.read().rstrip()

    for i in range(START_OF_SIGNAL_LENGTH, len(datastream) + 1):
        # start = 4 -> datastream[0, 1, 2, 3]
        buffer = datastream[i - START_OF_SIGNAL_LENGTH:i]
        # if all letters are unique
        if len(set(buffer)) == START_OF_SIGNAL_LENGTH:
            return i
    # if no start is found, return -1
    return -1


def main():
    assert start_of_signal("test_input_1.txt") == 7
    assert start_of_signal("test_input_2.txt") == 5
    assert start_of_signal("test_input_3.txt") == 6
    assert start_of_signal("test_input_4.txt") == 10
    assert start_of_signal("test_input_5.txt") == 11
    answer = start_of_signal("input.txt")
    print(f"The number of characters processed before the first start-of-packet marker is {answer}.")


if __name__ == "__main__":
    main()
