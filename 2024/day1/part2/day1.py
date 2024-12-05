from collections import defaultdict

ex_inp = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

numbers = [[int(x) for x in l.split(" ") if len(x) > 0] for l in inp.split("\n")]

A = [x[0] for x in numbers]
B = [x[1] for x in numbers]

print(f"{A=}, {B=}")

counts = defaultdict(int)
for n in B:
  counts[n] += 1

print(sum(
  counts[x] * x
  for x in A
))