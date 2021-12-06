import threading
from collections import Counter

import numpy as np


# Rcursive solution that is wildly too slow
def fish_count(days_left, new=True):
    if new:
        if days_left >= 9:
            return fish_count(days_left - 9, new=False) + fish_count(days_left - 9, new=True)
        else:
            return 1
    else:
        if days_left >= 7:
            return fish_count(days_left - 7, new=False) + fish_count(days_left - 7, new=True)
        else:
            return 1


def get_chunks(size, buckets):
    indices = []
    if size < buckets:
        return [(0, size)]
    bucket_size, remainder = divmod(size, buckets)
    for i in range(0, buckets):
        end = (i + 1) * bucket_size
        if i == buckets - 1:
            end += remainder
        indices.append((i * bucket_size, end))
    return indices


def count_lanternfish():
    TOTAL_DAYS = 200
    NUM_THREADS = 10
    with open("input", "r") as f:
        data = f.read()
    fish = [int(f.strip()) for f in data.split(",") if f]
    for i in range(0, TOTAL_DAYS):
        fish_to_add = []

        def process_fish(start, finish):
            for n in range(start, finish):
                if fish[n] == 0:
                    fish_to_add.append(8)
                    fish[n] = 6
                else:
                    fish[n] -= 1

        threads = []

        fish_buckets = get_chunks(len(fish), NUM_THREADS)
        for bucket in fish_buckets:
            x = threading.Thread(target=process_fish, args=(bucket[0], bucket[1]))
            threads.append(x)
            x.start()
        for thread in threads:
            thread.join()

        fish.extend(fish_to_add)
        print(f"Day {i}, {len(fish)} total fish, {len(fish_to_add)} added fish")
    print(f"{TOTAL_DAYS} total days, {len(fish)} total fish")
    # print(",".join(str(f) for f in fish))


def better_solution():
    TOTAL_DAYS = 256
    with open("input", "r") as f:
        data = f.read()
    fish = Counter(int(f.strip()) for f in data.split(",") if f)
    for day in range(0, TOTAL_DAYS):
        new_fish = fish[0]
        for state in range(0, 8):
            fish[state] = fish[state + 1]
        fish[8] = new_fish
        fish[6] += new_fish
    print(f"{TOTAL_DAYS} total days, {sum(fish.values())} total fish")


if __name__ == "__main__":
    better_solution()
