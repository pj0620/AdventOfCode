ex_inp = """AAAA
BBCD
BBCC
EEEC"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = ex_inp

#################################
# PART 2
#################################
from typing import Set, Tuple


def get_corners(x, y) -> Set[Tuple[int, int]]:
  return {(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)}


def merge_corners(A, B):
  return (A - B) | (B - A)


visited = set()
ans = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if (x, y) in visited:
      continue
    plant = board[x][y]
    if plant == "B":
      pass
    area = 0
    total_corners = 4
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
      
      # internal corners
      this_corners: Set[Tuple[int, int]] = get_corners(xc, yc)
      other_corners: Set[Tuple[int, int]] = set()
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xn, yn = xc + dx, yc + dy
        if not (0 <= xn < len(board)) or not (0 <= yn < len(board[0])) or board[xn][yn] != plant:
          continue
        other_corners |= get_corners(xn, yn)
        q.append((xn, yn))
      shared_corners = this_corners & other_corners
      new_corners = this_corners - other_corners
      total_corners += len(new_corners) - len(shared_corners)
      area += 1
    print(f"{plant} -> {(total_corners, area)=}")
    ans += total_corners * area
print("part 2:", ans)
