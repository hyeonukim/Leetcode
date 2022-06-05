def answer(columnTitle):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    res = 0
    for s in columnTitle:
        res *= 26
        for i in range(len(alphabet)):
            if s == alphabet[i]:
                res += (i+1)

    return res
if __name__ == "__main__":
    s = 'ZY'
    print(answer(s))
    