a = int(input())
b = set(input().split())


c = int(input())
d = set(input().split())

x = set(b) & set(d)
print(len(x))
