"""
二分法除了用于查找，还能用于寻找局部最小
"""

a = [9, 8, 7, 2, 4, 6, 9, 2, 3, 5]

left = 0
right = len(a)-1
minimum = 0
while left <= right:
    middle = int(left + (right - left)/2)  # 直接使用(left+right)/2可能会溢出，用这种方法代替
    if a[middle] < a[middle-1] and a[middle] < a[middle + 1]:
        minimum = a[middle]
        break
    elif a[middle] > a[middle-1]:
        right = middle - 1
        print("right" + str(right))
    else:
        left = middle + 1
        print("left" + str(left))

print(minimum)
