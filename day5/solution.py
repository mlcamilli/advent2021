import numpy as np


def get_points(line, diagonal=False):
    parts = line.split(" -> ")
    x1, y1 = (int(val) for val in parts[0].split(","))
    x2, y2 = (int(val) for val in parts[1].split(","))
    if x1 == x2:
        lesser, greater = (y1, y2) if y2 > y1 else (y2, y1)
        return [(x1, y) for y in range(lesser, greater + 1)]
    elif y1 == y2:
        lesser, greater = (x1, x2) if x2 > x1 else (x2, x1)
        return [(x, y1) for x in range(lesser, greater + 1)]
    else:
        # Slope is one so both values will increase by 1
        if diagonal:
            if x1 > x2:
                xpoints = range(x2, x1 + 1)
                xpoints = reversed(xpoints)
            else:
                xpoints = range(x1, x2 + 1)
            if y1 > y2:
                ypoints = range(y2, y1 + 1)
                ypoints = reversed(ypoints)
            else:
                ypoints = range(y1, y2 + 1)
            return zip(xpoints, ypoints)
        else:
            return []


def get_lines():
    with open("input", "r") as f:
        lines = f.readlines()
    grid = np.full((999, 999), 0)
    # grid = np.full((10, 10), 0)
    for line in lines:
        points = get_points(line, True)
        for point in points:
            grid[point[1]][point[0]] += 1
    overlap = len(np.where(grid > 1)[0])
    print(f"{overlap} overlapping points")


if __name__ == "__main__":
    get_lines()
