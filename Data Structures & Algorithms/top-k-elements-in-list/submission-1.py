class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set()
        map = {}
        for i in nums:
            if i in unique:
                map[i] += 1
            else:
                unique.add(i)
                map[i] = 0
        temp = []
        values = list(map.values())
        for _ in range(k):
            maximum = max(values)
            temp.append(maximum)
            values.remove(maximum)
        res = []
        keys = list(map.keys())
        values = list(map.values())
        for x in temp:
            index = values.index(x)
            res.append(keys[index])
            keys.pop(index)
            values.pop(index)
        return res
