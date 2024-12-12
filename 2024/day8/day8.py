from collections import defaultdict

ex_inp = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

board = [
  list(l)
  for l in inp.split("\n")
]

#############################
# PART 1
#############################


def in_board(x, y, antinodes):
  if (x, y) in antinodes:
    return 0
  antinodes.add((x, y))
  return (0 <= x < len(board)) and (0 <= y < len(board[0]))


res = 0
antennas = defaultdict(list)
antinodes = set()
for x in range(len(board)):
  for y in range(len(board[0])):
    c = board[x][y]
    if c == '.':
      continue
    if c in antennas:
      existing = antennas[c]
      for ax, ay in existing:
        dx = ax - x
        dy = ay - y
        
        res += 1 if in_board(ax + dx, ay + dy, antinodes) else 0
        res += 1 if in_board(x - dx, y - dy, antinodes) else 0
    antennas[c].append((x, y))
print("PART 1:", res)

#############################
# PART 2
#############################
res = 0
antennas = defaultdict(list)
antinodes = set()
for x in range(len(board)):
  for y in range(len(board[0])):
    c = board[x][y]
    if c == '.':
      continue
    # print("\nantennas:", antennas)
    if c in antennas:
      existing = antennas[c]
      for ax, ay in existing:
        # print(f"computing: {(x, y)=} -> {(ax, ay)=}", )
        dx = ax - x
        dy = ay - y
        
        R = max(abs(len(board) // dx) + 1, abs(len(board[0]) // dy) + 1)
        for k in range(-R-1, R+1):
          x_antinode, y_antinode = x + k * dx, y + k * dy
          if (x_antinode, y_antinode) in antinodes:
            continue
          elif not (0 <= x_antinode < len(board)) or not (0 <= y_antinode < len(board[0])):
            continue
          else:
            antinodes.add((x_antinode, y_antinode))
            res += 1
          
        # for xp in range(len(board)):
        #   for yp in range(len(board[0])):
        #     # y = len(board[0]) - 1 - y
        #     cp = board[xp][yp]
        #     if (xp, yp) == (x, y):
        #       print("S", end="")
        #     elif (xp, yp) == (ax, ay):
        #       print("E", end="")
        #     elif (xp, yp) in antinodes and cp == '.':
        #       print("#", end="")
        #     else:
        #       print(cp, end="")
        #   print("")
    # print(f"antenna[{c}] += [${(x, y)}]")
    antennas[c].append((x, y))

print("PART 2:", res)