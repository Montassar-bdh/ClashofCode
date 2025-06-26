"""
Solution for Missing digit problem: https://codingame.com/contribute/view/6934a6b6e14f2af545004ed4a8f3703180
Author: Montassar-bdh
"""
num = set('0123456789')

n = int(input())
for i in range(n):
    line = input()
    l = set(line)
    print((num - l).pop())
