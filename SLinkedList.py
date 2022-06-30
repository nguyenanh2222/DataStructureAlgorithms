class Node:
    # khoi tao danh sach
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        temp_str = ''
        while temp:
            temp_str += f"{temp.data}->"
            temp = temp.next
        temp_str += 'None'
        return temp_str

    def insertNode2Head(self, new_data: int):
        # chen node co gia tri new_data vao dau head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertNode2Tail(self, new_node: int):
        # chen node co gia tri x vao cuoi head
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def insertNode2After(self, prev_node: Node, new_data):
        # chen co node co gia tri x vao sau node q trong danh sach
        if prev_node is None:
            print("Node can not be none")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True  # tìm thấy
            current = current.next
        return False  # không tìm thấy

    # def isEmpty(self):
    # ...
    # kiem tra danh sach co rong hay khong
    # def nodeGetHead(self):
    # ...
    # tra ra node dau tien
    # def getHeadData(self):
    # ...
    # lay gia tri node dau tien trong danh sach
    def removeNodeAtHead(self, key):
        # loai bo node dau tien
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                return
        while (temp is not None):
            if temp.data == key:
                break
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

    def removeNodeAtTail(self):
        # loai bo node dau tien co gia tri bang x
        if (self.head != None):
            if (self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next
                tailNode = temp.next
                temp.next = None
                tailNode = None

    def removeNode(self, x: int):
        temp = self.head
        if (temp is not None):
            if (temp.data == x):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == x:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    # def removeNodes(self, x: int):
    #     ...
    # loai bo tat ca cac node co gia tri bang x
    # def appendList(self, l, x: int):
    #     ...
    # noi 2 danh sach lien ket


list = LinkedList()
list.insertNode2Head(1)
list.insertNode2Head(2)
list.insertNode2Head(3)
list.insertNode2Tail(4)
list.insertNode2Head(2)
list.insertNode2Head(2)
list.insertNode2Head(2)
# list.removeNodeAtHead(3)
# list.search()
# # search chua ok
# list.removeNodeAtHead(2)
# list.removeNodeAtTail()
list.removeNode(2)
print(list)
