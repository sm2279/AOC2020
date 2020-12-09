import pandas as pd
import numpy as np
import time
import math
import re

data = open('AOC2020/input_9.txt', 'r').read().splitlines()

data = [int(i) for i in data]

def find_sum(len1, len2, num):
    found = -1
    for i in range(len1, len2):
        if found == 1:
            break
        for j in range(len1, len2):
            if i == j:
                continue
            if found == 1:
                break
            if (data[i] + data[j]) == num:
                found = 1
                break

    if found == -1:
        return -1
    return num

def part_one():
    i = 25
    while i < len(data):
        print(data[i])
        find = find_sum(i-25, i, data[i])

        if find == -1:
            print("FOUND IT ", data[i])
            break

        i += 1

def part_two():
    i = 25
    found = 10884537
    ix = 500

    sum_set = []

    u = 0
    i = 0
    while i < len(data):
        if u == -1:
            break
        if ix == i:
            continue
        j = i
        sum_set = []
        while sum(sum_set) <= found:
            print(sum(sum_set), found)
            if sum(sum_set) == found:
                u = -1
                print("FOUND IT ", sum_set, sum(sum_set))
                break
            sum_set.append(data[j])
            j = j + 1
        i = i + 1

    print(min(sum_set), max(sum_set), min(sum_set) + max(sum_set))

part_two()

