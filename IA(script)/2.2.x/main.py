import argparse
from check_balises import *


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="path to the file")
    args = parser.parse_args()
    return(args.name)


def create_array(line):
    tmp_list = []
    index = 0
    pos = 0
    pos2 = 0

    if line[0] == '<':
        index = line.find(' ') + 1
        tmp_list.append(line[0: index - 1])
    while True:
        if line[index:].find('"') is not -1:
            pos = line.index('"', index)
            pos2 = line.index('"', pos + 1)
            tmp_list.append(line[index:pos2 + 1])
            index = pos2 + 2
        else:
            break
    return(tmp_list)


def clean_data(lines):
    good = []
    for line in lines:
        tmp_list = create_array(line)
        good.append(tmp_list)
    return(good)

if __name__ == "__main__":

    file_name = argument_parser()
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except Exception as ex:
        print(f'Error: {ex}')
    data_array = clean_data(lines)
    check_tag(lines)