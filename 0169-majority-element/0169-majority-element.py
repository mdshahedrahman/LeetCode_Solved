class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        arr = {}

        for num in nums:
            arr[num] = arr.get(num, 0) + 1 
        
        return max(arr, key=arr.get)
