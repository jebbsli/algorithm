"""
回文字符串
Input: "abca"
Output: True
"""


def judge(s: str, left: int, right: int):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right += 1

    return True


def valid_palindrome(s: str):
    """
    可以删除一个字符，判断是否能构成回文字符串
    :param s:
    :return:
    """
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return judge(s, left, right - 1) or judge(s, left + 1, right)
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    result = valid_palindrome('abca')
    print("Result:", result)
