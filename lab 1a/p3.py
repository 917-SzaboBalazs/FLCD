# Sum of n numbers
n = input()
arr = list()
sum = 0
x = 0
i = 0

n = int(n)

while (i < n):
  x = input()
  x = int(x)
  arr.append(x)
  i = i + 1

i = 0

while (i < n):
  sum = sum + arr[i]
  i = i + 1

print(sum)
