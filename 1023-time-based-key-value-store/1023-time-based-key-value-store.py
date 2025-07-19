import bisect
class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []

        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            idx = bisect.bisect_left(self.store[key], timestamp, key=lambda x: x[0])
            if (idx == len(self.store[key]) or timestamp != self.store[key][idx][0]) :
                value = self.store[key][idx - 1]
                if timestamp < value[0]:
                    return ""
                else:
                    return value[1]
            else:
                return self.store[key][idx][1]
        else:
            return ""

            

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)