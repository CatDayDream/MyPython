"""
！重要题，每年必出
在归并排序的过程中对算法进行一个深度优化可以用于求小和
等价于求有多少个逆序对
"""


def merge_sort(s):
    """归并排序"""
    n = len(s)
    # 拆分到剩一个或没有直接返回，不用排序
    if n < 2:
        return
    # 将输入的s拆分
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    # 子序列递归调用排序
    merge_sort(s1)
    merge_sort(s2)
    # 合并
    merge(s1, s2, s)
    print(s)


def merge(s1, s2, s):
    """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
    # j和i就相当于两个指向的位置，i指s1，j指s2
    global small_sum
    i = j = 0
    while i+j < len(s):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            small_sum += (len(s2) - j) * s1[i]
            print(small_sum)
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


if __name__ == '__main__':
    small_sum = 0
    s = [5, 8, 9, 22, 42, 21, 1, 2, 67, 11, 3, 45]
    merge_sort(s)
    print("sorted array: " + str(s))
    print("small sum: " + str(small_sum))
