for i in range(32):
    a = bin(i)
    print(a)
    a = a[2::]
    print(a.zfill(5))  # 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
    print(a.rjust(5))
    print(a.ljust(5))
    # ljust(width)和rjust(width)分别返回一个原字符串左（右）对齐,并使用空格填充至长度 width 的新字符串
