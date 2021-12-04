#!/usr/bin/env python3
from collections import defaultdict

loc = 0
count_of_each_line = defaultdict(int)
gamma_rate = ""
epsilon_rate = ""


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f.readlines():
            loc += 1
            for i, num in enumerate(line[:-1]):
                count_of_each_line[i] += int(num)

    loc //= 2

    for cnt in count_of_each_line.values():
        if cnt <= loc:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
