import re
import numpy as np


def max_of_each_color(blue, green, red):
    return max([int(count) for count in blue]) * max([int(count) for count in green]) * max([int(count) for count in red])


def part_2():
    total = 0
    with open("input.txt", "r") as f:
        contents = f.read().split('\n')
        for game in contents:
            match = re.search(r'Game (?P<game_num>\d+): ', game)
            if match:
                blue = re.findall(r'(\d+) blue', game)
                red = re.findall(r'(\d+) red', game)
                green = re.findall(r'(\d+) green', game)
                total += max_of_each_color(blue, green, red)
    return total


def is_possible(blue, green, red):
    return not any(
        [
            any([int(count)>14 for count in blue]),
            any([int(count)>13 for count in green]),
            any([int(count)>12 for count in red])
        ]
    )

    
def part_1():
    total = 0
    with open("input.txt", "r") as f:
        contents = f.read().split('\n')
        for game in contents:
            match = re.search(r'Game (?P<game_num>\d+): ', game)
            if match:
                blue = re.findall(r'(\d+) blue', game)
                red = re.findall(r'(\d+) red', game)
                green = re.findall(r'(\d+) green', game)
                if not is_possible(blue, green, red):
                    continue
                total += int(match.group("game_num"))
    return total
                        

def main():
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")

if __name__ == "__main__":
    main()