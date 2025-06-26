"""
Solution for Checklist problem: https://www.codingame.com/contribute/view/501632906b6e159b67a97979631262148ae8
Author: Montassar-bdh
"""
count = int(input())
for i in input().split():
    n = int(i)
    if n %2:
        print(f"[x] {n}")
    else:
        print(f"[ ] {n}")
