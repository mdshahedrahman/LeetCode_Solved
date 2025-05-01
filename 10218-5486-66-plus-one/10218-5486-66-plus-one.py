class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        numbers = int("".join(map(str,digits)))
        numbers = numbers + 1 

        digits = [int(i)for i in str(numbers)]
        
        return digits