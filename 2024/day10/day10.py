ex_inp = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

top_map = [
  [int(c) for c in l]
  for l in inp.split("\n")
]

reachable = 0
for xs in range(len(top_map)):
  for ys in range(len(top_map[0])):
    if top_map[xs][ys] != 0:
      continue
    visited = set()
    q = [(xs, ys)]
    while q:
      x_cur, y_cur = q.pop(-1)
      cur_height = top_map[x_cur][y_cur]
      for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
        nx, ny = x_cur + dx, y_cur + dy
        if not (0 <= nx < len(top_map)) or not (0 <= ny < len(top_map[0])):
          continue
        if (nx, ny) in visited:
          continue
        next_height = top_map[nx][ny]
        if next_height == cur_height + 1:
          if next_height == 9:
            visited.add((nx, ny))
            reachable += 1
          else:
            q.append((nx, ny))
      visited.add((x_cur, y_cur))
print("PART 1: ", reachable)

#############
# PART 2
#############
reachable = 0
for xs in range(len(top_map)):
  for ys in range(len(top_map[0])):
    if top_map[xs][ys] != 0:
      continue
    q = [(xs, ys)]
    while q:
      x_cur, y_cur = q.pop(-1)
      cur_height = top_map[x_cur][y_cur]
      for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
        nx, ny = x_cur + dx, y_cur + dy
        if not (0 <= nx < len(top_map)) or not (0 <= ny < len(top_map[0])):
          continue
        next_height = top_map[nx][ny]
        if next_height == cur_height + 1:
          if next_height == 9:
            reachable += 1
          else:
            q.append((nx, ny))
        else:
          pass
print("PART 2: ", reachable)
