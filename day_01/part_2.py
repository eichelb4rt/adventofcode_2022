import os

def main():
    with open("input.txt", 'r') as f:
        input_text = f.read()
    elves_bags_str: list[str] = input_text.split(os.linesep * 2)
    elves_bags_int: list[list[int]] = [[int(item) for item in bag.split(os.linesep)] for bag in elves_bags_str]
    elves_total_calories: list[int] = sorted([sum(bag) for bag in elves_bags_int])
    top_three = sum(elves_total_calories[-3:])
    print(f"The top 3 elves carry {top_three} calories.")

if __name__ == "__main__":
    main()