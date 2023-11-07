a = [1, 2]
b = [1]


def get_total_x(a, b):
    x = []
    rx = []
    for i in a:
        for j in a:
            print(f"a/j", i, j)
            if i % j == 0:
                x.append(i)

    print(list(set(x)))

    for i in b:
        for j in list(set(x)):
            print(f"i/j", i, j)
            if i % j == 0:
                rx.append(i)

    lenx = len(list(set(rx)))
    print(lenx)
    return lenx


get_total_x(a, b)
