import pandas as pd
import numpy as np
import time
import re

f = open("AOC2020/input_4.txt", "r")

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def check_valid_fields(lst1):
    required1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in required1:
        if i not in lst1:
            return False
    return True

def check_color_hex(color_code):
    if not color_code.startswith('#'):
        return False
    if len(color_code) != 7:
        return False
    valid = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_code)
    if valid is None:
        return False
    else:
        return True

def part_one():
    valid = 0

    passport_fields = []
    for i in f:
        i = i.rstrip()

        if i == '' or i == 'FIN':
            if check_valid_fields(passport_fields):
                valid += 1
            passport_fields = []
            continue

        line = i.split(' ')
        fileds = [l.split(':') for l in line]
        if len(fileds) > 1:
            for o in fileds:
                if o[0] in required:
                    passport_fields.append(o[0])
        else:
            tmp = fileds[0]
            if tmp[0] in required:
                passport_fields.append(tmp[0])

    print(valid)


def part_two():
    valid = 0

    passport_fields = []
    for i in f:
        i = i.rstrip()
        if i == '' or i == 'FIN':
            if check_valid_fields(passport_fields):
                valid += 1
            passport_fields = []
            continue

        line = i.split(' ')
        fileds = [l.split(':') for l in line]

        if len(fileds) > 1:
            for o in fileds:
                if (o[0] == 'byr'):
                    if (len(o[1]) == 4) & (1920 <= int(o[1]) <= 2002):
                        passport_fields.append(o[0])
                elif (o[0] == 'iyr'):
                    if (len(o[1]) == 4) & (2010 <= int(o[1]) <= 2020):
                        passport_fields.append(o[0])
                elif (o[0] == 'eyr'):
                    if (len(o[1]) == 4):
                        if (2020 <= int(o[1]) <= 2030):
                            passport_fields.append(o[0])
                elif (o[0] == 'hgt'):
                    value = o[1]
                    unit = value[-2:]
                    if unit in ['cm', 'in']:
                        value = int(value[:-2])
                        if (unit == 'cm') & (150 <= value <= 193):
                            passport_fields.append(o[0])
                        elif (unit == 'in') & (59 <= value <= 76):
                            passport_fields.append(o[0])
                elif o[0] == 'hcl':
                    color = o[1]
                    if check_color_hex(color):
                        passport_fields.append(o[0])
                elif o[0] == 'ecl':
                    if o[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        passport_fields.append(o[0])
                elif o[0] == 'pid':
                    if (len(o[1]) == 9) & (o[1].isdigit()):
                        passport_fields.append(o[0])
        else:
            o = fileds[0]
            if (o[0] == 'byr'):
                if (len(o[1]) == 4) & (1920 <= int(o[1]) <= 2002):
                    passport_fields.append(o[0])
            elif (o[0] == 'iyr'):
                if (len(o[1]) == 4) & (2010 <= int(o[1]) <= 2020):
                    passport_fields.append(o[0])
            elif (o[0] == 'eyr'):
                if (len(o[1]) == 4):
                    if (2020 <= int(o[1]) <= 2030):
                        passport_fields.append(o[0])
            elif (o[0] == 'hgt'):
                value = o[1]
                unit = value[-2:]
                if unit in ['cm', 'in']:
                    value = int(value[:-2])
                    if (unit == 'cm') & (150 <= value <= 193):
                        passport_fields.append(o[0])
                    elif (unit == 'in') & (59 <= value <= 76):
                        passport_fields.append(o[0])
            elif o[0] == 'hcl':
                color = o[1]
                if check_color_hex(color):
                    passport_fields.append(o[0])
            elif o[0] == 'ecl':
                if o[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    passport_fields.append(o[0])
            elif o[0] == 'pid':
                if (len(o[1]) == 9) & (o[1].isdigit()):
                    passport_fields.append(o[0])
    print(valid)

part_two()