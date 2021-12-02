import re

"""
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what 
you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's 
going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these 
together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you
multiply your final horizontal position by your final depth?
"""


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read().splitlines()
        return content  # list with string-values


# def get_forward_values(nav_list):
#     forward = 0
#     forward_pattern = re.compile(r'forward\s(\d+)')
#     for i in nav_list:
#         res = re.search(forward_pattern, i)
#         if res:
#             forward += int(res.group(1))
#     print(forward)


def get_values(nav_list, regex_pattern):
    steps = 0
    direction_pattern = re.compile(regex_pattern)

    for value in nav_list:
        res = re.search(direction_pattern, value)
        if res:
            steps += int(res.group(1))  # only get value from string, convert to int, add to previous values
    return steps


def main():
    list_content = read_file('input.txt')

    pattern_list = [r'forward\s(\d+)', r'down\s(\d+)', r'up\s(\d+)']
    forward = get_values(list_content, pattern_list[0])
    down = get_values(list_content, pattern_list[1])
    up = get_values(list_content, pattern_list[2])

    horizontal = forward
    depth = down - up

    return horizontal * depth  # 1990000


if __name__ == '__main__':
    main()
