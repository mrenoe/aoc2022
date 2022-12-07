def get_input():
  
  with open("txtfiles/day6.txt", "r") as tf:
    lines = tf.read().strip()
  return lines


def part1():
  buffer = list(get_input())
  
  for i in range(len(buffer)):
    test = set(buffer[i:i+4])
    
    if len(test) == 4:
      print(i+4)
      break

def part2():
  buffer = list(get_input())
  
  for i in range(len(buffer)):
    test = set(buffer[i:i+14])
    
    if len(test) == 14:
      print(i+14)
      break

if __name__ == '__main__':
  #part1()
  part2()