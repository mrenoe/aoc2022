from collections import defaultdict

def get_input():
  input = defaultdict(list)
  with open("txtfiles/day1.txt", "r") as tf:
    line = tf.readline()
    i = 0
    while line:
      line = line.rstrip('\n')
      if len(line) > 0:
        input[i].append(int(line))
      else:
        i += 1
      line = tf.readline()
  return input

def part1():
  input = get_input()
  max = 0
  for i in input:
    s = sum(input[i])
    if s > max:
      max = s
  print(max)


def part2():
  input = get_input()
  sums = []
  for i in input:
    sums.append(sum(input[i]))

  sums.sort()
  print(sum(sums[-3:]))





if __name__ == '__main__':
  #part1()
  part2()