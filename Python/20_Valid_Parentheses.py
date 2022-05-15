def answer(s):
    arr = []
    for i in range(len(s)):
        if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
            arr.append(s[i])
        if (s[i] == ')' or s[i] == ']' or s[i] == '}'):
            if (len(arr) == 0):
                return False
            if (s[i] == ')' and arr[-1] == '('):
                arr.pop()
            elif (s[i] == ']' and arr[-1] == '['):
                arr.pop()
            elif (s[i] == '}' and arr[-1] == '{'):
                arr.pop()
            else:
                return False
    if (len(arr) > 0):
        return False
    else:
        return True

if __name__ == "__main__":
    str = input("Enter question\n")
    print(answer(str))