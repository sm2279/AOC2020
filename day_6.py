import pandas as pd
import numpy as np
import time
import math
import re

pd.set_option('display.max_rows', None)

from collections import OrderedDict


def remove_dups(str):

    return "".join(set(str))


f = open("AOC2020/input_6.txt", "r")


def part_one():
    sum = 0
    counter = 0
    distinct = []
    for i in f:
        i = i.rstrip()
        if i == '' or i == 'FIN':
            sum = sum + counter
            distinct = []
            counter = 0
        else:
            for j in i:
                if j not in distinct:
                    counter += 1
                    distinct.append(j)

    print(sum)

def part_two():
    sum = 0
    counter = 0
    distinct = []
    for i in f:
        i = i.rstrip()
        if i == '' or i == 'FIN':
            people = len(distinct)
            if people == 1:
                counter = len(set(remove_dups(distinct[0])))
                sum += counter
                counter = 0
                distinct = []
            else:
                qs = {}
                for j in distinct:
                    for k in range(0, len(j)):
                        if j[k] not in qs:
                            qs[j[k]] = 1
                        else:
                            qs[j[k]] += 1

                filter_qs = { k: v for k, v in qs.items() if v == people }

                counter = len(filter_qs.keys())
                print(filter_qs, counter)
                sum += counter
                counter = 0
                distinct = []

        else:
            distinct.append(remove_dups(i))
    print(sum)

part_two()