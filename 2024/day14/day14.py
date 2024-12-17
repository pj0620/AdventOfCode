ex_inp = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

##################################
# PART 1
##################################

robots = []
for l in inp.split("\n"):
  problem = []
  eq_split = l.split("=")
  
  p_split = eq_split[1].split(",")
  problem.append(int(p_split[0].strip()))
  problem.append(int(p_split[1].split(" ")[0].strip()))
  
  v_split = eq_split[2].split(",")
  problem.append(int(v_split[0].strip()))
  problem.append(int(v_split[1].strip()))
  
  robots.append(tuple(problem))

#             |
# 0 1 2 3 4 5 6 7 8 9 10 11 12

quad_counts = [[0, 0], [0, 0]]
for px, py, vx, vy in robots:
  xf, yf = (px + 100 * vx) % 101, (py + 100 * vy) % 103
  
  if xf == 50 or yf == 51:
    continue
  
  xq = 1 if xf < 50 else 0
  yq = 1 if yf < 51 else 0
  
  quad_counts[xq][yq] += 1
ans = quad_counts[0][0] * quad_counts[0][1] * quad_counts[1][0] * quad_counts[1][1]
print("PART 1:", ans)
