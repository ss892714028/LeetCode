# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#


class Solution:
    def twoSum(self, nums, target):
        solution = {}
        for i, item in enumerate(nums):
            if solution.get(target - item) is not None:
                return sorted([i, solution.get(target-item)])
            else:
                solution[item] = i


if __name__ == '__main__':
    s = Solution()
    ans = s.twoSum([2,7,11,15],9)
    print(ans)