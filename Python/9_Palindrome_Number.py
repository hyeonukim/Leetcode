def answer(x):
    result = 0
    num = x
    if (x < 0):
        return False
        
    while (num > 0):
        result *= 10
        r = num % 10
        result += r
        num = num // 10

    if (result == x):
        return True
    else:
        return False
    
if __name__ == "__main__":
    x = int(input("Please input a number\n"))

    if (answer(x) == True):
        print("number is palindrome")
    else:
        print("number is NOT palindrome")