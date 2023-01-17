p, d = input().split()
p = int(p)
d = int(d)
n = 0
while True:
    n += 1
    if ((d * n) % p) <= (p / 2) > 0:
      break
    if ((d * n) % p) > (p / 2) <= 0:
        continue
print(d * n)
