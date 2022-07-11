"""Tree: Cấu trúc dữ liệu biểu diễn các Node được kết nối với nhau theo mô hình phân cấp
hai node nối với nhau bởi các cạnh, node gốc, node ch, node anh em, node ngoài, node lá,
node trong, cây có chiều cao, bậc của node, node có độ sâu, cây có n node sẽ có n-1 cạnh
Binary Tree: mỗi cây có tối đa hai node con. Một cây nhị phân sẽ tận dụng lợi thế của hai
kiểu cấu trúc dữ liệu :
    - Mảng đã sắp xếp
    -Danh sách liên kết
=> việc tìm kiếm nhanh như mảng đã sắp xếp
Traversal: Duyệt cây với 3 loại cơ bản:
pre-oder traversal, In-order traversal, post-order traversal.
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(Node):

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def isLeft(self, p: int):
        p = Node(p)
        if p.left == None and p.right == None:
            return True
        return False

    def NLR(self, p: Node):
        if p:
            print(p.data)
            self.NLR(p.left)
            self.NLR(p.right)
    def LNR(self, p: Node):
        if p:
            self.LNR(p.left)
            print(p.data)
            self.LNR(p.right)
    def LRN(self, p: Node):
        if p:
            self.LRN(p.left)
            self.LNR(p.right)
            print({p.data})







