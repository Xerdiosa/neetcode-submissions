class MyHashMap:

    def __init__(self):
        self.keys = [None for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.keys[key]=value

    def get(self, key: int) -> int:
        if self.keys[key] is None:
            return -1
        return self.keys[key]

    def remove(self, key: int) -> None:
        self.keys[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)