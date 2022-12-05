import os


def get_bags(input_text: str) -> list[list[int]]:
    elves_bags_str: list[str] = input_text.split(os.linesep * 2)
    return [[int(item) for item in bag.split(os.linesep)] for bag in elves_bags_str]


def get_max_calories(input_file: str) -> int:
    with open(input_file, 'r') as f:
        lines = f.read()
    bags = get_bags(lines)
    calories: list[int] = [sum(bag) for bag in bags]
    return max(calories)


def main():
    assert get_max_calories("test_input.txt") == 24000
    answer = get_max_calories("input.txt")
    print(f"The elf with the highest calories carries {answer} calories.")


if __name__ == "__main__":
    main()
