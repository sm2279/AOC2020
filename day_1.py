import pandas as pd
import numpy as np
import time
f = open("input.txt", "r")

input_ = [int(i.rstrip()) for i in f]

def part_one():
    # part one
    foundit = 0
    for ix in input_:
        for jx in input_:
            if input_.index(ix) == input_.index(jx):
               continue
            if (ix + jx) == 2020:
               print(ix,jx)
               print(ix * jx)
               foundit = 1
               break

def part_two():
    # part two
    foundit = 0
    for ix in input_:
        for jx in input_:
            for zx in input_:
                if input_.index(ix) == input_.index(jx) or input_.index(zx) == input_.index(jx) or input_.index(ix) == input_.index(zx):
                    continue
                if (ix + jx + zx) == 2020:
                    print(ix ,jx, zx)
                    foundit = 1
                    break
            if foundit == 1:
                break
        if foundit == 1:
            break


def __main__():
    start = time.time()

    part_one()
    part_two()
    
    end = time.time()
    print("Time: ", end-start)