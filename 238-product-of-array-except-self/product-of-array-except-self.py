class Solution:
    def forward_sum(self, nums, i, sum_array):
        if i == len(nums) - 1:
            sum_array.append(1)
            return 1

        sum = self.forward_sum(nums, i + 1, sum_array) * nums[i + 1]
        sum_array.insert(0, sum)
        return sum

    def reverse_sum(self, nums, i, sum_array):
        if i == 0:
            sum_array[i] = sum_array[i] * 1
            return 1

        sum = self.reverse_sum(nums, i - 1, sum_array) * nums[i - 1]
        sum_array[i] = sum_array[i] * sum
        return sum

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_sum_arr = []
        self.forward_sum(nums, 0, forward_sum_arr)
        self.reverse_sum(nums, len(nums) - 1, forward_sum_arr)

        return forward_sum_arr
