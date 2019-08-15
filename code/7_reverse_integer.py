# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
# Input: 123
# Output: 321
#
# Example 2:
# Input: -123
# Output: -321
#
# Example 3:
# Input: 120
# Output: 21


class Solution:
    def reverse(self, x):
        if x > 0:
            x = int(str(x)[::-1])

        else:
            x = -int(str(-x)[::-1])
        if x >= 2147483647 or x <= -2147483648:
            return 0
        else:
            return x


if __name__ == '__main__':
    s = Solution()
    ans = s.reverse(123)
    print(ans)
