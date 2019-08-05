

def judge_square_sum(num):
    """
    判断一个数是否为两个数的平方和
    :param num:
    :return:
    """
    num1 = 0
    num2 = int(num ** 0.5)
    while num1 <= num2:
        pow_sum = num1 ** 2 + num2 ** 2
        if pow_sum == num:
            print("The two numbers: ", num1, num2)
            return True
        elif pow_sum > num:
            num2 -= 1
        else:
            num1 += 1

    return False


if __name__ == '__main__':
    result = judge_square_sum(34)
    print("Result:", result)
