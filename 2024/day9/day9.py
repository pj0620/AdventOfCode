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
# PART 1
################################
memory = list(int(x) for x in inp)
print(memory)
l = 0
r = len(memory) - 1
if r % 2 == 1:
  r -= 1
res = []
while l <= r:
  if l % 2 == 0:
    for _ in range(memory[l]):
      res.append(l // 2)
    memory[l] = 0
    l += 1
  else:
    l_free_count = memory[l]
    r_file_count = memory[r]
    r_file = r//2
    if l_free_count < r_file_count:
      memory[l] = 0
      l += 1
      memory[r] = r_file_count - l_free_count
      for _ in range(l_free_count):
        res.append(r_file)
    elif l_free_count == r_file_count:
      memory[l] = 0
      memory[r] = 0
      l += 1
      r -= 2
      for _ in range(l_free_count):
        res.append(r_file)
    else:
      for _ in range(r_file_count):
        res.append(r_file)
      memory[r] = 0
      r -= 2
      memory[l] -= r_file_count
      
print(res)
print("PART 1:", sum(
  k * int(x)
  for k, x in enumerate(res)
))
