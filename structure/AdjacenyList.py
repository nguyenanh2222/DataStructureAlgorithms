"""doc danh sach ke"""
class AdjList():

    def __init__(self, nodes: []):
        self.num = len(nodes)
        self.nodes = nodes

    def list_size(self):
        return self.num

    def is_empty(self):
        if self.num == 0:
            return True
        else:
            return False

    def is_full(self):
        MAX = 10
        if self.num == MAX:
            return True
        else:
            return False

    def insert_node(self, x, pos):
        for i in self.nodes:
            if self.





    def binary_search(self, arr: [], target):
        """requirement: tu dau mang phai xap xep tang dan"""
        left = 0
        right = len(arr)
        mid = round((left + right) / 2)
        while left < right:
            if arr[mid] < target:
                return self.binary_search(arr=arr[mid:], target=target)
            elif arr[mid] > target:
                return self.binary_search(arr=arr[:mid], target=target)
            elif arr[mid] == target:
                print(arr[mid])
                break


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 10]
    adj = AdjList(nodes=arr)
    print(adj.list_size())
    print(adj.binary_search(arr, 3))
