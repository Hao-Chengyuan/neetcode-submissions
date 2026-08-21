class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list[list])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap.keys():
            self.tmap[key].append([value, timestamp])
        else:
            self.tmap[key] = [[value, timestamp]]
        return None

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.tmap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= self.tmap[key][m][1]:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res