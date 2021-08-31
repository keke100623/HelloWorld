"""
def sum_2_sum():
    """"""
    num1 = int(input("请输入数字一："))
    num2 = int(input("请输入数字二："))
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_sum()
"""

"""
def sum_2_sum(num1, num2):
    """"""
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_sum(10, 20)
"""


def sum_2_sum(num1, num2):
    """对两个数字求和"""
    return num1 + num2


sum_result = sum_2_sum(10, 20)
print("计算结果：%d" % sum_result)
