def find_max_rectangle(heights):
    indices_stack = []
    max_rectangle = 0
    for index, height in enumerate(heights + [-1]):
        while indices_stack and heights[indices_stack[-1]] >= height:
            popped = indices_stack.pop(-1)
            left_bound = indices_stack[-1] if indices_stack else -1
            max_rectangle = max(
                max_rectangle,
                (index - left_bound - 1) * heights[popped],
            )
        indices_stack.append(index)
        print(indices_stack)

    return max_rectangle


def maximal_rectangle(matrix):
    if not matrix:
        return 0

    max_rectangle = 0
    heights = [0] * len(matrix[0])
    for row in matrix:
        for index, num in enumerate(row):
            heights[index] = heights[index] + 1 if num else 0
        max_rectangle = max(
            max_rectangle,
            find_max_rectangle(heights),
        )

    return max_rectangle


matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]

print(maximal_rectangle(matrix))
