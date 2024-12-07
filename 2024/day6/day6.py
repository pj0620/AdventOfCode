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

inp = r_inp

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

visited = set()
total = 0
while 0 <= xp < len(board) and 0 <= yp < len(board[0]):
  visited.add((xp, yp))
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
x_start, y_start, pos_start = xp, yp, pos

def hits_loop(board_inp):
  visited_2 = set()
  xp, yp, pos = x_start, y_start, pos_start
  while 0 <= xp < len(board_inp) and 0 <= yp < len(board_inp[0]):
    if (xp, yp, pos) in visited_2:
      return True
    visited_2.add((xp, yp, pos))
    xn, yn = xp, yp
    if pos == 0:
      xn -= 1
    elif pos == 1:
      yn += 1
    elif pos == 2:
      xn += 1
    else:
      yn -= 1
    
    if not (0 <= xn < len(board_inp)) or not (0 <= yn < len(board_inp[0])):
      return False
    
    if board_inp[xn][yn] == '#':
      pos = (pos + 1) % 4
    else:
      xp, yp = xn, yn
  return False

board_templ = deepcopy(board)
board_templ[x_start][y_start] = '.'
res = 0
for x, y in visited:
  board_templ[x][y] = "#"
  if hits_loop(board_templ):
    res += 1
  board_templ[x][y] = "."
print("PART2:", res)
