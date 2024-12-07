from copy import deepcopy

ex_inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = ex_inp

board = [
  list(l)
  for l in inp.split("\n")
]
directions = ["^", ">", "v", "<"]

##################
# PART 1
##################
xp, yp, pos = -1, -1, None
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] in directions:
      xp, yp, pos = x, y, directions.index(board[x][y])
      break
  if pos is not None:
    break
print(f"[PART 1] start: {(xp, yp, pos)=}")

total = 0
while 0 <= xp < len(board) and 0 <= yp < len(board[0]):
# while total < 4:
  xn, yn = xp, yp
  if pos == 0:
    xn -= 1
  elif pos == 1:
    yn += 1
  elif pos == 2:
    xn += 1
  else:
    yn -= 1
    
  if not (0 <= xn < len(board)) or not (0 <= yn < len(board[0])):
    if board[xp][yp] != 'X':
      total += 1
      board[xp][yp] = 'X'
    break
  
  if board[xn][yn] == '#':
    pos = (pos + 1) % 4
  else:
    if board[xp][yp] != 'X':
      total += 1
      board[xp][yp] = 'X'
    xp, yp = xn, yn

print("\n".join(["".join(l) for l in board]))
print("PART1:", total)

##################
# PART 2
##################

board = [
  list(l)
  for l in inp.split("\n")
]
directions = ["^", ">", "v", "<"]

xp, yp, pos = -1, -1, None
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] in directions:
      xp, yp, pos = x, y, directions.index(board[x][y])
      break
  if pos is not None:
    break
print(f"[PART 2] start: {(xp, yp, pos)=} \n {board}")

board_templ = deepcopy(board)
board_templ[xp][yp] = '.'
board_cur = deepcopy(board)
total = 0
res = []
while True:
  xn, yn = xp, yp
  dxr, dyr = xp, yp
  if pos == 0:
    xn -= 1
    dyr += 1
  elif pos == 1:
    yn += 1
    dxr -= 1
  elif pos == 2:
    xn += 1
    dyr -= 1
  else:
    yn -= 1
    dxr += 1
  
  # break if out of map
  if not (0 <= xn < len(board_cur)) or not (0 <= yn < len(board_cur[0])):
    break
  
  print("\n".join(["".join(l) for l in board_cur]), end="\n\n")
  xr, yr = xp, yp
  while (0 <= xr < len(board_cur)) and (0 <= yr < len(board_cur[0])):
    if board_cur[xr][yr] == directions[(pos + 1) % 4]:
      res.append((xp, yp))
    elif board_cur[xr][yr] == '#':
      break
    xr += dxr
    yr += dyr
  
  next_v = board_cur[xn][yn]
  if next_v == '#':
    pos = (pos + 1) % 4
  else:
    board_cur[xp][yp] = directions[pos]
    xp, yp = xn, yn
print("PART2:", res)
