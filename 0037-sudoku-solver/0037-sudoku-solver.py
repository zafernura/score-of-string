class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3)*3 + (c//3)].add(num)

        def backtrack(i):
            if i == len(empty):
                return True

            r, c = empty[i]
            b = (r//3)*3 + (c//3)

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(i + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack(0)