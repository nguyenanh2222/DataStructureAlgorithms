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
    def __init__(self, id: int):
        self.id = id
        self.name = None
        self.person_count = None


class TreeDepartment:
    def __init__(self):
        self.de = None
        self.left = None
        self.right = None

    def insertNode(self, p: Department, x: int):
        if p != None:
            if p.data == x:  # da ton tai trong cay
                return False
            if p.data > x:
                return self.insertNode(p.left, x)
            else:
                return self.insertNode(p.right, x)
        p = Department(x)
        if p == None:
            return False
        p.data = x
        p.left = None
        p.right = None
        return p

    def search_id(self, id: int):
        if self.de:
            if self.de.id == id:
                return self.de.id
            if id < self.de.id:
                return self.search_id(self.de.left)
            return self.search_id(self.de.right)
        return None

    def search_person_count_by_id(self, id: int):
        if self.de:
            if self.de.id == id:
                return self.de.person_count
            if id < self.de.id:
                return self.search_person_count_by_id(self.de.left)
            return self.search_person_count_by_id(self.de.right)
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
