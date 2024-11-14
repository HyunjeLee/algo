def pow(n, m):
    if m == 0:
        return 1

    return n * pow(n, m - 1)


T = int(input())
n, m = map(int, input().split(" "))

print(f"#{T} {pow(n, m)}")