def get_input():
    return int(input("Select a operation:\n1.Insertion\n2.Searching\n3.Display\n4.Quit\t"))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("Enter Element ")))
    elif q == 2:
        key = int(input("Enter Element to Search "))
        print(
            f"Node is present in the list at the position : {ls.index(key) + 1}" if key in ls else "Node is not present in the list")
    elif q == 3:
        for i in ls:
            print(i)
    else:
        break