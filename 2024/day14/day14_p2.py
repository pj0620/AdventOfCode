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
# PART 2
##################################

# parse input
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

for t in range(10000):
  
  # Find robots close to each other
  next_set = set()
  matching = set()
  for px, py, vx, vy in robots:
    xf, yf = (px + t * vx) % 101, (py + t * vy) % 103
    if (xf, yf) in next_set:
      matching.add((xf, yf))
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        next_set.add((xf + dx, yf + dy))
        
  # print matching board
  if len(matching) > 256:
    for x in range(100):
      for y in range(101):
        if (x, y) in next_set:
          print("*", end="")
        else:
          print(".", end="")
      print("")
    print("t:", t)
    