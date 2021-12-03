def get_position():
    aim = 0
    depth = 0
    horizontal = 0
    with open("input", "r") as f:
        instructions = [val for val in f.read().split("\n") if val]
        for instruction in instructions:
            command, value = instruction.split(" ")
            if command == "forward":
                horizontal += int(value)
                depth += aim * int(value)
            elif command == "down":
                aim += int(value)
            elif command == "up":
                aim -= int(value)
            else:
                raise Exception("Bad command should never happen")
    print(f"Depth {depth}, Horizontal {horizontal}, Final {horizontal * depth}")


def get_position_old():
    depth = 0
    horizontal = 0
    with open("input", "r") as f:
        instructions = [val for val in f.read().split("\n") if val]
        for instruction in instructions:
            command, value = instruction.split(" ")
            if command == "forward":
                horizontal += int(value)
            elif command == "down":
                depth += int(value)
            elif command == "up":
                depth -= int(value)
            else:
                raise Exception("Bad command should never happen")
    print(f"Depth {depth}, Horizontal {horizontal}, Final {horizontal * depth}")


if __name__ == "__main__":
    get_position()
