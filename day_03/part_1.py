def get_rucksacks(lines: list[str]) -> list[str]:
    # get rid of line breaks and empty lines
    return [line.rstrip() for line in lines]


def find_mistake(rucksack: str) -> str:
    compartment_size = len(rucksack) // 2
    compartment_1 = set(rucksack[:compartment_size])
    compartment_2 = set(rucksack[compartment_size:])
    common_items = compartment_1.intersection(compartment_2)
    # there is exactly 1 mistake in every rucksack
    return list(common_items)[0]


def priority(mistake: str) -> int:
    if mistake.islower():
        return ord(mistake) - ord('a') + 1
    else:
        return ord(mistake) - ord('A') + 27


def sum_priorities(input_file: str) -> int:
    with open(input_file, 'r') as f:
        rucksacks = get_rucksacks(f.readlines())
    mistakes = [find_mistake(rucksack) for rucksack in rucksacks]
    priorities = [priority(mistake) for mistake in mistakes]
    return sum(priorities)


def main():
    assert sum_priorities("test_input.txt") == 157
    answer = sum_priorities("input.txt")
    print(f"The sum of the priorities is {answer}.")


if __name__ == "__main__":
    main()
