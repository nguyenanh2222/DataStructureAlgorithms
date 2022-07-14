from random import randrange

arr = []


class RecursionArray:
    def input_s_array(self, arr: [], n: int):
        if n <= 0:
            return
        i = self.input_array(arr, n)
        print(f"Input arr {i}: ", n)


    def input_array(self, arr:[], n: int):
        arr.append(n)
        for i in range(1, len(arr)):
            return self.input_array(arr, n)



if __name__ == "__main__":
    arr = []
    rec_a = RecursionArray()
    n = randrange(1, 10)
    rec_a.input_s_array(arr, n)
    rec_a.input_s_array(arr, n)
    rec_a.input_s_array(arr, n)
    # print()
