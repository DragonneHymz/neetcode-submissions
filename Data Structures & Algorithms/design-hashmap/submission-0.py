class ListNode:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode() for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        current = self.hashMap[key % len(self.hashMap)]
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        current = self.hashMap[key % len(self.hashMap)]
        while current.next:
            if current.next.key == key:
                return current.next.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.hashMap[key % len(self.hashMap)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)