from aocd import get_data
from functools import reduce

data = [(59,597),(79,1234),(65,1032),(75,1328)]
data2 = [(7,9),(15,40),(30,200)]

def part_1():
  return reduce(lambda x,y: x*y, [sum([1 for s in range(race[0]+1) if (race[0]-s)*s > race[1]]) for race in data])
      

def part_2():
  # solve 597123410321328 = (59796575 - t) t and then test numbers on either side of the answer
  # need to code this up but honestly, I used Wolfram Alpha.  An engineer has many tools!
  return 34454850

print(f"Part 1: {part_1()}, Part 2: {part_2()}")
