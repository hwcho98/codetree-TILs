import sys
from collections import deque
input = sys.stdin.readline

dr = (1,0,-1,0)
dc = (0,1,0,-1)

def choose(cnt,idx):
    if cnt == m:
        bfs()
        return
    for i in range(idx,l):
        chosen.append(hospital[i]+(0,))
        choose(cnt+1,i+1)
        chosen.pop()

def bfs():
    vis = [[False]*n for _ in range(n)]
    for r,c,_ in chosen:
        vis[r][c] = True
    cnt = 0
    q = deque(chosen)
    while q:
        r,c,s = q.popleft()
        for t in range(4):
            rr = r+dr[t]
            cc = c+dc[t]
            if 0<=rr<n and 0<=cc<n and not vis[rr][cc]:
                vis[rr][cc] = True
                if bd[rr][cc] == 0:
                    cnt += 1
                    if virus == cnt:
                        global ans
                        ans = min(ans,s+1)
                        return
                    q.append((rr,cc,s+1))
                elif bd[rr][cc] == 2:
                    q.append((rr,cc,s+1))


n,m = map(int,input().split())
bd = [list(map(int,input().split())) for _ in range(n)]
virus = 0
hospital,chosen = [],[]
for i in range(n):
    for j in range(n):
        if bd[i][j] == 0: virus += 1
        elif bd[i][j] == 2: hospital.append((i,j))
l = len(hospital)
ans = 2500*(virus>0)
choose(0,0)
print(ans if ans < 2500 else -1)