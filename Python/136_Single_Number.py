def answer(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

if __name__ == "__main__":
    nums = [2,2,1]
    print(answer(nums))