START_OF_MESSAGE_LENGTH = 14


def start_of_message(input_file: str) -> int:
    with open(input_file, 'r') as f:
        datastream = f.read().rstrip()

    for i in range(START_OF_MESSAGE_LENGTH, len(datastream) + 1):
        # i = 14 -> datastream[0, 1, 2, ..., 13]
        buffer = datastream[i - START_OF_MESSAGE_LENGTH:i]
        # if all letters are unique
        if len(set(buffer)) == START_OF_MESSAGE_LENGTH:
            return i
    # if no start is found, return -1
    return -1


def main():
    assert start_of_message("test_input_1.txt") == 19
    assert start_of_message("test_input_2.txt") == 23
    assert start_of_message("test_input_3.txt") == 23
    assert start_of_message("test_input_4.txt") == 29
    assert start_of_message("test_input_5.txt") == 26
    answer = start_of_message("input.txt")
    print(f"The number of characters processed before the first start-of-message marker is {answer}.")


if __name__ == "__main__":
    main()
