class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set) # key=(row /3, col/3)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if( board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row//3, col//3)]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        return True
# Time complexity O(square(9, 2)): inserting and accessing a elem in hashset takes O(1)
# Space Complexity O(square(9,2)): because of 9x9 grid