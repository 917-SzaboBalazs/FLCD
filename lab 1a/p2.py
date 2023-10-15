# Sort 3 numbers

a = input()
b = input()
c = input()

a = int(a)
b = int(b)
c = int(c)

tmp = 0

if a > b:
  tmp = a
  a = b
  b = tmp

if b > c:
  tmp = b
  b = c
  c = tmp

if a > b:
  tmp = a
  a = b
  b = tmp

print(a)
print(b)
print(c)