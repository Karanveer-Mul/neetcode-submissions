class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        fastest_rate = 0
        for i in range(len(piles)):
            fastest_rate = max(fastest_rate, piles[i])

        if h == len(piles):
            return fastest_rate
        
        slowest_rate = 1
        result = fastest_rate
        
        while slowest_rate <= fastest_rate:
            mid_rate = slowest_rate + (fastest_rate - slowest_rate)//2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/mid_rate)
            
            if total_hours <= h:
                result = mid_rate
                fastest_rate = mid_rate - 1
            else:
                slowest_rate = mid_rate + 1
                

        return result


