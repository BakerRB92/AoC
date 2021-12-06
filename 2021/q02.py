import aocd
from aocd.models import Puzzle
from aocd import get_data
import os

AOCD_SESSION = ""
ns = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


ns_t = get_data(session=AOCD_SESSION, day=2, year=2021, block=False)
data = [n for n in ns.split()]
Distance = data[1::2]
Direction = data[0::2]

New_data = list(zip(Direction, Distance))

Horz_Pos = int(0)
Depth_pos = int(0)

aim = int(0)

for Sub_Data in New_data:
    Dir = Sub_Data[0]
    Dist = int(Sub_Data[1])
    if Dir == 'forward':
        Horz_Pos += Dist
        Depth_pos += aim*Dist
    else:
        if Dir == 'up':
            Depth_pos -= Dist
            aim -= Dist
        else:
            Depth_pos += Dist
            aim += Dist


final_pos = Horz_Pos * Depth_pos
print(f'Horzential: {Horz_Pos}, Depth: {Depth_pos} - Final Pos: {final_pos}')





