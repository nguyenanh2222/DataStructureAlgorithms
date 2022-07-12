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


class TreeDepartment:
    def __init__(self):
        self.root = None

    def print_tree(self):
        # print(type(self.root))
        if self.root.left:
            self.root.left.print_tree()
        print(self.root)
        if self.root.right:
            self.root.right.print_tree()

    def search_id(self, id: int):
        if self.root:
            # print((self.root.id))
            if self.root.id == id:
                return self.root.id
            if id < self.root.id:
                # print('trai')
                return self.search_id(self.root.left)
            # print('phai')
            return self.search_id(self.root.right)
        return None

    def insert_department(self, p: Department, id: int, name: str, person_count: int):
        if id == None:
            raise Exception("invalid input")
        if self.search_id(id):
            raise Exception("invalid input")
        if not self.root:
            self.root = Department(id=id, name=name, person_count=person_count)
            return p
        else:
            if p.id > id:
                return self.insert_department(p.left, id, name, person_count)
            if p.id < id:
                return self.insert_department(p.right, id, name, person_count)
            p = Department(id=id, name=name, person_count=person_count)
            return p

    def search_person_count_by_id(self, id: int):
        if self.root:
            if self.root.id == id:
                return self.root.person_count
            if id < self.root.id:
                return self.search_person_count_by_id(self.root.left)
            return self.search_person_count_by_id(self.root.right)
        return None

    def search_smaller_person_count(self, id: int):
        p: Department
        list_department = []
        if self.search_id(id) is None:
            return f"department {id} not found"
        else:
            if p.person_count < self.search_person_count_by_id(id):
                list_department.append([p.id, p.name, p.person_count])
                return list_department


if __name__ == '__main__':
    p = Department(id=1, name="A", person_count=2500)
    tree = TreeDepartment()
    # tree = tree.search_id(1)
    # tree.search_id(1)
    tree.insert_department(p, id=2, name="B", person_count=3000)
    tree.print_tree()
    tree.insert_department(p, id=3, name="C", person_count=5100)
    tree.insert_department(p, id=4, name="D", person_count=4050)
    tree.insert_department(p, id=5, name="E", person_count=3600)
    tree.print_tree()
    # p = Department(id=2, name="B", person_count=2500)
    # tree = tree.insert(p)
