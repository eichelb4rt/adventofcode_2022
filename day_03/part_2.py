def get_rucksacks(lines: list[str]) -> list[str]:
    # get rid of line breaks and empty lines
    return [line.rstrip() for line in lines if not len(line) == 0]

def get_groups(rucksacks: list[str]) -> list[tuple[str, str, str]]:
    return [(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]) for i in range(0, len(rucksacks), 3)]

def find_badge(group: list[str]) -> str:
    elf_1 = set(group[0])
    elf_2 = set(group[1])
    elf_3 = set(group[2])
    common_items = elf_1.intersection(elf_2).intersection(elf_3)
    # there is exactly 1 common item for the whole group
    return list(common_items)[0]

def priority(mistake: str) -> int:
    if mistake.islower():
        return ord(mistake) - ord('a') + 1
    else:
        return ord(mistake) - ord('A') + 27

def sum_priorities(input_file: str) -> int:
    with open(input_file, 'r') as f:
        rucksacks = get_rucksacks(f.readlines())
    groups = get_groups(rucksacks)
    badges = [find_badge(group) for group in groups]
    priorities = [priority(badge) for badge in badges]
    return sum(priorities)

def main():
    assert sum_priorities("test_input.txt") == 70
    answer = sum_priorities("input.txt")
    print(f"The sum of the priorities is {answer}.")

if __name__ == "__main__":
    main()