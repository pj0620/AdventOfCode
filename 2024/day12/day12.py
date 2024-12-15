from typing import Set, Tuple

ex_inp = """AAAA
BBCD
BBCC
EEEC"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = ex_inp

board = [
  l for l in inp.split("\n")
]

#################################
# PART 1
#################################
visited = set()
ans = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if (x, y) in visited:
      continue
    plant = board[x][y]
    perim = 0
    area = 0
    q = [(x, y)]
    while q:
      xc, yc = q.pop(-1)
      if not (0 <= xc < len(board)) or not (0 <= yc < len(board[0])):
        continue
      if (xc, yc) in visited:
        continue
      
      cur_plant = board[xc][yc]
      if cur_plant != plant:
        continue
      
      visited.add((xc, yc))
      
      deduct = 0
      for dx1, dy1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xn1, yn1 = xc + dx1, yc + dy1
        if not (0 <= xn1 < len(board)) or not (0 <= yn1 < len(board[0])):
          continue
        if board[xn1][yn1] == plant:
          deduct += 1
          q.append((xn1, yn1))
          
      perim += 4 - deduct
      area += 1
      # print(f"{(xc, yc)=} -> {(4 - deduct, 1)=}")
    print(f"{plant} -> {(perim, area)=}")
    ans += perim * area
print("part 1:", ans)