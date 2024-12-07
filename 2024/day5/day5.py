from collections import defaultdict

ex_inp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

rules = [
  (int(l.split('|')[0]), int(l.split('|')[1]))
  for l in inp.split("\n\n")[0].split("\n")
]
lists = [
  [int(x) for x in l.split(",")]
  for l in inp.split("\n\n")[1].split("\n")
]

####################
# PART 1
####################

next_map = defaultdict(list)
for rule in rules:
  next_map[rule[1]].append(rule[0])

# for lis in [lists[-2]]:
res = 0
for lis in lists:
  valid = True
  not_allowed = set()
  for x in lis:
    if x in not_allowed:
      valid = False
      break
    else:
      if x in next_map:
        for y in next_map[x]:
          not_allowed.add(y)
  if valid:
    res += lis[len(lis) // 2]
  
print(f"part 1:", res)

####################
# PART 2
####################
print("PART 2")

def topo_sort(graph):
  visited = set()
  stack = []
  
  def dfs(node):
    if node in visited:
      return
    visited.add(node)
    if node not in graph:
      return
    for neighbor in graph[node]:
      dfs(neighbor)
    stack.append(node)
  
  for node in graph:
    if node not in visited:
      dfs(node)
      
  return stack

topo_sorted = topo_sort(next_map)

forward_map = defaultdict(list)
for rule in rules:
  forward_map[rule[0]].append(rule[1])


def is_valid(lis):
  not_allowed = set()
  for x in lis:
    if x in not_allowed:
      return False
    else:
      if x in next_map:
        for y in next_map[x]:
          not_allowed.add(y)
  return True


res = 0
for lis in lists:
  if is_valid(lis):
    continue
  
  final_lis = lis[:]
  swapped = True
  while swapped:
    swapped = False
    mid_val = final_lis[len(lis) // 2]
    
    # swap second half of list
    for i in range(len(lis) // 2 + 1, len(lis)):
      v = final_lis[i]
      if v in forward_map:
        n = forward_map[v]
        if mid_val in n:
          final_lis[len(lis) // 2], final_lis[i] = final_lis[i], final_lis[len(lis) // 2]
          swapped = True
          break
    if swapped:
      continue
      
    # swap first half of list
    if mid_val not in forward_map:
      continue
    next_vals = forward_map[mid_val]
    for i in range(0, len(lis) // 2):
      v = final_lis[i]
      if v in next_vals:
        final_lis[len(lis) // 2], final_lis[i] = final_lis[i], final_lis[len(lis) // 2]
        swapped = True
        break
    
  print(f"{lis} -> {final_lis}")
  
  res += final_lis[len(lis) // 2]
  
print("part 2:", res)