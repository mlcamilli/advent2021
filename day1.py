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


if __name__ == "__main__":
    get_increases()
