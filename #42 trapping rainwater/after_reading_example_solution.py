def trap(heights):
    max_lhs = [0]
    max_rhs = [0]

    for i in range(1, len(heights)):
        max_lhs.append(max(heights[:i]))
        max_rhs.insert(0, max(heights[-i:]))
    print(max_lhs, max_rhs)
    total = 0
    for i in range(1, len(heights)):
        total += max(min(max_lhs[i], max_rhs[i]) - heights[i], 0)

    print(total)


trap([0,1,0,2,1,0,1,3,2,1,2,1])