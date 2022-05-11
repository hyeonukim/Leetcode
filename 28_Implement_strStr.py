def answer(haystack, needle):
    if needle == '':
        return 0
    if needle not in haystack:
        return -1
    
    n = len(needle)
    for i in range(0, len(haystack)-n+1):
        if haystack[i:i+n] == needle:
            return i

if __name__ == "__main__":
    haystack = input("type in haystack\n")
    needle = input("type in needle\n")

    print(answer(haystack, needle))