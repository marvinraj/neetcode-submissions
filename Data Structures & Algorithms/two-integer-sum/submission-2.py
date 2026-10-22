class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store length of nums
        numsLen = len(nums)
        # dict to store seen numbers and its index
        seen = {}

        for i in range(numsLen):
            # current value using current index
            num = nums[i]
            # complement of the current value and targe
            c = target - num
            
            #if complement in seen, dict, get the value and its index
            if c in seen:
                return [seen[c], i]
            seen[num] = i