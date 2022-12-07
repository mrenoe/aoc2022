
def get_input():
  
  with open("txtfiles/day3.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines

def _get_priority(v):
  if ord(v) >= 65 and ord(v) <= 90:
    return ord(v) - 38
  else:
    return ord(v) - 96

def part1():
  packs = get_input()
  tot = 0
  for pack in packs:
    firstpart, secondpart = pack[:len(pack)//2], pack[len(pack)//2:]
    same = set(firstpart) & set(secondpart)
    same = same.pop()
    tot += _get_priority(same)
  print(tot)


def part2():
  packs = get_input()
  tot = 0
  i = 0
  while i < len(packs)-2:
    
    same = set(packs[i]) & set(packs[i+1]) & set(packs[i+2])
    same = same.pop()
    tot += _get_priority(same)
    i += 3
  print(tot)

if __name__ == '__main__':
  #part1()
  part2()