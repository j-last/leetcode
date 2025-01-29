def minimumOperations(grid: list[list[int]]) -> int:
    operations = 0
    for col in range(len(grid[0])):
        last_num = grid[0][col]
        for row in range(1, len(grid)):
            num = grid[row][col]
            if num <= last_num:
                last_num += 1
                operations += (last_num - num)
            else:
                last_num = num
    return operations        

print(
    minimumOperations(
        [[3,2],[1,3],[3,4],[0,1]]
    )
)