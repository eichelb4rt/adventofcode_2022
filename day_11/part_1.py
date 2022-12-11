from typing import Callable, Self


N_ROUNDS = 20
RELIEF_DIVISOR = 3


class Monkey:
    def __init__(self, starting_items: list[int], operation: Callable[[int], int], test: Callable[[int], bool], test_true: int, test_false: int) -> None:
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspections = 0

    def throw_all(self) -> list[tuple[int, int]]:
        """Returns a list with entries `(thrown_item, thrown_to)`. Also empties the current item list."""

        thrown = [self.throw(item) for item in self.items]
        self.items = []
        return thrown

    def throw(self, worry: int) -> tuple[int, int]:
        """Returns the worry level before throwing and the monkey the item is thrown to."""

        self.inspections += 1
        worry = self.operation(worry)
        worry //= RELIEF_DIVISOR
        if self.test(worry):
            throw_to = self.test_true
        else:
            throw_to = self.test_false
        return worry, throw_to

    def receive(self, item: int):
        self.items.append(item)

    @classmethod
    def from_encoding(cls, encoding: str) -> Self:
        lines = encoding.splitlines()
        # monkey number is in first line
        current_line = 0
        # starting items
        current_line += 1
        offset = len("  Starting items: ")
        starting_items = [int(item) for item in lines[current_line][offset:].split(", ")]
        # operation
        current_line += 1
        offset = len("  Operation: new = ")
        operand_1, operation_char, operand_2 = lines[current_line][offset:].split(" ")
        if operation_char == '*':
            operation = lambda old: (old if operand_1 == "old" else int(operand_1)) * (old if operand_2 == "old" else int(operand_2))
        elif operation_char == '+':
            operation = lambda old: (old if operand_1 == "old" else int(operand_1)) + (old if operand_2 == "old" else int(operand_2))
        # test
        current_line += 1
        offset = len("  Test: divisible by ")
        divisible_by = int(lines[current_line][offset:])
        test = lambda worry: worry % divisible_by == 0
        # if test is true
        current_line += 1
        offset = len("    If true: throw to monkey ")
        if_true = int(lines[current_line][offset:])
        # if test is false
        current_line += 1
        offset = len("    If false: throw to monkey ")
        if_false = int(lines[current_line][offset:])

        return Monkey(starting_items, operation, test, if_true, if_false)

    def __str__(self) -> str:
        return f"Items: {', '.join([str(item) for item in self.items])}"


def round(monkeys: list[Monkey]):
    for monkey in monkeys:
        thrown = monkey.throw_all()
        for item, thrown_to in thrown:
            monkeys[thrown_to].receive(item)


def monkey_business(input_file: str) -> int:
    # read monkeys
    with open(input_file, 'r') as f:
        monkey_encodings = f.read().split("\n\n")
    monkeys = [Monkey.from_encoding(encoding) for encoding in monkey_encodings]
    # play keep away
    for _ in range(N_ROUNDS):
        round(monkeys)
    # see who the most busy monkeys were
    inspections = sorted([monkey.inspections for monkey in monkeys])
    return inspections[-1] * inspections[-2]


def main():
    assert monkey_business("test_input.txt") == 10605
    answer = monkey_business("input.txt")
    print(f"Monkey business: {answer}")


if __name__ == "__main__":
    main()
