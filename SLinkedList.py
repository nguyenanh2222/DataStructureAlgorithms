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

    def liearSearch(self, target: int):
        current_node = self.head
        while current_node is not None:
            if current_node.data == target:
                print(current_node.data)
                break
            if current_node.data != target:
                current_node = current_node.next
            if current_node == None:
                print("Not found")

    def isEmpty(self):
        # kiem tra danh sach co rong khong
        if self.head is None:
            print("Empty")

    def nodeGetHead(self):
        first_node = self.head
        while first_node is not None:
            print("Head is", first_node.data)
            break
        if first_node is None:
            print("Head can not be none")

    def getHeadData(self):
        # lay gia tri node dau tien trong danh sach
        first_node = self.head
        while first_node is not None:
            print(first_node.data)
            break
        if first_node is None:
            print("Head can not be none")

    def removeNodes(self, x: int):
        temp = self.head
        while temp.data == x:
            temp.next = temp.next.next

    def appendList(self, l, x: []):
        fist_node_x = self.head
        last_node_y = self.head
        # noi 2 danh sach lien ket
        last_node_y.next = fist_node_x

    def removeNodeAtHead(self):
        if self.head is None:
            print("Head is not none")
        if self.head is not None:
            self.head = self.head.next

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
        while (temp is not None):
            if temp.data == x:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None


list = LinkedList()
list.insertNode2Head(1)
print(list)
list.insertNode2Head(1)
list.insertNode2Head(2)
list.insertNode2Head(2)
list.insertNode2Head(3)
list.insertNode2Head(3)
# list.liearSearch(9)
# list.removeNodes(3)
list.removeNodeAtTail()
list.removeNodeAtHead()
list.removeNode(2)
# list.removeNodes(2)
# list.isEmpty()
# list.nodeGetHead()
print(list)
