# AoC_2024
Advent of Code 2024 edition

Day 2 Part A (https://adventofcode.com/2024/day/2#part1):
    Count the lines of input that match the patterns:
        i- the line start-to-finish either increases or decreases
        ii- each value in the line must have a difference of 1 - 3 (CANNOT be same number, or have difference greater than 3)
    The total number of 'safe' (valid) lines will be the answer to submit


Day 2 Part B (https://adventofcode.com/2024/day/2#part2):
    Same process as before, except can now tolerate a SINGLE bad level. This means if there is a single duplicate value, or a single level that affects the gradual increase/decrease, then ignore and count as safe. If there is MORE THAN 1 incorrect level then is still unsafe. Should also be unsafe if the difference is greater than 3. 
