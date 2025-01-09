"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
 return the number of islands.

An island is surrounded by water
 and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
from collections import deque


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0  # Return 0 if the grid is empty.

        def BFS(r, c):
            """Perform BFS starting from cell (r, c)."""
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))  # Mark this cell as visited.

            while queue:
                row, col = queue.popleft()
                # Explore the four possible directions (up, down, left, right).
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    newRow, newColumn = row + dr, col + dc  # New row and column
                    # Check if the new cell is within bounds, is land ('1'), and not visited.
                    if (0 <= newRow < rows and 0 <= newColumn < cols and
                            grid[newRow][newColumn] == "1" and (newRow, newColumn) not in visit):
                        queue.append((newRow, newColumn))
                        visit.add((newRow, newColumn))

        rows = len(grid)
        cols = len(grid[0])
        visit = set()  # Set to keep track of visited cells.
        count = 0  # Initialize island count.

        for r in range(rows):
            for c in range(cols):
                # If the cell is land and not visited, it's a new island.
                if grid[r][c] == "1" and (r, c) not in visit:
                    BFS(r, c)  # Perform BFS to mark all connected land.
                    count += 1  # Increment the island count.

        return count
