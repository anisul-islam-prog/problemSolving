class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

#Time Complexity O(n) due to iterating array of n times
#Space Complexity O(n) due to hashset takes upto memory of n elements