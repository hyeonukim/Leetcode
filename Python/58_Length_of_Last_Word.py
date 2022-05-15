def answer(s):
    arr = s.split()
    return len(arr[-1])

if __name__ == "__main__":
    s = input("Type the string\n")
    print(answer(s))