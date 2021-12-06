from aocd import get_data
##from ..util.config import AOCD_SESSION, AOCD_DIR

"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""

AOCD_SESSION = ""
Test_data = """
"""


ns = get_data(session=AOCD_SESSION, day=1, year=2021, block=False)

T_data = [int(n) for n in ns.split()]

print("part a:", sum(n2 > n1 for n1, n2 in zip(T_data, T_data[1:])))
print("part b:", sum(n2 > n1 for n1, n2 in zip(T_data, T_data[3:])))

