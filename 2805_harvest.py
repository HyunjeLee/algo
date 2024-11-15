T = int(input())  # 테스트 케이스 갯수

for test_case in range(1, T + 1):

    N = int(input())  # 줄 갯수 N X N  # N은 홀수
    start = 0
    end = N - 1
    profit = 0
    matrix = [[] for _ in range(N)]

    # input
    for line in range(N):
        matrix[line] = [int(char) for char in input()]  # list comprehension

    # main logic
    profit += sum(matrix[N // 2])

    for i in range(1, N // 2 + 1):
        for _ in range(i):
            matrix[N // 2 + i].pop()
            matrix[N // 2 + i].pop(0)

            matrix[N // 2 - i].pop()
            matrix[N // 2 - i].pop(0)

        profit += sum(matrix[N // 2 + i])
        profit += sum(matrix[N // 2 - i])

    # print
    print(f"#{test_case} {profit}")

    # test
    # for i in range(N):
    #     print("test", end=" ")
    #     print(*matrix[i])
