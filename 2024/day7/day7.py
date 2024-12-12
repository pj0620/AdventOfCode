from typing import List, Generator

ex_inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

# print(inp.split("\n")[0].split(":"))
test_vals = [
  int(l.split(":")[0])
  for l in inp.split("\n")
]
nums = [
  [int(x.strip()) for x in l.split(":")[1].split()]
  for l in inp.split("\n")
]

############################
# PART 1
############################


def dp(x: List[int]) -> Generator[int, None, None]:
  if len(x) == 1:
    yield x[0]
  else:
    for sub in dp(x[1:]):
      yield x[0] + sub
      yield x[0] * sub
      
      # remove for part 1
      yield int(str(sub) + str(x[0]))


res = 0
for test_val, inp in zip(test_vals, nums):
  for y in dp(inp[::-1]):
    # print("test_val", test_val, ", y", y)
    if y == test_val:
      res += test_val
      break
print("PART 1:", res)


