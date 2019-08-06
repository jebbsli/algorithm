"""
在有序数组中找出两个数，使它们的和为 target
"""
numbers = [2, 7, 11, 15]


def two_sum(num_list, target):
    """
    使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。

    如果两个指针指向元素的和 sum == target，那么得到要求的结果；
    如果 sum > target，移动较大的元素，使 sum 变小一些；
    如果 sum < target，移动较小的元素，使 sum 变大一些。
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
