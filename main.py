from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1):
    for b in range(N - i - 1):
        if a[b] > a[b + 1]:
            a[b], a[b + 1] = a[b + 1], a[b]

print(a)