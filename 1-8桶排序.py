"""
<桶排序>不基于比较的排序，根据数据状况做的排序，根据数据状况定制，例如有进制的数字
逐一比较数字个十百位，进入桶队列，先进先出
统计个位，十位，百位的词频count进行入桶出桶+前缀和输出定位
本质也是用空间换时间
"""


def bucket_sort(s):
    str_length = len(s)
    d = 2
    while d >= 0:
        array = []
        for num in s:
            array.append(str(num).zfill(3))
        print(array)

        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(str_length):
            count[int(array[j][d])] += 1
        print(count)

        for i in range(1, 10):
            count[i] = count[i-1] + count[i]
        print(count)

        for k in range(str_length - 1, -1, -1):
            s[count[int(array[k][d])]-1] = int(array[k])
            print("遍历" + str(k), "数字位次" + str(d), s)
            count[int(array[k][d])] -= 1
        print(s)
        d -= 1


if __name__ == '__main__':
    s = [5, 8, 9, 22, 42, 21, 1, 2, 672, 11, 3, 45]
    bucket_sort(s)
