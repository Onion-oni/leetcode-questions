#189. Rotate Array
#Rotates an array to the right by 'k' steps
def rotate(nums,k):
    f = 0
    while f < k:
        y = nums.pop()
        nums.insert(0,y)
        f += 1
    print(nums)
