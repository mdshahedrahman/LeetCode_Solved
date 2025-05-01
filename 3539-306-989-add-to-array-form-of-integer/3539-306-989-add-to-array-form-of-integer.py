class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(num) -1, -1, -1):
            if i >= 0: 
                k += num[i]
                res.append(str(k%10))
                k = k//10

        if k > 0: 
            res.append(str(k))   
        
        res = ''.join(reversed(res))
        return [int(i) for i in str(res)]


