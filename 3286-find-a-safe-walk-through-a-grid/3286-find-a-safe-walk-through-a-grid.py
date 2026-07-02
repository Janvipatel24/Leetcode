class Solution:
    def findSafeWalk(self, grid, health):

        m = len(grid)
        n = len(grid[0])

        best = [[-1] * n for _ in range(m)]

        startHealth = health - grid[0][0]

        if startHealth <= 0:
            return False

        q = deque()

        q.append((0, 0, startHealth))

        best[0][0] = startHealth

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:

            x, y, hp = q.popleft()

            if x == m-1 and y == n-1:
                return True

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:

                    newHealth = hp - grid[nx][ny]

                    if newHealth <= 0:
                        continue

                    if newHealth > best[nx][ny]:

                        best[nx][ny] = newHealth

                        q.append((nx, ny, newHealth))

        return False
        