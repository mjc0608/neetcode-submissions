class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append((value, timestamp))
        else:
            self.m[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.m:
            return ""
        m = self.m[key]
        l = 0
        r = len(m) - 1

        if timestamp < m[0][1]:
            return ""

        while l <= r:
            mid = (l + r) // 2
            if m[mid][1] == timestamp or (
                m[mid][1] < timestamp and (
                    mid + 1 >= len(m) or m[mid+1][1] > timestamp
                )
            ):
                return m[mid][0]
            if m[mid][1] > timestamp:
                # too late
                r = mid - 1
            else:
                l = mid + 1
                
        return ""