from collections import defaultdict
def get_input():
  
  with open("txtfiles/day8.txt", "r") as tf:
    lines = []
    for line in tf.read().split("\n"):
      lines.append([int(i) for i in list(line)])
  return lines

def visibleUp(i, j, input):
  size = input[i][j]
  while i > 0:
    i -= 1
    if size <= input[i][j]:
      return False
  return True

def visibleDown(i, j, input):
  size = input[i][j]
  while i < len(input)-1:
    i += 1
    if size <= input[i][j]:
      return False
  return True

def visibleLeft(i, j, input):
  size = input[i][j]
  while j > 0:
    j -= 1
    if size <= input[i][j]:
      return False
  return True

def visibleRight(i, j, input):
  size = input[i][j]
  while j < len(input[i])-1:
    j += 1
    if size <= input[i][j]:
      return False
  return True

def part1():
  input = get_input()
  print(input)
  map = [ [0]*len(input[i]) for i in range(len(input))]
  count = 0
  for i in range(0, len(input)):
    for j in range(0, len(input[i])):
      if i == 0 or j == 0 or j == len(input[i])-1 or i == len(input)-1:
        #print(f"i, {i}, j: {j}")
        map[i][j] = 'v'
        count += 1
      else:
        left = visibleLeft(i, j, input)
        right = visibleRight(i, j, input)
        up = visibleUp(i, j, input)
        down = visibleDown(i, j, input)
        if up or down or left or right:
          map[i][j] = 'v'
          count += 1
        else:
          map[i][j] = 'i'
       
  print(count)
        
def viewingDistanceUp(i, j, input):
  size = input[i][j]
  distance = 0
  while i > 0:
    i -= 1
    distance += 1
    if size <= input[i][j]:
      break
  return distance

def viewingDistanceDown(i, j, input):
  size = input[i][j]
  distance = 0
  while i < len(input)-1:
    i += 1
    distance += 1
    if size <= input[i][j]:
      break
  return distance

def viewingDistanceLeft(i, j, input):
  size = input[i][j]
  distance = 0
  while j > 0:
    j -= 1
    distance += 1
    if size <= input[i][j]:
      break
  return distance

def viewingDistanceRight(i, j, input):
  size = input[i][j]
  distance = 0
  while j < len(input[i])-1:
    j += 1
    distance += 1
    if size <= input[i][j]:
      break
  return distance

def part2():
  input = get_input()
  
  distances = []
  for i in range(0, len(input)):
    for j in range(0, len(input[i])):
      if i == 0 or j == 0 or j == len(input[i])-1 or i == len(input)-1:
        continue
      else:
        left = viewingDistanceLeft(i, j, input)
        right = viewingDistanceRight(i, j, input)
        up = viewingDistanceUp(i, j, input)
        down = viewingDistanceDown(i, j, input)
        print(f"\nAt point {i},{j}, value: {input[i][j]}")
        print(f"Scores - Left: {left}, Right: {right}, Up: {up}, Down:{down}")
        distances.append(left * right * up * down)
      
       
  print(distances)     
  print(f"max: {max(distances)}")


if __name__ == '__main__':
  #part1()
  part2()