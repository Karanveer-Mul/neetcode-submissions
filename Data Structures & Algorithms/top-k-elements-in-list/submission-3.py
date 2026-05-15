class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        heap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        for key, value in freq.items():
            heapq.heappush(heap, [value, key])

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for item in heap:
            result.append(item[1])

        return result