def minimumOperations(grid: list[list[int]]) -> int:
    operations = 0
    for col in range(len(grid[0])):
        # Keep track of the number above the current number 
        # (starting with the first number in the column).
        last_num = grid[0][col]
        for row in range(1, len(grid)):
            num = grid[row][col]
            if num <= last_num:
                # The number has to become one more than the last number.
                last_num += 1
                operations += (last_num - num)
            else:
                last_num = num
    return operations        
