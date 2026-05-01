class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n - 2, -1, -1 ):
            j = i+1

            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                j += result[j]

            if j < n and temperatures[i] < temperatures[j]:
                result[i] = j-i

        return result
