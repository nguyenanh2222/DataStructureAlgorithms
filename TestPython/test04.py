from typing import List


def most_frequent(data: List[str]) -> str:
    chunk = []
    for item in data:
        chunk.append(data.count(item))
    count_max = max(chunk)
    for item in data:
        if data.count(item) == count_max:
            return item
    return ""


print("Example:")
print(most_frequent(["a", "a", "bi", "bi", "bi"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")