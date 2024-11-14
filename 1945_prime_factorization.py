T = int(input())

primes = {2, 3, 5, 7, 11}
answer = {}

for i in range(T):
    N = int(input())

    for prime in primes:
        cnt = 0
        while N % prime == 0:
            N //= prime
            cnt += 1
        answer[prime] = cnt

    print(f"#{i + 1}", end=" ")
    for item in answer.values():
        print(item, end=" ")
    print()
