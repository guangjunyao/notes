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


text = 'abxabcabcabyabcaby'
pattern = 'abcaby'
print(brute_force_search(text, pattern))


def suffix_prefix_matching(pattern):
    temp = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = temp[j - 1]
        if pattern[i] == pattern[j]:
            temp[i] = j + 1
            j += 1
        else:
            if j != 0:
                j = temp[j - 1]
            else:
                temp[i] = 0
    return temp


partial_array = suffix_prefix_matching(pattern)
print('array for suffix==prefix', partial_array)
len_t = len(text)
len_p = len(pattern)
i = 0
j = 0
count = 0
match = []
for i in range(1, len_t):
    while j > 0 and text[i] != pattern[j]:
        j = partial_array[j - 1]

    if text[i] == pattern[j]:
        j += 1
        count += 1
    if j == len_p:
        match.append(i - j + 1)
        j = 0
print(match)
