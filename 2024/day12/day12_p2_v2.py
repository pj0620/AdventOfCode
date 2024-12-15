import numpy as np
from scipy import ndimage, signal

np.set_printoptions(precision=2, suppress=True)

ex_inp = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

board = [
  l for l in inp.split("\n")
]

#################################
# PART 2
#################################

letters = list(set(inp))
letters.remove('\n')
boards = []
for letter in letters:
  new_board = [[0] * (len(board[0]) + 2)]
  for i in range(len(board)):
    new_board.append([0] + [
      1 if y == letter else 0
      for y in board[i]
    ] + [0])
  new_board += [[0] * (len(board[0]) + 2)]
  boards.append(np.array(new_board).astype(np.float64))

UL = np.array([[1, -0.333], [-0.333, -0.333]]).astype(np.float64)
UR = np.array([[-0.333, 1], [-0.333, -0.333]]).astype(np.float64)
DL = np.array([[-0.333, -0.333], [1, -0.333]]).astype(np.float64)
DR = np.array([[-0.333, -0.333], [-0.333, 1]]).astype(np.float64)

D1 = np.array([[0.5, -0.5], [-0.5, 0.5]]).astype(np.float64)
D2 = np.array([[-0.5, 0.5], [0.5, -0.5]]).astype(np.float64)

corners_map = {}
for letter, board_arr in zip(letters, boards):
  corners = np.zeros(shape=(len(board), len(board[0])))
  
  # corners
  res = ndimage.convolve(board_arr, UL, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[:-2,:-2]
  
  res = ndimage.convolve(board_arr, UR, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[:-2, 1:-1]

  res = ndimage.convolve(board_arr, DL, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[1:-1, :-2]

  res = ndimage.convolve(board_arr, DR, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[1:-1, 1:-1]
  
  # cross
  res = ndimage.convolve(board_arr, D1, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  fixed_res_1 = masked[1:-1, 1:-1]
  fixed_res_2 = masked[:-2, :-2]
  corners += fixed_res_1 + fixed_res_2
  
  res = ndimage.convolve(board_arr, D2, mode='constant', cval=0.0)
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  fixed_res_1 = masked[1:-1, :-2]
  fixed_res_2 = masked[:-2, 1:-1]
  corners += fixed_res_1 + fixed_res_2
  
  # corners flipped
  res = signal.convolve2d(board_arr, -UL, boundary='fill', mode='same')
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[2:, 2:]
  
  res = signal.convolve2d(board_arr, -DR, boundary='fill', mode='same')
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[1:-1, 1:-1]
  
  res = signal.convolve2d(board_arr, -UR, boundary='fill', mode='same')
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[2:,1:-1]
  
  res = signal.convolve2d(board_arr, -DL, boundary='fill', mode='same')
  masked = np.where(np.isclose(res, 1.0, atol=0.1), 1, 0)
  corners += masked[1:-1, 2:]
  
  corners_map[letter] = corners

visited = set()
ans = 0
for x in range(len(board)):
  for y in range(len(board[0])):
    if (x, y) in visited:
      continue
    plant = board[x][y]
    corners = corners_map[plant]
    corner_count = 0
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
        q.append((xn1, yn1))
      
      corner_count += int(corners[xc, yc])
      area += 1
    ans += corner_count * area
print("part 2:", ans)