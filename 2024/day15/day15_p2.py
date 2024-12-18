from typing import Tuple, List

inp = None
with open('r_inp.txt', 'r') as f:
  inp = f.readlines()

##############################
# PART 2
##############################

# parse input
board = []
actions = []
ox, oy = -1, -1
in_board = True
mapping = {
  '#': '##',
  'O': '[]',
  '.': '..',
  '@': '@.',
}
for l in inp:
  if l == '\n':
    in_board = False
    continue
  row = []
  for c in l:
    if c == '\n':
      continue
    if in_board:
      for q in mapping[c]:
        row.append(q)
    else:
      actions += [c]
  if in_board:
    board.append(row)


def print_board():
  global board
  print("### Board ###")
  for x in range(len(board)):
    for y in range(len(board[0])):
      print(board[x][y], end="")
    print("")


print_board()
print(actions)

# find character start position
ox, oy = -1, -1
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] == '@':
      ox, oy = x, y


def is_clear(x, y, dx, dy, visited=None) -> Tuple[bool, List[Tuple[int, int]]]:
  global board
  visited = visited if visited else set()
  if (x, y) in visited:
    return True, []
  # visited.add((x, y))
  c = board[x][y]
  if c == '.':
    return True, []
  elif c == '#':
    return False, []
  if c in ['[', ']']:
    if dx == 0:
      is_clear_next, next_vals = is_clear(x, y + dy, 0, dy, visited)
      return is_clear_next, [(x, y)] + next_vals
    else:
      # implies -> dy == 0
      is_clear_next_1, next_vals_1 = True, []
      is_clear_next_0, next_vals_0 = is_clear(x + dx, y, dx, 0, visited)
      if not is_clear_next_0:
        return False, []
      if c == '[' and 1 <= y + 1 < len(board[0]) - 1:
        is_clear_next_1, next_vals_1_r = is_clear(x + dx, y + 1, dx, 0, visited)
        next_vals_1 += next_vals_1_r
        next_vals_1 += [(x, y + 1)]
      elif c == ']' and 1 <= y - 1 < len(board[0]) - 1:
        is_clear_next_1, next_vals_1_r = is_clear(x + dx, y - 1, dx, 0, visited)
        next_vals_1 += next_vals_1_r
        next_vals_1 += [(x, y - 1)]
      return is_clear_next_1, next_vals_0 + next_vals_1 + [(x, y)]


# clear, points = is_clear(ox - 1, oy, -1, 0)
# print(f"{(clear, points)=}")

diff_map = {
  '>': (0,  1),
  '^': (-1, 0),
  '<': (0, -1),
  'v': (1, 0)
}
# print("\n\n MAin")
# print_board()
for a in actions:
  # print_board()
  # print("a =", a)
  dx, dy = diff_map[a]
  nx, ny = ox + dx, oy + dy
  if board[nx][ny] == '.':
    board[nx][ny] = '@'
    board[ox][oy] = '.'
    ox, oy = nx, ny
  elif board[nx][ny] in ['[', ']']:
    # print("board[nx][ny]:", board[nx][ny])
    clear, points = is_clear(nx, ny, dx, dy)
    if clear:
      # print(points)
      points_sorted = sorted(list(set(points)), key=lambda p: -abs(p[0] - ox) if dx != 0 else -abs(p[1] - oy))
      # print(points_sorted)
      for px, py in points_sorted:
        board[px + dx][py + dy] = board[px][py]
        board[px][py] = '.'
      board[nx][ny] = '@'
      board[ox][oy] = '.'
      ox, oy = nx, ny
  # print_board()
  # print("\n")

res = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] == '[':
      res += 100 * x + y
# print_board()
print("PART 2", res)