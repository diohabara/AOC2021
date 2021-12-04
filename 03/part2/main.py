#!/usr/bin/env python3
from collections import defaultdict


def get_list_of_numbers():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


def get_most_frequent_bit(lis):
    cnt0 = lis.count("0")
    cnt1 = lis.count("1")
    if cnt0 <= cnt1:
        return "1"
    else:
        return "0"


def get_least_frequent_bit(lis):
    cnt0 = lis.count("0")
    cnt1 = lis.count("1")
    if cnt0 <= cnt1:
        return "0"
    else:
        return "1"


def calculate_oxygen_generator_rating():
    idx = 0
    numbers = get_list_of_numbers()
    while 1 < len(numbers) and idx < len(numbers[0]):
        most_bit = get_most_frequent_bit([n[idx] for n in numbers])
        remain_set = set([i for i, n in enumerate(numbers) if n[idx] == most_bit])
        numbers = [n for i, n in enumerate(numbers) if i in remain_set]
        idx += 1
    return numbers[0]


def calculate_co2_scrubber_rating():
    idx = 0
    numbers = get_list_of_numbers()
    while 1 < len(numbers) and idx < len(numbers[0]):
        least_bit = get_least_frequent_bit([n[idx] for n in numbers])
        remain_set = set([i for i, n in enumerate(numbers) if n[idx] == least_bit])
        numbers = [n for i, n in enumerate(numbers) if i in remain_set]
        idx += 1
    return numbers[0]


if __name__ == "__main__":
    oxygen = int(calculate_oxygen_generator_rating(), 2)
    co2 = int(calculate_co2_scrubber_rating(), 2)
    print(oxygen * co2)
