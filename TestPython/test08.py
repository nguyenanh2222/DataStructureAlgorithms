total = 5
print(globals())
if globals()["total"] is 5:
    print("total")

# print([name for name in globals() if globals()[name] is 5])