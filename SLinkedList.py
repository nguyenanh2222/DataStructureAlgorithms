class Node:
    def init(self, data=None):
        self.data = data
        self.next = None
        # khoi tao danh sach
class SingleLinkedList:
    def init(self):
        self.head = None
    def displaySLL(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    # hien thi danh sach Node
    def isEmpty(self):
        ...
    # kiem tra danh sach co rong hay khong
    def nodeGetHead(self):
        ...
    # tra ra node dau tien
    def getHeadData(self):
        ...
    # lay gia tri node dau tien trong danh sach
    def insertNode2Head(self, x: int):
    # chen node co gia tri x vao dau head
            ...
    def insertNode2Tail(self, x: int):
        new_data = Node(x)
        if self.head is None:
            self.head = new_data
    # chen node co gia tri x vao cuoi head
    def insertNode2Tail(self, x: int):
        if self.next == None:
            p = Node(data=x)
            return p
    #chen node p vao cuoi danh sach
    def insertNode2After(self, q: Node, x: int):
        ...
    # chen co node co gia tri x vao sau node q trong danh sach
    def removeNodeAtHead(self):
        ...
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