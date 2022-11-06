def solve(s):
    chunk = []
    for item in s.split(" "):
        chunk.append(item.title())
    return " ".join(chunk)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "12hello  word"

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
