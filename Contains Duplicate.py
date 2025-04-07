def hasDuplicate(nums):
    tempSet = set(nums)
    if len(tempSet) == len(nums):
        return True
    return False

def main():
    x = hasDuplicate([1,2,3,2])
    print("answer :",x)
    
if __name__ == "__main__":
    main()