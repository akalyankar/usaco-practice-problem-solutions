import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

lines = []

m, n, k = map(int, input().split())

for i in range(m):
    emptyline = ""
    line = input().strip()
    for ch in line:
        emptyline += ch * k
    for i in range(k):
        lines.append(emptyline)

for i in lines:
    print(i)
