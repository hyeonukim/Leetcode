def answer(nums, val):

    if len(nums) == 0:
        return 0
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+= 1
    return k

if __name__ == "__main__":
    print("Enter numbers for list and enter else than number to stop")
    try: 
        nums = []
        while True:
            nums.append(int(input()))
    except:
        print(nums)
    
    val = int(input("Enter the value you want to remove\n"))
    k = answer(nums,val)
    print(k)