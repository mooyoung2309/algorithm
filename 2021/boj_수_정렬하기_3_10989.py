import sys

N = int(sys.stdin.readline())

nums = [] * 10001
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for i in nums:
    print(i)
