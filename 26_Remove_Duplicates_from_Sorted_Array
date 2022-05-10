def answer(nums):
    if len(nums) == 0:
        return 0
        
    k = 0
    for i in range(1, len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]
    k += 1
    return k

if __name__ == "__main__":
    print("Enter numbers for list and enter else than number to stop")
    try: 
        nums = []
        while True:
            nums.append(int(input()))
    except:
        print(nums)

    k = answer(nums)
    print(k)