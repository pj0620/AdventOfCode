from dataclasses import dataclass
from typing import Self

ex_inp = """15 17"""

with open('inp.txt', 'r') as f:
  r_inp = f.read()

inp = r_inp

@dataclass
class LLNode:
  val: int
  next: Self | None
  
  def __str__(self):
    print("in __str__")
    ans = str(self.val)
    if self.next:
      if self.next == self:
        ans += ", <loop>"
      else:
        ans += ", " + str(self.next)
    return ans
  
  def __len__(self):
    if self.next:
      return 1 + len(self.next)
    else:
      return 1

# Build LL
head = None
cur = None
for x in inp.split(" "):
  if not head:
    head = LLNode(int(x), None)
    cur = head
  else:
    new_node = LLNode(int(x), None)
    cur.next = new_node
    cur = cur.next
    
for itx in range(25):
  # print("in loop", itx)
  last = None
  cur = head
  while cur:
    if cur.val == 0:
      # print("val == 0")
      cur.val = 1
      last = cur
    elif len(str(cur.val)) % 2 == 0:
      # print("val % 2 == 0")
      str_val = str(cur.val)

      l_val = int(str_val[:len(str_val) // 2])
      r_val = int(str_val[len(str_val) // 2:])

      l_node = LLNode(int(l_val), None)
      r_node = LLNode(int(r_val), None)

      if last:
        last.next = l_node
      else:
        head = l_node

      l_node.next = r_node

      last = r_node
    else:
      # print("else")
      cur.val *= 2024
      last = cur
    cur = cur.next
    last.next = cur
  print("printing head")
  # print(str(head))



# print(len(head))