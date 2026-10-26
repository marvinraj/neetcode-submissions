class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for x in nums:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1
        
        sorted_seen = sorted(seen, key=seen.get, reverse=True)
        
        return sorted_seen[:k]