def answer(s):

    left, right, resLen = -1, -1, 0

    for i in range(len(s)):
        #in case Palindrome is odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if resLen < (r-l+1):
                resLen = (r-l+1)
                left, right = l, r
            l -= 1
            r += 1
        #in case Palindrome is even
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if resLen < (r-l+1):
                resLen = (r-l+1)
                left, right = l, r
            l -= 1
            r += 1
        
    return s[left:right+1]

if __name__ == "__main__":
    s = 'cbbd'
    print(answer(s))