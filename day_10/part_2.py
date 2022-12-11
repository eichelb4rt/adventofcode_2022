import numpy as np

CRT_WIDTH = 40
CRT_HEIGHT = 6


class CPU:
    def __init__(self) -> None:
        self.x = 1
        self.current_cycle = 1
        self.signal_stength_sum = 0
        # y, x
        self.pixels = np.empty((CRT_HEIGHT, CRT_WIDTH), dtype=str)

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
        self.draw()
        self.current_cycle += 1

    def draw(self):
        pixel = self.current_cycle - 1
        y = pixel // CRT_WIDTH
        x = pixel % CRT_WIDTH
        # the sprite reaches from self.x - 1 to self.x + 1
        if x >= self.x - 1 and x <= self.x + 1:
            self.pixels[y, x] = '#'
        else:
            self.pixels[y, x] = '.'

    def current_signal_strength(self) -> int:
        return self.current_cycle * self.x

    def crt(self) -> str:
        return "\n".join(["".join(row) for row in self.pixels])


def crt(input_file: str) -> str:
    with open(input_file, 'r') as f:
        program = f.read().splitlines()
    cpu = CPU()
    cpu.run(program)
    return cpu.crt()


def main():
    test_output = crt("test_input.txt")
    print(f"Test CRT display:\n{test_output}")
    answer = crt("input.txt")
    print(f"CRT display:\n{answer}")


if __name__ == "__main__":
    main()
