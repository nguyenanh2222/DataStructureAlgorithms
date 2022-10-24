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
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def isLeaf(self, p: Node):
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

    def travelsalTree(self, type: int):
        while type:
            if self.NLR(self.root):
                break
            elif self.LNR(self.root):
                break
            elif self.LRN(self.root):
                break
            else:
                break

    def searchNode(self, p: Node, x: int):
        if p:
            if p.data == x:
                return p
            elif p.data > x:
                return self.searchNode(p.left, x)
            elif p.data < x:
                return self.searchNode(p.right, x)
        return None

    def insertNode(self, p: Node, x: int):
        if p != None:
            if p.data == x:  # da ton tai trong cay
                return False
            if p.data > x:
                return self.insertNode(p.left, x)
            else:
                return self.insertNode(p.right, x)
        p = Node(x)
        if p == None:
            return False
        p.data = x
        p.left = None
        p.right = None
        return p

    def searchStandFor(self, p: Node, q: Node):
        if p.left:
            self.searchNode(p, q.left)
        else:
            p.data = q.data
            p = q
            q = q.right

    def delNode(self, p: Node, x: int):
        if p == None:
            return False
        if p.data > x:
            return self.delNode(p.left, x)
        if p.data < x:
            return self.delNode(p.right, x)
        else:
            temp: Node
            temp = p
            if p.left == None:
                p = p.right
            else:
                if p.right == None:
                    p = p.left
                else:
                    self.searchStandFor(temp, p.right)
        del temp
        return p

    def delOneNode(self, x: int):
        return self.delNodex(self.root, x)

    def removeTree(self, p: Node):
        if p != None:
            self.removeTree(p.left)
            self.removeTree(p.right)
            del p
        return

    def countNode(self, p: Node):
        if not p:
            return False
        c1: int
        c2: int
        c1 = self.countNode(p.left)
        c2 = self.countNode(p.right)
        # cong them node dang xet
        return c1 + c2 + 1

    def countLeafNode(self, p: Node):
        if not p:
            return False
        c1: int
        c2: int
        c1 = self.countLeafNode(p.left)
        c2 = self.countLeafNode(p.right)
        # neu node dang xet la node la
        return c1 + c2 + self.isLeaf(p)

    def count1Node(self, p: Node):
        # dem so node co mot cay con
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.count1Node(p.left)
        c2 = self.count1Node(p.right)
        if p.left and p.right is None:
            c3 += 1
        if p.right and p.left is None:
            c3 += 1
        return c1 + c2 + c3

    def count2Node(self, p: Node):
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.count2Node(p.left)
        c2 = self.count2Node(p.right)
        if p.left and p.right:
            c3 += 1
        return c1 + c2 + c3

    def countSmallerNode(self, p: Node, x: int):
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.countSmallerNode(p.left, x)
        c2 = self.countSmallerNode(p.right, x)
        if p.data < x:
            c3 += 1
        return c1 + c2 + c3

    def countLargerNode(self, p: Node, x: int):
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.countLargerNode(p.left, x)
        c2 = self.countLargerNode(p.right, x)
        if p.data > x:
            c3 += 1
        return c1 + c2 + c3

    def countLargerSmallerNode(self, p: Node, x: int, y: int):
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.countLargerSmallerNode(p.left, x, y)
        c2 = self.countLargerSmallerNode(p.right, x, y)
        if p.data > x and p.data < y:
            c3 += 1
        return c1 + c2 + c3

    def getHightofTree(self, p: Node):
        if not p:
            return False
        c1: int
        c2: int
        c3: int
        c1 = self.getHightofTree(p.left)
        c2 = self.getHightofTree(p.right)
        if c1 > c2:
            _max = c1
        else:
            c2
        return _max + 1

    def countNodeLv(self, p: Node, k: int, i: int):
        # dem tong node o muc k, i luu tru bien dem
        if not p:
            return False
        if i == k:
            print(p.data)
            return True
        return self.countNodeLv(p.left, k, i + 1) + self.countNodeLv(p.right, k, i + 1)

    def nodeLvtoLv(self, p: Node, k: int, i: int):
        if not p:
            return
        if i == k:
            print(p.data)
        self.nodeLvtoLv(p.left, k, i+1)
        self.nodeLvtoLv(p.right, k, i+1)

if __name__ == '__main__':
    tree = Node(5)
    a = 6
    b = BinarySearchTree
    print(b.insertNode(tree, a))