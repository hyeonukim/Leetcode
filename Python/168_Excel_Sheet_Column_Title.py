def answer(columnNumber):

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
    res = ""
    
    while columnNumber > 26:
        mod = columnNumber % 26
        if mod== 0:
            columnNumber = columnNumber // 26 - 1
        else:
            columnNumber = columnNumber // 26
        res += alphabet[mod-1]

    res += alphabet[columnNumber-1]
    return res[::-1]

if __name__ == "__main__":
    columnNum = 701
    print(answer(columnNum))