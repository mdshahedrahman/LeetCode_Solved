class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        arr = {}
        
        # 1. Count occurrences using if/else
        for num in nums:
            if num in arr:
                arr[num] = arr[num] + 1
            else:
                arr[num] = 1
                
        # 2. Find the key with the highest count using a loop
        max_count = 0
        majority_num = None
        
        for num, count in arr.items():
            if count > max_count:
                max_count = count
                majority_num = num
                
        return majority_num