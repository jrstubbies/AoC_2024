# AoC_2024
Advent of Code 2024 edition


Day 3 Part A:
    Taking in a input of chars, identify the valid parts. Valid parts are in form of:
        - "mul(x, y)"
        - where x and y are two numbers between 1 and 3 digits long
    Take the valid statements and perform the multiplication of the two numbers within the brackets.
    The final answer is the sum of all valid multiplications.


Day 3 Part B:
    Using same input. The input contains words "do()" and "don't()". Now need to calculate ONLY the 'mul(x,y)'
    that come AFTER a 'do()' and before a 'don't()'.