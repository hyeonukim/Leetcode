def answer(s):

    res = ""
    for ch in s:
        if ch.isalpha() or ch.isdigit():
            res += ch

    res = res.lower()
    reverse = res[::-1]

    if res == reverse:
        print(res)
        print(reverse)
        return True
    return False
    


    return 
if __name__ == "__main__":
    s = "0P"

    print(answer(s))