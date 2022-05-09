def answer(arr):

    minStr = min(arr, key = len)
    minLen = len(minStr)
    str = ""
    
    for i in range(minLen):
        for j in range(len(arr)):
            if (minStr[:i+1] != arr[j][:i+1]):
                return str
        str += minStr[i]

    return str

if __name__ == "__main__":

    arr = ["flower", "flow", "flight"]
    str = 'flow'
    print(answer(arr))