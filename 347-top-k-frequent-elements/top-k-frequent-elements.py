import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def new_cmp_lt(a, b):
            return a[1] < b[1]

        # # override the existing "cmp_lt" module function with your function
        # heapq.cmp_lt = new_cmp_lt

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        h = []

        k_largest = heapq.nlargest(k, freq, key=freq.get)
        return k_largest
