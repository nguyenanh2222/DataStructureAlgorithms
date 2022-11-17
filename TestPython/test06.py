def to_binary(input: int) -> int:
    b = int
    if input == 0:
        return 0
    else:
        b = input % 2
    return to_binary(input // 2) * 10 + b


def test_cir(input: int) -> int:
    if input == 0:
        print("stop")
    else:
        # print(input, "tr")
        test_cir(input-1)
        print(input, "s")

# print(to_binary(8))
test_cir(8)
