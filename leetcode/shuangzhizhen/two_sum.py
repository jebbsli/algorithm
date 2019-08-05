
numbers = [2, 7, 11, 15]


def two_sum(num_list, target):
    """
    在有序数组中找出两个数，使它们的和为 target。
    :param num_list:
    :param target:
    :return:
    """
    if len(num_list) < 2:
        return None

    left = 0
    right = len(num_list) - 1
    while left < right:
        num = num_list[left] + num_list[right]
        if num == target:
            return num_list[left], num_list[right]
        elif num < target:
            left += 1
        else:
            right -= 1

    return None


if __name__ == '__main__':
    result = two_sum(numbers, 18)
    if result:
        print("Num:", result)
    else:
        print("Not Found.")
