class LinkedList:

    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        if index > len(self.arr)-1:
            return -1
        else:
            return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.arr.insert(0,val)

    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index > len(self.arr)-1:
            return False
        else:
            del self.arr[index]
            return True

    def getValues(self) -> List[int]:
        return self.arr
