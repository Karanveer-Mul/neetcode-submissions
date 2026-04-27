class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        output = []

        for i in range(len(nums)):
            
            heapq.heappush(heap, [-nums[i], i])

            if i >= k-1: # First condition for the first window
                # Esentially lets the pile up heap then clears
                # any top element that is out of index
                while heap[0][1] <= i - k:  
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
