def answer(n):
    step = [1, 2, 3]
    fib = [1, 1]
    k = 1
    if n == 0:
        return 0
    if n <= 2:
        return step[n-1]
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
        step.append(fib[i]+step[i])
        k += 1
    return step[n-1]

if __name__ == "__main__":
    n = int(input("Type in a number\n"))
    print(answer(n))