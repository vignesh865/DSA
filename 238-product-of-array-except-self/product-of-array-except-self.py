class Solution:

    def forward_sum(self, nums, i, sum_array):

        if i == len(nums)-1:
            sum_array.append(1)
            return 1
        
        sum = self.forward_sum(nums, i+1, sum_array)* nums[i+1]
        sum_array.insert(0, sum)
        return sum

    # def reverse_sum(self, nums, i, sum_array):

    #     if i == 0:
    #         sum_array.append(1)
    #         return 1
        
    #     sum = self.reverse_sum(nums, i-1, sum_array)* nums[i-1]
    #     sum_array.append(sum)
    #     return sum


    def reverse_sum(self, nums, i, sum_array):

        if i == 0:
            sum_array[i] = sum_array[i]*1
            return 1
        
        sum = self.reverse_sum(nums, i-1, sum_array)* nums[i-1]
        sum_array[i] = sum_array[i]*sum
        return sum

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # forward_sum = [1]
        # i = 1
        # while i < len(nums):
        #     forward_sum.append(forward_sum[i-1]*nums[i])
        #     i+=1

        # reverse_sum = [1]
        # i = len(nums)-2
        # while i > 0:
        #     reverse_sum.insert(reverse_sum[0]*nums[i], 0)
        #     i-=1

        forward_sum_arr = []
        self.forward_sum(nums, 0, forward_sum_arr)
        reverese_sum_arr = []
        self.reverse_sum(nums, len(nums)-1, forward_sum_arr)
        print(forward_sum_arr, reverese_sum_arr)

        return forward_sum_arr
