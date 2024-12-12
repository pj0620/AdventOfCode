from collections import defaultdict

ex_inp = "2333133121414131402"

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

for i, x in enumerate(inp):
  if i % 2 == 0:
    print(str(i // 2) * int(x), end="")
  else:
    print("." * int(x), end="")
print("")

################################
# PART 2
################################
memory = list(int(x) for x in inp)
r_start = len(memory) - 1
if r_start % 2 == 1:
  r_start -= 1
moved = set()
res = 0
block = 0
free_occupants = defaultdict(list)
for l in range(1, len(memory) - 1, 2):
  cur_l_size = memory[l]
  for r in range(r_start, l, -2):
    r_size = memory[r]
    r_id = r // 2
    if r_id not in moved and r_size <= cur_l_size:
      # print(f"moving {r_id} -> {l}")
      cur_l_size -= r_size
      moved.add(r_id)
      free_occupants[l].append((r_id, r_size))

res = 0
blocks = 0
for i in range(len(memory)):
  if i % 2 == 0:
    id = i // 2
    size = memory[i]
    if id in moved:
      blocks += size
      continue
    for m in range(size):
      res += (blocks + m) * id
    blocks += size
  else:
    size = memory[i]
    if i not in free_occupants:
      blocks += size
      continue
    occupants = free_occupants[i]
    total_o_sizes = 0
    for o_id, o_size in occupants:
      total_o_sizes += o_size
      for m in range(o_size):
        res += (blocks + m) * o_id
      blocks += o_size
    blocks += size - total_o_sizes
print("PART 2:", res)