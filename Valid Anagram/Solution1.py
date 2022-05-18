class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # Declaring hasmap to store char count of S & T
        countS, countT = {}, {}

        # Count Number of characters in S & T
        for i in range(len(s)):
            # .get for fetching value against key and 0 is default if key does not exists
            countS[s[i]] = 1+countS.get(s[i], 0)
            countT[t[i]] = 1+countT.get(t[i], 0)
        # Comparing char count of S & T
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

# Time Complexity O(n) because iterating over all n times of string
# Space Complexity O(n) because of hashmap
