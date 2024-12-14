from collections import defaultdict
from dataclasses import dataclass
from typing import Self, List

ex_inp = """125 17"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

cache = {}

#####################
# PART 1
#####################


def dp(val, n):
  global cache
  if n == 0:
    return 1
  elif (val, n) in cache:
    return cache[(val, n)]
  
  if val == 0:
    res = dp(1, n - 1)
  elif len(str(val)) % 2 == 0:
    str_val = str(val)
    l_val = int(str_val[:len(str_val) // 2])
    r_val = int(str_val[len(str_val) // 2:])
    l_count = dp(l_val, n - 1)
    r_count = dp(r_val, n - 1)
    res = l_count + r_count
  else:
    res = dp(2024 * val, n - 1)
  cache[(val, n)] = res
  return res


final_part1 = 0
for x in inp.split(" "):
  final_part1 += dp(int(x), 25)
print("part 1:", final_part1)

#####################
# PART 2
#####################

final_part2 = 0
for x in inp.split(" "):
  final_part2 += dp(int(x), 75)
print("part 2:", final_part2)

# nodes = list(range(2025))
# graph = defaultdict(list)
# for n in nodes:
#   if n == 0:
#     graph[n].append((1, 1))
#   elif len(str(n)) % 2 == 0:
#     str_val = str(n)
#     l_val = int(str_val[:len(str_val) // 2])
#     r_val = int(str_val[len(str_val) // 2:])
#     graph[n].append((l_val, 1))
#     graph[n].append((r_val, 1))
#   else:
#     queue = [(n * 2024, 1)]
#     while queue:
#       cur_n, cur_steps = queue.pop(-1)
#       cur_str = str(cur_n)
#       if cur_n < 2025:
#         graph[n].append((cur_n, cur_steps))
#       elif len(cur_str) % 2 == 0:
#         l_val = int(cur_str[:len(cur_str) // 2])
#         r_val = int(cur_str[len(cur_str) // 2:])
#         queue.append((l_val, cur_steps + 1))
#         queue.append((r_val, cur_steps + 1))
#       else:
#         queue.append((2024 * cur_n, cur_steps + 1))
# print(graph)
#
# tot_connections = 0
# for iter in range(75):
#   print("iter: ", iter)
#   for n_str in inp.split(" "):
#     n = n_str
#     print("n = ", n, " tot_connections = ", tot_connections)
#     new_connections = []
#     for nex_val, nex_steps in graph[n]:
#       if nex_steps >= 75:
#         new_connections.append((nex_val, nex_steps))
#         continue
#       for nex2_val, nex2_steps in graph[nex_val]:
#         if nex2_steps + nex_steps > 75:
#           continue
#         new_connections.append((nex2_val, nex2_steps + nex_steps))
#     tot_connections -= len(graph[n])
#     tot_connections += len(new_connections)
#     graph[n] = new_connections
# print(graph)

# total_steps = []
# for n in inp.split(" "):
#   res = 0
#   q = [(int(n), 0)]
#   visited = set()
#   while q:
#     print(n, " -> ", len(q), " <> ", max(steps for x, steps in q))
#     cur_val, cur_steps = q.pop(-1)
#     if cur_val in visited:
#       continue
#     visited.add(cur_val)
#     if cur_steps >= 75:
#       res += 1
#     else:
#       next_vals = graph[cur_val]
#       for nex_val, nex_steps in next_vals:
#         if nex_steps + cur_steps <= 75:
#           q.append((nex_val, nex_steps + cur_steps))
#   total_steps.append(res)
# print(total_steps)

# print(len(head))