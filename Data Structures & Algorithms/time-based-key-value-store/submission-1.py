class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)
        print(values)
        if not values:
            return ""
        
        start, end = 0, len(values)-1
        res = ""
        while start <= end:
            mid = (start + end)//2
            mid_timestamp, mid_value = values[mid]
            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp < timestamp:
                res = mid_value
                start = mid + 1
            else:
                end = mid - 1
        return res

        
