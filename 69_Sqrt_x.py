def answer(x):
    left = 0
    right = x
    ans = 0
    while left <= right:
        mid = left + (right-left)//2
        if (mid * mid == x):
            return mid
        elif (mid * mid < x):
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans
    

if __name__ == "__main__":
    x = int(input("type in a number\n"))
    print(answer(x))