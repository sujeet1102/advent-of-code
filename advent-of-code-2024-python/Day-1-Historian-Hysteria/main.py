
# MIT License

# Copyright (c) 2024 Sujeet Jagtap

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# advent-of-code-2024-python: Learning python the pythonic way while completing AOC 2024

# Author: Sujeet Jagtap sujeet1102.github.io 
# GitHub: https://github.com/sujeet1102/advent-of-code

from collections import defaultdict

def parse_numbers_from_file(filename):
    left_side_nums = []
    right_side_nums = []

    with open(filename, 'r') as file:
        for line in file:
            a, b = map(int, line.split())
            left_side_nums.append(a)
            right_side_nums.append(b)
    return left_side_nums, right_side_nums

left_list, right_list = parse_numbers_from_file('input.txt')

left_list.sort(key=None, reverse=False)
right_list.sort(key=None, reverse=False)

answer1 = 0

for i in range(0, 1000):
    answer1 += abs(left_list[i]-right_list[i])

print(f"total distance between your lists = {answer1}")

hash_array = defaultdict(int)
for i in range(0, 1000):
    hash_array[right_list[i]] += 1

similarity_score = 0
for i in range(0, 1000):
    similarity_score += (left_list[i] * hash_array[left_list[i]])

print(f"similarity score = {similarity_score}")