import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = map(int, input().split())
lspeed = []
bspeed = []

for i in range(n):
    x, l = map(int, input().split())
    for i in range(x):
        lspeed.append(l)

for i in range(m):
    y, b = map(int, input().split())
    for i in range(y):
        bspeed.append(b)

ospeed = 0

for i in range(100):
    if bspeed[i] > lspeed[i] and bspeed[i] - lspeed[i] > ospeed:
        ospeed = bspeed[i] - lspeed[i]

print(ospeed)
