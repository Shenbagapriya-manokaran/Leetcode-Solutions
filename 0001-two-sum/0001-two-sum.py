class Solution:
     def twoSum(self, nums: List[int],         target: int) -> List[int]:

      for i in range(0, len (nums)):
         for j in range(i+1,len(nums)):

           temp = nums[i] + nums[j]

           if temp == target:

                return ([i,j])
        