import os


def get_bags(input_text: str) -> list[list[int]]:
    elves_bags_str: list[str] = input_text.split(os.linesep * 2)
    return [[int(item) for item in bag.split(os.linesep)] for bag in elves_bags_str]


def get_top_three(input_file: str) -> int:
    with open(input_file, 'r') as f:
        lines = f.read()
    bags = get_bags(lines)
    calories: list[int] = sorted([sum(bag) for bag in bags])
    return sum(calories[-3:])


def main():
    assert get_top_three("test_input.txt") == 45000
    answer = get_top_three("input.txt")
    print(f"The top 3 elves carry {answer} calories.")


if __name__ == "__main__":
    main()
