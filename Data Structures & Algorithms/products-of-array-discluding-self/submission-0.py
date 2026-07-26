class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first count number of 0's - 3 cases
        num_zeros = 0
        total_prod = 1
        for x in nums:
            if x==0: num_zeros+=1
            if x!=0:
                total_prod*=x
        out = []
        if num_zeros == 0:
            for i,x in enumerate(nums):
                out.append(total_prod // x)
        elif num_zeros == 1:
            for i,x in enumerate(nums):
                if x == 0:
                    out.append(total_prod)
                else:
                    out.append(0)
        elif num_zeros > 1:
            for i,x in enumerate(nums):
                out.append(0)

        return out
            