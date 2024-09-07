"""
一个数组里有一个数字是奇数次个数，找出这个数
"""
a = [1, 1, 1, 1, 2, 2, 3, 3, 3]

num = 0
for i in range(len(a)):
    num ^= a[i]

print(num)

"""
一个数组里有两个数字是奇数次个数，找出这个数
"""
b = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
eor = 0
for j in range(len(b)):
    eor ^= b[j]  # eor 为两个奇数次数的异或

rightone = eor & (~eor + 1)  # 得到eor最右边的1,~符号将二进制数取反,将其+1,再与原值与运算可以得出该值最右边1的位置，可以用于值标记
onlyone = 0

for cur in b:
    if cur & rightone == 1:
        onlyone ^= cur

leftone = eor ^ onlyone
print(onlyone)
print(leftone)
