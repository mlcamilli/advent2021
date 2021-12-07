import numpy as np


def get_alignment():
    with open("input", "r") as f:
        data = f.read()
    xpoints = np.array([int(i) for i in data.strip().split(",")])

    solutions = []
    for median in range(max(xpoints)):
        solutions.append(fuel_v2(xpoints, median))
    print(f"{str(min(solutions))} minimum fuel")


def fuel(points, median):
    return sum(abs(points - median))


def fuel_v2(points, median):
    value = abs(points - median)
    return sum((value * (value + 1)) / 2)


if __name__ == "__main__":
    get_alignment()
