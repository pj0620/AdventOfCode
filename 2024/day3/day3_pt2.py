ex_inp = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

###########################
# Part 1
###########################
tokens = []
cur = 0
while cur < len(inp):
  c = inp[cur]
  if c == 'm':
    if cur + 2 < len(inp) and inp[cur: cur + 3] == 'mul':
      tokens.append("mul")
      cur += 3
    else:
      cur += 1
  elif c == 'd':
    if cur + 5 < len(inp) and inp[cur: cur + 5] == "don't":
      tokens.append("don't")
      cur += 5
    elif cur + 1 < len(inp) and inp[cur: cur + 2] == "do":
      tokens.append("do")
      cur += 2
    else:
      cur += 1
  elif c in ['(', ')', ',']:
    tokens.append(c)
    cur += 1
  elif c.isnumeric():
    end = cur + 1
    while end < len(inp) and inp[end].isnumeric():
      end += 1
    tokens.append(inp[cur: end])
    cur = end
  else:
    cur += 1

print(tokens)
res = 0
cur = 0
enabled = True
while cur + 5 < len(tokens):
  if (tokens[cur] == 'mul' and tokens[cur + 1] == '('
      and tokens[cur + 2].isnumeric() and tokens[cur + 3] == ','
      and tokens[cur + 4].isnumeric() and tokens[cur + 5] == ')'):
    if enabled:
      res += int(tokens[cur + 2]) * int(tokens[cur + 4])
    cur += 6
  elif (tokens[cur] == 'do' and tokens[cur + 1] == '('
      and tokens[cur + 2] == ')'):
    enabled = True
    cur = cur + 3
  elif (tokens[cur] == "don't" and tokens[cur + 1] == '('
      and tokens[cur + 2] == ')'):
    enabled = False
    cur = cur + 3
  else:
    cur += 1
print(res)