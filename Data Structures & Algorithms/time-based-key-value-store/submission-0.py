class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return  ""

        # Find the nearest  stored time to timestamp

        pairs = self.time_dict[key]

        result = ""

        left = 0
        right = len(pairs) - 1

        while left <= right:
            mid = left + (right - left)//2

            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
           

        return result
