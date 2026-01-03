# Problem: Two Sum (LeetCode 1)
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
            return [mp[diff], i]
        mp[num] = i
