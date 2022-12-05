import os

def main():
    with open("input.txt", 'r') as f:
        input_text = f.read()
    elves_bags_str: list[str] = input_text.split(os.linesep * 2)
    elves_bags_int: list[list[int]] = [[int(item) for item in bag.split(os.linesep)] for bag in elves_bags_str]
    elves_total_calories: list[int] = [sum(bag) for bag in elves_bags_int]
    max_calories = max(elves_total_calories)
    print(f"The elf with the highest calories carries {max_calories} calories.")

if __name__ == "__main__":
    main()