problems = input().split(";")
num = 0

for c in problems:
    if '-' in c:
        nums = c.split('-')
        num += (int(nums[1]) - int(nums[0]) + 1)
    else:
        num += 1

print(num)

