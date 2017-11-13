import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = -sys.maxsize
        second_max =-sys.maxsize
        third_max = -sys.maxsize
        for i in nums:
            if(i> first_max):
                third_max = second_max
                second_max = first_max
                first_max = i
            elif i == first_max:
                pass
            elif i > second_max:
                third_max = second_max
                second_max = i
            elif i == second_max:
                pass
            elif i> third_max:
                third_max  = i
        print(third_max,second_max,first_max)
        if third_max == -sys.maxsize:
            return first_max
        else:
            return third_max

sol = Solution()
print(sol.thirdMax([1,2]))
print(sol.thirdMax([3,3, 2, 1]))
print(sol.thirdMax([3, 2,2, 1]))
print(sol.thirdMax([3, 2, 1]))

