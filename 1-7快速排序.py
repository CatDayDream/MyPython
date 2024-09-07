"""
<快速排序>
荷兰旗问题 快慢双指针+递归

"""


def quick_sort(arr, low, high):
    if low < high:  # 左侧向右排，右侧向左排
        pi = partition(arr, low, high)  # 得到划分位置
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr


def partition(arr, l, h):
    pivot = arr[l]  # 提前取出保存左指针位置值
    while l < h:  # 左右指针没有相遇则会继续遍历
        while l < h and arr[h] >= pivot:  # 右指针向左移动，找到值小于pivot时停下，并将左指针当前位置的值替换
            h -= 1
        arr[l] = arr[h]

        while l < h and arr[l] < pivot:  # 左指针向右移动，找到值大于pivot时停下，并将右指针当前位置的值替换
            l += 1
        arr[h] = arr[l]
    arr[l] = pivot  # 最后把pivot值赋给左指针当前位置
    print(arr)
    return l


if __name__ == '__main__':
    s = [5, 8, 9, 22, 42, 21, 1, 2, 672, 11, 3, 45, 22, 3]  # 待排数组
    sorted_array = quick_sort(s, 0, len(s)-1)
    print(sorted_array)
