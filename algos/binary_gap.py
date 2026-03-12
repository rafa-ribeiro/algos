"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded
by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
- The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
- The number 20 has binary representation 10100 and contains one binary gap of length 1.
- The number 15 has binary representation 1111 and has no binary gaps.
- The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.
"""

"""
Algorithm:

Case 1:
Input: 529 ->  binary '1000010001'
Output: 4

Case 2:
Input: 3 ->  binary '0011'
Output: 0

Case 3:
Input: ? ->  binary '100010'
Output: 3

Case 4:
Input: 15 ->  binary '1111'
Output: 0

Case 5:
Input: 5 ->  binary '101'
Output: 1

"""

# O(N)
def get_maximum_gap_size(num: int):
    binary_num = convert_num_to_binary_string(num=num)

    i = 0
    size = len(binary_num)
    max_gap = 0
    inc = 0
    while i < size:
        if binary_num[i] == '1':
            if inc > max_gap:
                max_gap = inc
            inc = 0
        elif binary_num[i] == '0':
            inc += 1

        i += 1

    return max_gap


def convert_num_to_binary_string(num: int) -> str:
    # return str(bin(num)[2:])
    bin_num = ''
    quotient = 1
    curr_num = num
    while quotient:
        quotient = curr_num // 2
        remainder = curr_num % 2
        curr_num = quotient
        bin_num = str(remainder) + bin_num

    return bin_num


n = 529
result = get_maximum_gap_size(num=n)
print(result)
