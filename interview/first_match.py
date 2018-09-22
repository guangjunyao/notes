"""
给定文本字符串text, 和模式串pattern, 从text中找出模式串第一次出现的位置。
"""


def brute_force_search(text, pattern):
    len_t = len(text)
    len_p = len(pattern)
    i = 0
    j = 0
    while i < len_t and j < len_p:
        if text[i + j] == pattern[j]:
            j += 1
        else:
            i += 1
            j = 0
    if j >= len_p:
        return i


a = 'abcdefg'
b = 'def'
print(brute_force_search(a, b))
