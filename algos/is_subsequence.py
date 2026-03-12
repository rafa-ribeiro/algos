"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
 positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

"""
Case 1
t = "ahbgdc"
s = "abc"
Expected = True

Case 2
t = "ahbgdc"
s = "acb"
Expected = False

Case 3
t = "abcd"
s = "abcd"
Expected = True

Case 4
t = "abc"
s = "abcd"
Expected = False

Case 5
t = "abb"
s = "ab"
Expected = True

Algorithm:

pointer_s e pointer_t
while pointer_s < size_s and pointer_t < size_t
    if t[pointer_t] == s[pointer_s]:
        pointer_s++

return pointer_s == size_s
"""


def is_subsequence(s: str, t: str) -> bool:
    size_s, size_t = len(s), len(t)
    if size_t < size_s:
        return False

    pointer_s, pointer_t = 0, 0
    while pointer_s < size_s and pointer_t < size_t:
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1

        pointer_t += 1

    return pointer_s == size_s
