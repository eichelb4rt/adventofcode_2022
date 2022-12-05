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


def score(match: str) -> int:
    # match is a line in format: `A X\n`.
    match = match.rstrip()
    # ignore empty lines
    if len(match) == 0:
        return 0
    enemy_shape = match[0]
    player_shape = match[-1]
    return SHAPE_SCORE[player_shape] + OUTCOME[(enemy_shape, player_shape)]


def total_score(input_file: str) -> int:
    with open(input_file, 'r') as f:
        matches = f.readlines()
    total_score = sum([score(match) for match in matches])
    return total_score

def main():
    assert total_score("test_input.txt") == 15
    answer = total_score("input.txt")
    print(f"Resulting score is {answer}.")


if __name__ == "__main__":
    main()
