def mutiple_table():
    # 九九乘法表
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # \t：转义字符，协助文本在输出时垂直方向保持对齐
            print("%d*%d=%d" % (col, row, col * row), end="\t")
            col += 1
        print("")  # 目的：就是在一行星星输出后，添加换行！
        row += 1


mutiple_table()
