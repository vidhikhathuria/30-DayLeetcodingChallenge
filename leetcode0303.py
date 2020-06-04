# Problem Link : https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(visited, i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if visited[i][j]:
                return 0
            visited[i][j] = 1
            if grid[i][j] == '0':
                # print(i, j, grid[i][j])
                return 0
            else:
                # print(i, j,grid[i][j])
                return dfs(visited, i + 1, j, grid) + dfs(visited, i - 1, j, grid) + dfs(visited, i, j - 1, grid) + dfs(visited, i, j + 1, grid) + 1
        visited = [[0 for i in grid[0]] for j in grid]
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # for k in visited:
                #     print(k)
                # print()
                if visited[i][j] == 0 and grid[i][j] == '1':
                    dfs(visited, i, j, grid)
                    c += 1
        return c