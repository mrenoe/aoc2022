from collections import defaultdict
def get_input():
  
  with open("txtfiles/day7a.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines


def dfs(visited, directory, directories, directory_sizes):
  print(f"visited: {visited}")
  if directory in visited:
    print(f"{directory} in {visited} returning: {sum(directory_sizes[directory])}")
    return sum(directory_sizes[directory])
  visited.add(directory)
  running_total = sum(directory_sizes[directory])
  for i in range(1, len(directories[directory])):
    print(f"Traversing {directories[directory][i]}")

    running_total += dfs(visited, directories[directory][i], directories, directory_sizes)

  print(f"finished, returning {running_total}")
  return running_total

def part1():
  shell_out = get_input()
  directories = defaultdict(list)
  directory_sizes = defaultdict(list)
  directories['/'] #starting point
  cwd =  '/'
  ls_running = False
  for line in shell_out:
    
    if line[0] == '$':
      ls_running = False
      command = line.split()
      
      if command[1] == 'cd' and command[2] == '..':
        cwd = directories[cwd][0]
      elif command[1] == 'cd':
        cwd = command[2]
      elif command[1] == 'ls':
        ls_running = True
        continue

    if ls_running:
      args = line.split()
      if args[0] == 'dir':
        directories[cwd].append(args[1])
        directories[args[1]].append(cwd) #cwd has to be the 0th element
      else:
        size, _ = line.split()
        directory_sizes[cwd].append(int(size))
  print(directories)
  print(directory_sizes)
  total_sizes = {}
  for directory in directories:
    print(f"directory: {directory}")
    start = 0
    if directory != '/':
      start = 1
    visited = set()
    tot = sum(directory_sizes[directory])
    for i in range(start, len(directories[directory])):
      tot += dfs(visited, directories[directory][i], directories, directory_sizes)
    
    total_sizes[directory] = tot
  
  print(total_sizes)
  total = 0
  for dir in total_sizes:
    if total_sizes[dir] <= 100000:
      total += total_sizes[dir]
  print(total)
    

def part2():
  '''
  '''

if __name__ == '__main__':
  part1()
  #part2()