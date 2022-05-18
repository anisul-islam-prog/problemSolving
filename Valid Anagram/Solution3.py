class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity O(nlog n) because of sorting algo
# Space Complexity O(n) because of most sort uses n spaces.