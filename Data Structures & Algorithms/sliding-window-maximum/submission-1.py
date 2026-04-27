class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        que = deque()
        output = []

        left = 0

        for right in range(len(nums)):
            while que and nums[que[-1]] <  nums[right]:
                que.pop()
            que.append(right)

            if left > que[0]:
                que.popleft()

            if right >= k - 1:
                output.append(nums[que[0]])
                left += 1

        return output
