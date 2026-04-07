class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        
        heap = []
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key, value in freq.items():
            
            heapq.heappush(heap, [value, key])

            if len(heap) > k:
                heapq.heappop(heap)
    
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
