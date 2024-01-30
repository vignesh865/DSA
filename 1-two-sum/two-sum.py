class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_d = {}

        for _, num in enumerate(nums):
            diff = target - num

            if sum_d.get(diff) is None:
                sum_d[num] = _
            else:
                return [sum_d[diff], _]
