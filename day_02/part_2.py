# A < B < C < A

OUTCOME_SCORE = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

CORRECT_SHAPE = {
    ('A', 'X'): 'C',
    ('A', 'Y'): 'A',
    ('A', 'Z'): 'B',
    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A',
}

SHAPE_SCORE = {
    'A': 1,
    'B': 2,
    'C': 3
}


def get_matches(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines]


def score(match: str) -> int:
    # match is in format: `A X`
    enemy_shape = match[0]
    outcome = match[-1]
    player_shape = CORRECT_SHAPE[(enemy_shape, outcome)]
    return SHAPE_SCORE[player_shape] + OUTCOME_SCORE[outcome]


def total_score(input_file: str) -> int:
    with open(input_file, 'r') as f:
        matches = get_matches(f.readlines())
    total_score = sum([score(match) for match in matches])
    return total_score


def main():
    assert total_score("test_input.txt") == 12
    answer = total_score("input.txt")
    print(f"Resulting score is {answer}.")


if __name__ == "__main__":
    main()
