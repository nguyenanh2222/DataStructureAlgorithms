'''cấu trúc lại cây nhị phân sao cho mỗi node chứa 1 department
class Department:
  id: int
  name: str
  person_count: int

Viết hàm lấy ra cây con của department theo id (với department hiện tại là node root)
input: department id
output: tree
     de_1                                                          de_3
   /          \                                                       /       \
de_2     de_3          my_func(de_3)->     de_4      de_5
             /       \
          de_4    de_5
Viết hàm tìm danh sách department có person_count nhỏ hơn department truyền vào
input: department_id
output: List[Department]'''


class Department:
    def __init__(self, id: int, name: str, person_count: int):
        self.id = id
        self.name = name
        self.person_count = person_count
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.id}-{self.name}-{self.person_count}"

    def search_id(self, id: int):
        if self.id == id:
            return self.id
        if id < self.id:
            return self.search_id(self.left)
        return self.search_id(self.right)


class TreeDepartment:
    def __init__(self):
        self.root = None

    def print_tree(self, node: Department = None):
        if not node:
            node = self.root
        print(node)
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)

    def insert_department(self, id: int, name: str, person_count: int, p: Department = None):
        if id == None:
            raise Exception("invalid input")
        if not p:
            if not self.root:
                self.root = Department(id=id, name=name, person_count=person_count)
                return
            p = self.root
        if p.right.id > id:
            if not p.left:
                p.left = Department(id=id, name=name, person_count=person_count)
                return
            return self.insert_department(id, name, person_count, p.left)
        if p.id < id:
            if not p.right:
                p.right = Department(id=id, name=name, person_count=person_count)
                return
            return self.insert_department(id, name, person_count, p.right)


    def search_person_count_by_id(self, id: int):
        if self.root:
            print(self.root.person_count)
            return self.root.person_count
        if self.root.left:
            self.print_tree(self.root.left.id)
        if self.root.right:
            self.print_tree(self.root.right.id)


    def search_smaller_person_count(self, id: int):
        if id == None:
            raise Exception("invalid input")
        print(self.root.person_count)
        if self.root and self.root.person_count < self.search_person_count_by_id(id):
                return self.root.id
        if self.root.left and self.root.left.person_count < self.search_person_count_by_id(id):
            print(self.root.left.person_count)
            return self.search_smaller_person_count(self.root.left.id)
        if self.root.right and self.root.right.person_count > self.search_person_count_by_id(id):
            print(self.root.right.person_count)
            return self.search_smaller_person_count(self.root.right.id)


if __name__ == '__main__':
    tree = TreeDepartment()
    # tree = tree.search_id(1)
    # tree.search_id(1)
    tree.insert_department(id=2, name="B", person_count=3000)
    tree.print_tree()
    print("====")
    tree.insert_department(id=3, name="C", person_count=5100)
    tree.print_tree()
    print("====")
    tree.insert_department(id=4, name="D", person_count=4050)
    tree.print_tree()
    print("====")
    tree.insert_department(id=5, name="E", person_count=3600)
    tree.print_tree()
    print("====")
    tree.search_smaller_person_count(3)
    # p = Department(id=2, name="B", person_count=2500)
    # tree = tree.insert(p)
