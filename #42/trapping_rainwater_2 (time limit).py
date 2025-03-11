
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    total = 0
    for rows in range(max(height)): # works out water on each row one by one
        for i in range(len(height)):
            if height[i] > 0:
                first_wall = i
                break
        for i in range(1, len(height) + 1):
            if height[-i] > 0:
                last_wall = -i
                break
        
        total += height[first_wall+1:last_wall].count(0)

        height = list(map(lambda x: x-1 if x-1>0 else 0, height)) # decreases height of all walls by 1
    
    return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

