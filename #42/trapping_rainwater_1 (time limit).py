def water_in_row(row):
    """
    :type height: List[int]
    :rtype: int
    """
    first_1 = row.index(1)
    last_1 = len(row) - row[::-1].index(1) - 1

    water = row[first_1+1:last_1].count(0)

    return water

def trap(heights):
    matrix = [[0 for i in range(len(heights))] for i in range(max(heights))]
    for i, height in enumerate(heights):
        for j in range(0, height):
            matrix[j][i] = 1
    
    total = 0
    for row in matrix:
        total += water_in_row(row)
    
    return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
