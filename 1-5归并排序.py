"""
<归并排序>
时间复杂度:0(N*logN)
额外空间复杂度:O(N)
计算复杂度引入master公式T(N) = a*T(N/b) + O(N^d)
(母问题是N的规模,子问题是N/b的规模,a指的是子问题被调用了多少次,剩下的就是其他过程的复杂度)
1) log(b,a) > d --> O(N^log(b, a)
2) log(b,a) = d --> O(N^d * logN)
3) log(b,a) < d --> O(N^d)
对于归并排序,a=2,b=2,d=1,log(b,a)=d,采用公式 2
用递归以空间换时间，时间复杂度降低，后序遍历二叉树
主要原因是这种方式没有浪费比较行为，只是变成了更大的部分与下一部分进行排序，因此时间复杂度降低
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
    i = j = 0
    while i+j < len(s):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


if __name__ == '__main__':
    s = [5, 8, 9, 22, 42, 21, 1, 2, 67, 11, 3, 45]
    merge_sort(s)
    print(s)
