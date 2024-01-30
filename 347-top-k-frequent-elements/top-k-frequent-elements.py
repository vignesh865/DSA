import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def new_cmp_lt(a,b):
            return a[1]<b[1]

#override the existing "cmp_lt" module function with your function
        heapq.cmp_lt=new_cmp_lt

        freq = {}

        for num in nums:

            freq[num] = freq.get(num, 0) - 1

        h = []

        for i in freq.items():
            heapq.heappush(h, (i[1], i[0]))
        return [heapq.heappop(h)[1] for _ in range(k)]

        