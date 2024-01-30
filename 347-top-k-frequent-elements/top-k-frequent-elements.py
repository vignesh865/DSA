import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        h = []

        k_largest = heapq.nlargest(k, freq, key=freq.get)
        return k_largest
