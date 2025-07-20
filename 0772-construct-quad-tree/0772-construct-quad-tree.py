class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def is_leaf(start, end):
            has_1 = False
            has_0 = False

            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    if grid[i][j] == 1:
                        has_1 = True
                    else:
                        has_0 = True

                    if has_1 and has_0:
                        return False

            return True

        def get_subtree(start, end):
            # s(0,0) e(3,3)
            # s(0,0) e(1,1) tl
            # s(0,2) e(1,3) tr
            # s(2,0) e(3,1)
            # s(2,2) e(3,3)
            start_row, start_col = start
            end_row, end_col = end
            mid_row = start_row + (end_row - start_row) // 2
            mid_col = start_col + (end_col - start_col) // 2

            return (
                ((start_row, start_col), (mid_row, mid_col)),  # tl
                ((start_row, mid_col + 1), (mid_row, end_col)),  # tr
                ((mid_row + 1, start_col), (end_row, mid_col)),  # bl
                ((mid_row + 1, mid_col + 1), (end_row, end_col)),  # br
            )

        # general_idea

        def r(start, end):
            if is_leaf(start, end):
                value = grid[start[0]][start[1]]

                return Node(value, True, None, None, None, None)
            else:
                value = 0
                tl, tr, bl, br = get_subtree(start, end)

                tl_node = r(tl[0], tl[1])
                tr_node = r(tr[0], tr[1])
                bl_node = r(bl[0], bl[1])
                br_node = r(br[0], br[1])

                return Node(value, False, tl_node, tr_node, bl_node, br_node)

        n = len(grid)
        return r((0, 0), (n - 1, n - 1))
