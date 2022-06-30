class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        # khoi tao danh sach
class LinkedList:
    def __init__(self):
        self.head = None
if __name__=='__main__':
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    list.head.next = second
    list.head.next = third
    def displaySLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        # hien thi danh sach Node
    def insertNode2Head(self, new_data: int):
    # chen node co gia tri new_data vao dau head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertNode2Tail(self, new_node: int):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while (last.next):
            last = last.next
        last.next = new_node
    # chen node co gia tri x vao cuoi head
    def insertNode2After(self, prev_node: Node, new_data):
        if prev_node is None:
            print("Node can not be none")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    # chen co node co gia tri x vao sau node q trong danh sach
    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True  # tìm thấy
            current = current.next
        return False  # không tìm thấy
    def isEmpty(self):
        ...
    # kiem tra danh sach co rong hay khong
    def nodeGetHead(self):
        ...
    # tra ra node dau tien
    def getHeadData(self):
        ...
    # lay gia tri node dau tien trong danh sach

    def removeNodeAtHead(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        #loai bo node dau tien
    def removeNodeAtTail(self):
        ...
    #loai bo node cuoi cung
    def removeNode(self, x: int):
        ...
    # loai bo node dau tien co gia tri bang x
    def removeNodes(self, x: int):
        ...
    # loai bo tat ca cac node co gia tri bang x
    def appendList(self, l, x: int):
        ...
    #noi 2 danh sach lien ket
list = SingleLinkedList()
list.insertNode2Tail(1)
print(list.displaySLL())