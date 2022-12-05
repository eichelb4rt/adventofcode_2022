def get_pairings(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines]


def get_sections(shift: str) -> tuple[int, int]:
    """Gets start and end sections of a shift."""

    sections = shift.split("-")
    return int(sections[0]), int(sections[1])


def is_contained(shift_1: str, shift_2: str) -> bool:
    """Checks if `shift_1` is contained in `shift_2`."""

    shift_1_start, shift_1_end = get_sections(shift_1)
    shift_2_start, shift_2_end = get_sections(shift_2)
    return shift_1_start >= shift_2_start and shift_1_end <= shift_2_end


def fully_contained(pairing: str) -> bool:
    shift_1, shift_2 = pairing.split(",")
    return is_contained(shift_1, shift_2) or is_contained(shift_2, shift_1)


def n_fully_contained(input_file: str) -> int:
    with open(input_file, 'r') as f:
        pairings = get_pairings(f.readlines())
    return sum([fully_contained(pairing) for pairing in pairings])


def main():
    assert n_fully_contained("test_input.txt") == 2
    answer = n_fully_contained("input.txt")
    print(f"There are {answer} pairings where one shift is fully contained in the other.")


if __name__ == "__main__":
    main()
