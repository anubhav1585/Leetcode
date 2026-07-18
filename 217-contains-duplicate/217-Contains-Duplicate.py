class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        found = bool
        for i in nums:
            if i in seen:    
                found = True
                break
            else:    
                found = False

            seen.add(i)
           
        
        return found

                    

        