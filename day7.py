from collections import defaultdict
def get_input():
  
  with open("txtfiles/day7.txt", "r") as tf:
    lines = tf.read().split("\n")
  return lines


def dfs(visited, directory, directories, directory_sizes):
  
  visited.add(directory)
  running_total = sum(directory_sizes[directory])
  
  for i in range(0, len(directories[directory])):
    
    if directories[directory][i] not in visited:

      running_total += dfs(visited, directories[directory][i], directories, directory_sizes)


  return running_total

def part1():
  shell_out = get_input()
  directories = defaultdict(list)
  directory_sizes = defaultdict(list)
  directories['/-/'] = ['-1'] #starting point
  cwd =  '/'
  ls_running = False
  for line in shell_out:
    
    if line[0] == '$':
      ls_running = False
      command = line.split()
      
      if command[1] == 'cd' and command[2] == '..':
        print(f"cwd was: {cwd}, will become: {directories[cwd][0]}")
        cwd = directories[cwd][0]
        
      elif command[1] == 'cd':
        cwd = cwd + '-' + command[2]
      elif command[1] == 'ls':
        ls_running = True
        continue

    if ls_running:
      args = line.split()
      if args[0] == 'dir':
        if cwd == '/':
          directories[cwd].append(args[1])
          directories[args[1]].append(cwd) #cwd has to be the 0th element
        else:
          directories[cwd].append(f"{cwd}-{args[1]}")
          directories[f"{cwd}-{args[1]}"].append(cwd) #cwd has to be the 0th element
      else:
        size, _ = line.split()
        directory_sizes[cwd].append(int(size))
  #print(directories)
  #print(directory_sizes)
  total_sizes = {}
  for directory in directories: #Go over each directory
    print(f"\ndirectory: {directory}")
    visited = set()
    if directory != '/':
      visited.add(directories[directory][0])
    
    tot = 0
    tot += dfs(visited, directory, directories, directory_sizes)
    
    total_sizes[directory] = tot
  
  print(total_sizes)
  total = 0
  for dir in total_sizes:
    if total_sizes[dir] <= 100_000:
      
      total += total_sizes[dir]
  print(total)
    

def part2():
  '''
  '''

if __name__ == '__main__':
  part1()
  #part2()