import numpy as np

ex_inp = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

problems = []
for prob_str in inp.split("\n\n"):
  problem = []
  # print("\n", prob_str)
  abp_parts = prob_str.split("\n")
  for part in abp_parts[:2]:
    plus_split = part.split("+")
    problem.append(int(plus_split[1].split(",")[0].strip()))
    problem.append(int(plus_split[2]))
  eq_split_last = abp_parts[2].split("=")
  problem.append(int(eq_split_last[1].split(",")[0].strip()))
  problem.append(int(eq_split_last[2].strip()))
  problems.append(tuple(problem))

is_close = lambda x: (x - round(x, 0)) ** 2 <= 0.0001

res = 0
for problem in problems:
  ax, ay, bx, by, px, py = problem
  M = np.array([
    [ax, bx],
    [ay, by]
  ]).astype(np.float64)
  
  v = np.array([
    px,
    py
  ]).astype(np.float64)
  
  r = np.linalg.solve(M, v)
  cost = 3 * r[0] + r[1]

  if is_close(cost):
    print(cost)
    res += cost

print("PART 1:", res)

###########################
# PART 2
###########################

res = 0
for problem in problems:
  ax, ay, bx, by, px, py = problem
  px += 10000000000000
  py += 10000000000000
  
  # Constructing the matrix M
  det = ax * by - ay * bx
  if det == 0:
    raise ValueError("Matrix is singular, cannot solve.")
  
  # Calculating the inverse of M manually
  inv_M_det = [
    [by, -bx],
    [-ay, ax]
  ]
  
  # Constructing vector v
  v = [px, py]
  
  # Matrix-vector multiplication to find r
  r = [
    inv_M_det[0][0] * v[0] + inv_M_det[0][1] * v[1],
    inv_M_det[1][0] * v[0] + inv_M_det[1][1] * v[1]
  ]
  
  if r[0] % det != 0 or r[1] % det != 0:
    continue
  
  cost = (3 * r[0] + r[1]) // det
  
  res += round(cost, 0)

print("PART 2:", res)
