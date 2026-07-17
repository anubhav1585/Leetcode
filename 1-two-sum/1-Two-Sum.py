class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    a.append(i)
                   

        return a

             