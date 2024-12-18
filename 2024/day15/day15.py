inp = None
with open('r_inp.txt', 'r') as f:
  inp = f.readlines()

##############################
# PART 1
##############################

# parse input
board = []
actions = []
ox, oy = -1, -1
in_board = True
for l in inp:
  if l == '\n':
    in_board = False
    continue
  if in_board:
    board.append(list(l[:-1]))
  else:
    actions += list(l[:-1])

# find character start position
ox, oy = -1, -1
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] == '@':
      ox, oy = x, y

def print_board():
  global board
  print("### Board ###")
  for x in range(len(board)):
    for y in range(len(board[0])):
      print(board[x][y], end="")
    print("")

diff_map = {
  '>': (0,  1),
  '^': (-1, 0),
  '<': (0, -1),
  'v': (1, 0)
}
for a in actions:
  dx, dy = diff_map[a]
  nx, ny = ox + dx, oy + dy
  if board[nx][ny] == '.':
    board[nx][ny] = '@'
    board[ox][oy] = '.'
    ox, oy = nx, ny
  elif board[nx][ny] == 'O':
    sx, sy = nx, ny
    while board[sx][sy] == 'O':
      sx += dx
      sy += dy
    if board[sx][sy] == '#':
      continue
    else:
      board[sx][sy] = 'O'
      board[nx][ny] = '@'
      board[ox][oy] = '.'
      ox, oy = nx, ny

res = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] == 'O':
      res += 100 * x + y
print_board()
print("PART 1", res)


