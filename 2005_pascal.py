def pascal(original, new, first, second):
    last = len(original) - 1

    new[second] = original[first] + original[second]

    if second == last:
        return

    pascal(original, new, first + 1, second + 1)


T = int(input())  # TEST CASE

for test_case in range(1, T + 1):
    N = int(input())  # 반복 횟수
    original = [1, 1]
    new = [1, 1]

    print(f"#{test_case}")

    for i in range(1, N + 1):
        if i == 1:
            print(1)
        elif i == 2:
            print(1, 1)
        elif i > 2:
            pascal(original, new, 0, 1)

            new.append(1)
            original = new.copy()

            for num in new:
                print(num, end=" ")
            print()
