a = int(input())
b =[]
while a > 0:
  m = input()
  b.append(m)
  a -= 1

c = set(b)
print(len(c))
