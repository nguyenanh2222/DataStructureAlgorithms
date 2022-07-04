class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        temp_str = ""
        while temp:
            temp_str += f"{temp.data}-->"
            temp = temp.next
        temp_str += "None"
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

    def get_length(self):
        size = 0
        curr = self.head
        while curr:
            size += 1
            curr = curr.next
        return size

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if index < 0 or index >= self.get_length():
            raise Exception("invalid input")
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        count = 0
        curr = self.head
        while curr is not None:
            if count == index - 1:
                new_node = curr.next
                break
            curr = curr.next
            count += 1

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

    def removeNodeIndex(self, index):
        if index < 0 or index <= self.get_length():
            print("Invalid input")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1
    #
    # def removeNodeTarget(self, target: int):
    #     temp = self.head
    #     prev = temp.next
    #     if temp is None:
    #         print("Head can not none")
    #     if temp.data == target:
    #         temp = temp.next
    #         temp.data = prev.data
    #         temp.next = temp.next.next
    #         return
    #     while temp.next is not None and temp.data != target:
    #         prev = temp
    #         temp = temp.next
    #     if temp.next is None and temp.data != target:
    #         print("target not exits")
    #     elif temp.next is None and temp.data == target:
    #         prev.next = None
    #     else:
    #         prev.next = temp.next
    #     if self.head.next == target:
    #         self.head.next = self.head.next.next
        # //// remove mot gia tri target

    def removeNodeTarget(self, target: int):
        temp = self.head
        prev = None
        if temp is None:
            print("Head can not none")
        # TH 1 target = head
        if temp.data == target:
            self.head = temp.next
            temp.next = None
            return self.removeNodeTarget(target)
        while temp.next is not None:
            prev = temp
            temp = temp.next
            if temp.data == target:
                # TH TARGET IS NOT TAIL VA HEAD
                if temp.next:
                    prev.next = temp.next
                # TH TARGET IS TAIL
                else:
                    prev.next = None
                # CALL BACK FUNC
                return self.removeNodeTarget(target)

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


list = LinkedList()
list.insertNode2Head(8)
list.insertNode2Head(8)
list.insertNode2Head(1)
list.insertNode2Head(1)
list.insertNode2Head(2)
list.insertNode2Head(2)
list.insertNode2Head(3)
list.insertNode2Head(3)
list.insertNode2Head(8)

print(list)
# list.insertAtIndex(8, 0)
# print(list)
list.removeNodeTarget(8)
# list.removeNodeAtHead()
# list.removeNodeIndex(0)
# list.liearSearch(9)
# list.removeNodes(3)
# list.removeNodes(2)
# list.isEmpty()
# list.nodeGetHead()
print(list)
