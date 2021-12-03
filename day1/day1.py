def get_increases():
    with open("day1.txt", "r") as f:
        text = f.read()
        values = text.split("\n")
        increases = 0
        for i, val in enumerate(values):
            if i == 0 or not (val):
                continue
            if int(val) > int(values[i - 1]):
                increases += 1
        print(f"{increases} total increases.")


def get_thruple_increases():
    with open("day1.txt", "r") as f:
        text = f.read()
        raw_values = text.split("\n")
        values = [val for val in raw_values if val]
        increases = 0
        thruples = []
        for i in range(0, len(values)):
            if i > len(values) - 3:
                break
            total_val = sum([int(val) for val in values[i : i + 3]])
            thruples.append(total_val)

        for i, val in enumerate(thruples):
            if i == 0 or not (val):
                continue
            if int(val) > int(thruples[i - 1]):
                increases += 1
        print(f"{increases} total increases.")


if __name__ == "__main__":
    get_thruple_increases()
