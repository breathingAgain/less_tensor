
#!/usr/bin/env python
import random
a = set()
b = set()
for i in range(0, 15):
    a.add(random.randint(0, 100))
    b.add(random.randint(0, 100))
print(a)
print(b)

inp = a & b
print(inp)

inp = a - b
print(inp)

inp = b - a
print(inp)

inp = a ^ b
print(inp)
