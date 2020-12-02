import pandas as pd
import numpy as np
import time
f = open("AOC2020/input_2.txt", "r")

def part_one():
    valid_ctr = 0
    for line in f:
        l = line.split(":")
        password = l[1]
        rules = l[0]
        r = rules.split(" ")
        ch = r[1]
        nums = [int(n) for n in r[0].split("-")]
        occurances = password.count(ch)
        if (occurances >= nums[0]) & (occurances <= nums[1]):
            valid_ctr += 1

    print(valid_ctr)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def part_two():
    valid_ctr = 0
    for line in f:
        l = line.split(":")
        password = l[1].strip()
        rules = l[0]
        r = rules.split(" ")
        ch = r[1]
        nums = [int(n) for n in r[0].split("-")]
        positions = find(password, ch)
        positions = [(p + 1) for p in positions]
        common_positions = list(set(nums).intersection(positions))

        if len(common_positions) == 1:
            #print(nums, common_positions, ch, password)
            valid_ctr += 1
    print(valid_ctr)


def __main__():
    start = time.time()

    part_one()
    part_two()

    end = time.time()
    print("Time: ", end - start)