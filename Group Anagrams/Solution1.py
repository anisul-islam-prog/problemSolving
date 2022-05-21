class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        mapping char counts in the list of anamgrams. defaultdict(list) is used to if the key does not exists, it will add a default.
        """
        result = defaultdict(list) 
        for s in strs: 
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c)-ord("a")] += 1 
                
            result[tuple(count)].append(s)
        # print(result)
        return result.values()

""" 
Time complexity O(m*n*26) => O(m*n), m = number of strings in list; n= number of characters in a string
Space complexity  O(n)
"""