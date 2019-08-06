"""
given_s = "leetcode"
return_s = "leotcede
"""

# 元音字母
yuan_s = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def reverse_vowels(s: str):
    """
    使用双指针指向待反转的两个元音字符，一个指针从头向尾遍历，一个指针从尾到头遍历。
    :param s:
    :return:
    """
    left = 0
    right = len(s) - 1

    result_s = list(s)
    while left <= right:
        lc = s[left]
        rc = s[right]

        if lc not in yuan_s:
            result_s[left] = lc
            left += 1
        elif rc not in yuan_s:
            result_s[right] = rc
            right -= 1
        else:
            result_s[left] = rc
            result_s[right] = lc
            left += 1
            right -= 1

    return ''.join(result_s)


if __name__ == '__main__':
    given_s = "leetcode"
    result = reverse_vowels(given_s)
    print("Before:", given_s)
    print("After:", result)

