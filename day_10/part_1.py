class CPU:
    def __init__(self) -> None:
        self.x = 1
        self.current_cycle = 1
        self.signal_stength_sum = 0

    def run(self, program: list[str]):
        # give me the next instruction
        for instruction in program:
            # read the instruction
            if instruction.startswith('noop'):
                self.noop()
            elif instruction.startswith('addx'):
                argument = int(instruction.split(" ")[1])
                self.addx(argument)

    def noop(self):
        self.cycle()

    def addx(self, v: int):
        self.cycle()
        self.cycle()
        self.x += v

    def cycle(self):
        if self.current_cycle % 40 == 20:
            self.signal_stength_sum += self.current_signal_strength()
        self.current_cycle += 1

    def current_signal_strength(self) -> int:
        return self.current_cycle * self.x


def signal_strength_sum(input_file: str) -> int:
    with open(input_file, 'r') as f:
        program = f.read().splitlines()
    cpu = CPU()
    cpu.run(program)
    return cpu.signal_stength_sum


def main():
    assert signal_strength_sum("test_input.txt") == 13140
    answer = signal_strength_sum("input.txt")
    print(f"The sum of the signal strengths is: {answer}")


if __name__ == "__main__":
    main()
