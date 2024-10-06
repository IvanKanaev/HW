def triangle(h, symb, depth = 1):
    if h % 2 != 0 and depth == h//2 + 1:
        print(symb*depth)
        return

    if h % 2 == 0 and depth == h//2 + 1:
        print(symb*depth)
        print(symb * depth)
        return

    print(symb * depth)

    triangle(h,symb, depth = depth + 1)

    print(symb * depth)
    return
size, symb = input().split()
size = int(size)

print(triangle(size,symb))