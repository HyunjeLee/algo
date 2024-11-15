N = int(input())

for num in range(1, N + 1):
    clap = ""

    if num < 10:
        if num % 3 == 0:
            print("-", end=" ")
            continue

    elif 10 < num < 100:
        tens = num // 10
        units = num - tens * 10

        if units % 3 == 0 and units != 0:
            clap += "-"
        if tens % 3 == 0:
            clap += "-"

    elif 100 < num < 1000:
        hundreds = num // 100
        tens = (num - hundreds * 100) // 10
        units = num - hundreds * 100 - tens * 10

        if units % 3 == 0 and units != 0:
            clap += "-"
        if tens % 3 == 0 and tens != 0:
            clap += "-"
        if hundreds % 3 == 0:
            clap += "-"

    if clap:
        print(clap, end=" ")
        continue

    print(num, end=" ")
