def answer(digits):
    num = 0
    for i in range(len(digits)):
        num *= 10
        num += digits[i]
    num += 1
    arr = list(map(int,str(num)))
        
    return arr

if __name__ == "__main__":
    print("Enter numbers for digits and enter else than number to stop")
    try: 
        digits = []
        while True:
            digits.append(int(input()))
    except:
        print("your input is", digits)
    
    ans = answer(digits)
    print(ans)