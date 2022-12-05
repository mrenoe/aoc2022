def get_input():
  
  with open("day4.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines

def part2():
  
  pairs = get_input()
  count = 0
  for line in pairs:
    r1, r2 = line.split(',')
    min1, max1 = r1.split('-')
    set1 = set(range(int(min1),int(max1)+1))
    min2, max2 = r2.split('-')
    set2 = set(range(int(min2), int(max2)+1))
    if set1 & set2:
      count += 1
  print(count)


def part1():
  pairs = get_input()
  count = 0
  for line in pairs:
    r1, r2 = line.split(',')
    min1, max1 = r1.split('-')
    set1 = set(range(int(min1),int(max1)+1))
    min2, max2 = r2.split('-')
    set2 = set(range(int(min2), int(max2)+1))
    if set1 <= set2 or set2 <= set1:
      count += 1
  print(count)


if __name__ == '__main__':
  #part1()
  part2()