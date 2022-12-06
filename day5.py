def get_input():
  
  with open("day5.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines

def part1():
  #stacks = [['Z', 'N'],['M', 'C', 'D'],['P']]
  stacks = [['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'], 
            ['S', 'W', 'C'], 
            ['R', 'Z', 'T', 'M'],
            ['D','T','C','H','S','P','V'],
            ['G','P','T','L','D','Z'],
            ['F','B','R','Z','J','Q','C','D'],
            ['S','B','D','J','M','F','T','R'],
            ['L','H','R','B','T','V','M'],
            ['Q','P','D','S','V']
            ]
  instructions = get_input()
  for line in instructions:
    _, quantity, _, source, _, dest = line.split()
    source = int(source) - 1
    dest = int(dest) - 1
    quantity = int(quantity) * -1
    vals = stacks[source][quantity:]
    del stacks[source][quantity:]
    stacks[dest].extend(vals)
  print(stacks)
  for stack in stacks:
    print(stack.pop())


if __name__ == '__main__':
  part1()
  #part2()



#[G]                 [D] [R]        
#[W]         [V]     [C] [T] [M]    
#[L]         [P] [Z] [Q] [F] [V]    
#[J]         [S] [D] [J] [M] [T] [V]
#[B]     [M] [H] [L] [Z] [J] [B] [S]
#[R] [C] [T] [C] [T] [R] [D] [R] [D]
#[T] [W] [Z] [T] [P] [B] [B] [H] [P]
#[D] [S] [R] [D] [G] [F] [S] [L] [Q]
# 1   2   3   4   5   6   7   8   9 