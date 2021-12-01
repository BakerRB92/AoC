from aocd import get_data
from aocd.models import AOCD_CONFIG_DIR, Puzzle
from aocd.utils import AOC_TZ
from aocd.utils import blocker
from dotenv import load_dotenv
load_dotenv('.env')

session = {SESSION_ID}


"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""
ns = get_data(session=session, day=1, year=2021, block=False)

print(ns)
