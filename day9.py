from collections import defaultdict
def get_input():
  
  with open("txtfiles/day9.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines

def follow(head_pos, tail_pos):
      if head_pos[1] == tail_pos[1] and abs(head_pos[0]-tail_pos[0]) > 1: #if h_y == h_y
        if head_pos[0] > tail_pos[0]: #and h_x > t_x
          tail_pos = [tail_pos[0]+1, tail_pos[1]]
        elif head_pos[0] < tail_pos[0]: #and h_x < t_x
          tail_pos = [tail_pos[0]-1, tail_pos[1]]
          
      elif head_pos[0] == tail_pos[0] and abs(head_pos[1]-tail_pos[1]) > 1: #if h_x == h_x
        if head_pos[1] > tail_pos[1]: #and h_y > t_y
          tail_pos = [tail_pos[0], tail_pos[1]+1]
        elif head_pos[1] < tail_pos[1]: #and h_y < h_y
          tail_pos = [tail_pos[0], tail_pos[1]-1]
        
      elif head_pos[0] > tail_pos[0] and (abs(head_pos[0]-tail_pos[0]) > 1 or abs(head_pos[1]-tail_pos[1]) > 1): #if h_x > t_x
        if head_pos[1] > tail_pos[1]: #and h_y > t_y (Up right)
          tail_pos = [tail_pos[0]+1, tail_pos[1]+1]
        elif head_pos[1] < tail_pos[1]: #and h_y < t_y (Down right)
          tail_pos = [tail_pos[0]+1, tail_pos[1]-1]
          
      elif head_pos[0] < tail_pos[0] and (abs(head_pos[0]-tail_pos[0]) > 1 or abs(head_pos[1]-tail_pos[1]) > 1): #if h_x < t_x
        if head_pos[1] > tail_pos[1]: #and h_y > t_y (Up left)
          tail_pos = [tail_pos[0]-1, tail_pos[1]+1]
        elif head_pos[1] < tail_pos[1]: #and h_y < t_y (Down left)
          tail_pos = [tail_pos[0]-1, tail_pos[1]-1]
      return tail_pos

def part1():
  
  head_pos = [0,0] #x,y
  tail_pos = [0,0] #x,y
  visited_history = defaultdict()
  visited_history["0,0"] = '.'

  input = get_input()

  for move in input:
    direction, distance = move.split()
    
    if direction == "R":
      for _ in range(int(distance)):
        head_pos = [head_pos[0]+1, head_pos[1]]
        tail_pos = follow(head_pos, tail_pos)
        visited_history[f"{tail_pos[0]},{tail_pos[1]}"] = "."
    elif direction == "L":
      for _ in range(int(distance)):
        head_pos = [head_pos[0]-1, head_pos[1]]
        tail_pos = follow(head_pos, tail_pos)
        visited_history[f"{tail_pos[0]},{tail_pos[1]}"] = "."
    elif direction == "U":
      for _ in range(int(distance)):
        head_pos = [head_pos[0], head_pos[1]+1]
        tail_pos = follow(head_pos, tail_pos)
        visited_history[f"{tail_pos[0]},{tail_pos[1]}"] = "."
    elif direction == "D":
      for _ in range(int(distance)):
        head_pos = [head_pos[0], head_pos[1]-1]
        tail_pos = follow(head_pos, tail_pos)
        visited_history[f"{tail_pos[0]},{tail_pos[1]}"] = "."
  
  print(visited_history)
  print(len(visited_history))

def part2():
  
  head_pos = [0,0] #x,y
  rope = {
    1:[0,0],
    2:[0,0],
    3:[0,0],
    4:[0,0],
    5:[0,0],
    6:[0,0],
    7:[0,0],
    8:[0,0],
    9:[0,0],
  }

  visited_history = defaultdict()
  visited_history["0,0"] = '.'

  input = get_input()

  for move in input:
    direction, distance = move.split()
    
    if direction == "R":
      for _ in range(int(distance)):
        head_pos = [head_pos[0]+1, head_pos[1]]
        prev = head_pos
        for num in rope:

          rope[num] = follow(prev, rope[num])
          prev = rope[num]
        visited_history[f"{rope[9][0]},{rope[9][1]}"] = "."
    elif direction == "L":
      for _ in range(int(distance)):
        head_pos = [head_pos[0]-1, head_pos[1]]
        prev = head_pos
        for num in rope:

          rope[num] = follow(prev, rope[num])
          prev = rope[num]
        visited_history[f"{rope[9][0]},{rope[9][1]}"] = "."
    elif direction == "U":
      for _ in range(int(distance)):
        head_pos = [head_pos[0], head_pos[1]+1]
        prev = head_pos
        for num in rope:

          rope[num] = follow(prev, rope[num])
          prev = rope[num]
        visited_history[f"{rope[9][0]},{rope[9][1]}"] = "."
    elif direction == "D":
      for _ in range(int(distance)):
        head_pos = [head_pos[0], head_pos[1]-1]
        prev = head_pos
        for num in rope:

          rope[num] = follow(prev, rope[num])
          prev = rope[num]
        visited_history[f"{rope[9][0]},{rope[9][1]}"] = "."
  
  print(visited_history)
  print(len(visited_history))



if __name__ == '__main__':
  #part1()
  part2()