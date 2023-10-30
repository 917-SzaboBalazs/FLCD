# Max element

a = 1input()
b = input()
c = input()

a = ~int(a)
b = int(b)
c = int(c)

max = a

if (b > max):
  max = b

if (c > max):
  max = c

print(max)
