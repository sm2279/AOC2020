import pandas as pd
import numpy as np
import time
import math
import re

pd.set_option('display.max_rows', None)


f = open("AOC2020/input_5.txt", "r")
input_ = [i.rstrip() for i in f]

def get_id(code):
    rows = [i for i in range(0, 128)]
    for c in range(0, 6):
        if code[c] == 'B':
            rows = [i for i in rows if i >= math.ceil((min(rows) + max(rows))/2)]
        if code[c] == 'F':
            rows = [i for i in rows if i < math.ceil((min(rows) + max(rows))/2)]

    if code[6] == 'F':
        row = min(rows)
    elif code[6] == 'B':
        row = max(rows)

    cols = [i for i in range(0, 8)]
    for c in range(7, len(code)):
        if code[c] == 'L':
            cols = [i for i in cols if i < math.ceil((min(cols) + max(cols))/2)]
        if code[c] == 'R':
            cols = [i for i in cols if i >= math.ceil((min(cols) + max(cols)) / 2)]
    if code[9] == 'L':
        col = min(cols)
    elif code[9] == 'R':
        col = max(cols)

    id = row * 8
    id = id + col

    return id

def part_one():
    max_id = 0
    for i in input_:
        cur_id = get_id(i)
        if cur_id > max_id:
            max_id = cur_id
    print(max_id)

def find_seat(code):
    rows = [i for i in range(0, 128)]
    for c in range(0, 6):
        if code[c] == 'B':
            rows = [i for i in rows if i >= math.ceil((min(rows) + max(rows))/2)]
        if code[c] == 'F':
            rows = [i for i in rows if i < math.ceil((min(rows) + max(rows))/2)]

    if code[6] == 'F':
        row = min(rows)
    elif code[6] == 'B':
        row = max(rows)

    cols = [i for i in range(0, 8)]
    for c in range(7, len(code)):
        if code[c] == 'L':
            cols = [i for i in cols if i < math.ceil((min(cols) + max(cols))/2)]
        if code[c] == 'R':
            cols = [i for i in cols if i >= math.ceil((min(cols) + max(cols)) / 2)]
    if code[9] == 'L':
        col = min(cols)
    elif code[9] == 'R':
        col = max(cols)

    return row, col

def part_two():
    plane = []
    rows = [-1 for i in range(0, 8)]
    for i in range(0, 128):
        plane.append(rows)

    plane = pd.DataFrame(plane)

    ids = []

    for i in input_:
        r, c = find_seat(i)
        id = get_id(i)
        plane.iloc[r, c] = id
        ids.append(id)

    my_row = 0
    my_col = 0

    for ix, i in plane.iterrows():
        # skip first and last few rows, which are -1
        if ix <= 10:
            continue
        elif ix >= 108:
            continue

        for jx in range(0, 8):
            if plane.iloc[ix, jx] == -1:
                my_row = ix
                my_col = jx

    my_id = (my_row * 8) + my_col
    if ((my_id + 1) in ids) & ((my_id - 1) in ids):
        print(my_id)
    else:
        print("Try again :(")

part_two()