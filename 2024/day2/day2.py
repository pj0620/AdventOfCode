ex_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

data = [[int(x) for x in l.split(" ")] for l in inp.split("\n")]

print(data)

res = 0
for row in data:
  dec = row[1] < row[0]
  valid = True
  for i in range(len(row) - 1):
    dif = row[i+1] - row[i]
    # print(" ", dif, " -> ", -1 <= dif <= -3)
    if dec and not(-1 >= dif >= -3):
      valid = False
      break
    elif not dec and not(1 <= dif <= 3):
      valid = False
      break
  if valid:
    res += 1
print("part1: ", res)

###
# PART 2
###
res = 0
for row in data:
  print("#" * 10)
  print(f"{row=}")
  
  def dp(row, i):
    if i == len(row) - 1:
      return row[-1], 0, 0, 0
    
    next_first_val, inc_count, dec_count, rem_count = dp(row, i+1)
    print(i+1, f" -> {(next_first_val, inc_count, dec_count, rem_count)=}")
    dif = next_first_val - row[i]
    print(f"{i=} {dif=} {next_first_val} - {row[i]}")
    
    if not (1 <= abs(dif) <= 3):
      return next_first_val, inc_count, dec_count, rem_count + 1
    elif dif < 0:
      return row[i], inc_count, dec_count + 1, rem_count
    else:
      return row[i], inc_count + 1, dec_count, rem_count
  
  
  next_first_val, inc_count, dec_count, rem_count = dp(row, 0)
  print(f"{(next_first_val, inc_count, dec_count, rem_count)=}")
  
  if rem_count == 0 and min(inc_count, dec_count) <= 1:
    res += 1
  elif rem_count <= 1 and min(inc_count, dec_count) == 0:
    res += 1
  else:
    print("Unsafe!")
  
def is_valid(row):
  dec = row[1] < row[0]
  for i in range(len(row) - 1):
    dif = row[i + 1] - row[i]
    if dec and not (-1 >= dif >= -3):
      return False
    elif not dec and not (1 <= dif <= 3):
      return False
  return True

res = 0
for row in data:
  for i in range(len(row)):
    if is_valid(row[:i] + row[i+1:]):
      res += 1
      break
print("part2: ", res)
