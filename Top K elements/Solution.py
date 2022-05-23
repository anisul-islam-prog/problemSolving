class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #to store count of the elements in num array
        #to store the freq of occurance of elem in num array
        freq= [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) #if n not found default 0
        for n, c in count.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
# Time complexity O(n) because of bucket sort
# if heap used then the time complexity would have been O(klogn)