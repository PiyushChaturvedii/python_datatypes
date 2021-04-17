def findAllNumbers(N):
    cb = int(pow(N, 1.0 / 3))
    s = set()
    for i in range(1, cb - 1):
        for j in range(i + 1, cb):
            sum = (i * i * i) + (j * j * j)
            if sum in s:
                print(sum)
            else:
                s.add(sum)


if __name__ == '__main__':
    N = 25000
    findAllNumbers(N)