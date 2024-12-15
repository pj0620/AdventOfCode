from collections import defaultdict

ex_inp = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = ex_inp

board = [
  l for l in inp.split("\n")
]

#################################
# PART 2
#################################
from typing import Set, Tuple, List


def get_corners(x, y) -> List[Tuple[int, int]]:
  return [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]


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
    corners_map = defaultdict(int)
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
      for corner_x, corner_y in get_corners(xc, yc):
        if not (0 <= corner_x <= len(board)) or not (0 <= corner_y <= len(board[0])):
          continue
        corners_map[(corner_x, corner_y)] += 1
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xn, yn = xc + dx, yc + dy
        if not (0 <= xn < len(board)) or not (0 <= yn < len(board[0])):
          continue
        q.append((xn, yn))
      area += 1
    total_corners = sum(
      1 for corner, corner_count in corners_map.items() if corner_count % 2 == 1
    )
    print(f"{plant} -> {(total_corners, area)=}")
    ans += total_corners * area
print("part 2:", ans)
