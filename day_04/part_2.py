def get_pairings(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines]


def get_sections(shift: str) -> tuple[int, int]:
    """Gets start and end sections of a shift."""

    sections = shift.split("-")
    return int(sections[0]), int(sections[1])


def contains(shift: str, section: int) -> bool:
    """Checks if `section` is contained in `shift`."""

    shift_start, shift_end = get_sections(shift)
    return section >= shift_start and section <= shift_end


def overlapping(pairing: str) -> bool:
    shift_1, shift_2 = pairing.split(",")
    shift_1_start, shift_1_end = get_sections(shift_1)
    shift_2_start, shift_2_end = get_sections(shift_2)
    return contains(shift_2, shift_1_start) or contains(shift_2, shift_1_end) \
        or contains(shift_1, shift_2_start) or contains(shift_1, shift_2_end)


def n_overlap(input_file: str) -> int:
    with open(input_file, 'r') as f:
        pairings = get_pairings(f.readlines())
    return sum([overlapping(pairing) for pairing in pairings])


def main():
    assert n_overlap("test_input.txt") == 4
    answer = n_overlap("input.txt")
    print(f"There are {answer} pairings where one shift is fully contained in the other.")


if __name__ == "__main__":
    main()
