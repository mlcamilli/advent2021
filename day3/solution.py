from collections import Counter

import numpy as np


def get_power_consumption():
    with open("input", "r") as f:
        array = np.array([[bit for bit in row] for row in f.read().split("\n") if row])
        gamma_array = []
        epsilon_array = []
        for column in array.T:
            count = Counter(column)
            if count["0"] > count["1"]:
                gamma_array.append("0")
                epsilon_array.append("1")
            else:
                gamma_array.append("1")
                epsilon_array.append("0")
        gamma_string = "".join(gamma_array)
        epsilon_string = "".join(epsilon_array)
        gamma_rate = int(gamma_string, 2)
        epsilon_rate = int(epsilon_string, 2)
        print(
            f"Gamma: {gamma_string} {gamma_rate} | Epsilon: {epsilon_string} {epsilon_rate} | Power Consumption {epsilon_rate * gamma_rate}"
        )


def get_mode(count):
    if count["1"] >= count["0"]:
        return "1"
    else:
        return "0"


def get_life_support_rating():
    with open("input", "r") as f:
        co2 = oxygen = array = np.array([[bit for bit in row] for row in f.read().split("\n") if row])
        for i in range(0, len(array.T)):
            oxy_count = Counter(oxygen.T[i])
            co2_count = Counter(co2.T[i])
            if len(oxygen) != 1:
                oxygen = oxygen[(oxygen[:, i] == get_mode(oxy_count))]
            if len(co2) != 1:
                co2 = co2[(co2[:, i] != get_mode(co2_count))]
        co2_rating = int("".join(co2[0]), 2)
        oxygen_rating = int("".join(oxygen[0]), 2)
        print(f"CO2 Rating {co2_rating} \nOxy rating {oxygen_rating} \nLife Support Rating: {co2_rating*oxygen_rating}")


if __name__ == "__main__":
    get_life_support_rating()
