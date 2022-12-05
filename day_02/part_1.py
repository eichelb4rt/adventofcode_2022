OUTCOME = {
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('C', 'Y'): 0,
    ('A', 'X'): 3,
    ('B', 'Y'): 3,
    ('C', 'Z'): 3,
    ('A', 'Y'): 6,
    ('B', 'Z'): 6,
    ('C', 'X'): 6
}

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def get_matches(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines]


def score(match: str) -> int:
    # match is in format: `A X`
    enemy_shape = match[0]
    player_shape = match[-1]
    return SHAPE_SCORE[player_shape] + OUTCOME[(enemy_shape, player_shape)]


def total_score(input_file: str) -> int:
    with open(input_file, 'r') as f:
        matches = get_matches(f.readlines())
    total_score = sum([score(match) for match in matches])
    return total_score


def main():
    assert total_score("test_input.txt") == 15
    answer = total_score("input.txt")
    print(f"Resulting score is {answer}.")


if __name__ == "__main__":
    main()
