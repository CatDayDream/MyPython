"""
<冒泡排序>
每个i循环结束后，确定最右边的数
时间复杂度:0(N^2)
"""

a = [23, 64, 2, 7, 9, 332, 23, 42]
for i in range(len(a)):  # range左闭右开，遍历0-7的数
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)


# # 使用异或运算实现两个数交换
# def swap(a, b):
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
