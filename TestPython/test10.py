def swap_case(s):
    result = ""
    for item in s:
        if item.islower():
            result += item.upper()
        else:
            result += item.lower()
    return result

if __name__ == '__main__':
    s = "HackerRank.com presents 'Pythonist 2'."
    result = swap_case(s)
    print(result)