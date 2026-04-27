class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():

            heapq.heappush(heap, [value, key])

            if len(heap) > k:
                heapq.heappop(heap)

        output = []

        for i in range(k):        
            output.append(heapq.heappop(heap)[1])

        return output