ex_inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

#########################
# PART 1
#########################

board = [l for l in inp.split("\n")]
phrase = "XMAS"
def search(x, y, vect, cur):
  dx, dy = vect
  if phrase == cur:
    return 1
  elif not phrase.startswith(cur):
    return 0
  
  if not (0 <= x + dx < len(board)):
    return 0
  if not (0 <= y + dy < len(board[0])):
    return 0
  
  return search(x + dx, y + dy, vect, cur + board[x + dx][y + dy])


res = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if board[x][y] == 'X':
      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          if dx == dy == 0:
            continue
          S = search(x, y, (dx, dy), "X")
          res += S
          

print("part1: ", res)

#########################
# PART 2
#########################

check = lambda a, b: "".join(sorted([a, b])) == "MS"
res = 0
for x in range(1, len(board) - 1):
  for y in range(1, len(board[0]) - 1):
    if board[x][y] == 'A':
      ul = board[x - 1][y - 1]
      br = board[x + 1][y + 1]
      cond1 = check(ul, br)
      
      ur = board[x + 1][y - 1]
      bl = board[x - 1][y + 1]
      cond2 = check(ur, bl)
      res += 1 if cond1 and cond2 else 0

print("part2: ", res)