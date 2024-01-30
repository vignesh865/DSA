class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_d = {}
        for num in nums:
            if nums_d.get(num) is not None:
                return True
            nums_d[num] = 1
        return False
