import pandas as pd
import numpy as np
import time

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

f = open("AOC2020/input_3.txt", "r")

input_ = [i.rstrip() for i in f]


def part_one():
    trees = 0
    squares = 0

    position = 0
    for row in input_[1:]:
        if position + 3 >= len(row):
            position = (position + 3) % len(row)
        else:
            position += 3
        if row[position] == '#':
            row = replace_str_index(row, position, 'X')
            trees += 1
        else:
            squares += 1
            row = replace_str_index(row, position, 'O')
    print(trees)

def part_two(right, down):
    trees = 0
    squares = 0

    position = 0
    ir = 1
    for row in input_[1:]:
        if down == 2 and ir % 2 != 0:
            ir += 1
            continue

        if position + right >= len(row):
            position = (position + right) % len(row)
        else:
            position += right
        if row[position] == '#':
            row = replace_str_index(row, position, 'X')
            trees += 1
        else:
            squares += 1
            row = replace_str_index(row, position, 'O')
        ir += 1
    return trees

# part two
sc1 = part_two(1, 1)
sc2 = part_two(3, 1)
sc3 = part_two(5, 1)
sc4 = part_two(7, 1)
sc5 = part_two(1, 2)

print(sc1 * sc2 * sc3 * sc4 * sc5)
