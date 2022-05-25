def answer(numRows):

    list = [[1]]
    for i in range(2,numRows+1):
        new = []
        for j in range(i):
            if j == 0 or j == i-1:
                new.append(1)
            else:
                new.append(list[i-2][j] + list[i-2][j-1])
        
        list.append(new)
    
    return list
if __name__ == "__main__":

    print(answer(5))