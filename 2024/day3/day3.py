ex_inp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

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

res = 0
cur = 0
while cur + 5 < len(tokens):
  if (tokens[cur] == 'mul' and tokens[cur + 1] == '('
    and tokens[cur + 2].isnumeric() and tokens[cur + 3] == ','
    and tokens[cur + 4].isnumeric() and tokens[cur + 5] == ')'):
    res += int(tokens[cur + 2]) * int(tokens[cur + 4])
    cur += 6
  else:
    cur += 1
print(res)