class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
# Time complexity O(n) because of iteration the list n times. Adding and finding element in hashmap is O(1)
# Space complexity O(n) because of hashmap takes up n spaces
