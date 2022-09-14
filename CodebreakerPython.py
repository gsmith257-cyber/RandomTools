import json
import math

stepinator = json.load(open('\Users\you\Codebreaker2020\Challenge4\stepinator.json', 'r'))

step = 1/4
position = 0
velocity = 0
time = 0
while time < 220:
  if (time < len(stepinator)):
    velocity += stepinator[math.floor(time)]*step
  position += velocity*step
  if (time % 1 == 0):
    print(f'time: {math.floor(time)} vel: {round(velocity)} pos: {round(position)}')
  time += step
