import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dr = (-1,-1,1,1)
dc = (1,-1,-1,1)

addr = (1,0,-1,0)
addc = (0,1,0,-1)

mover = (0,-1,0,1)
movec = (1,0,-1,0)

def move(r,c,dr,dc,d):
    return r+dr[d], c+dc[d]

def make_sq(d,ans):
    # print(pos)
    if d == 2:
        r, c = pos[-1]
        rr, cc = move(r, c, dr, dc, d)
        while (pos[0][0]-rr) != (pos[0][1]-cc):
            rr, cc = move(rr, cc, dr, dc, d)
        pos.append((rr, cc))
        tmp = cal()
        pos.pop()

        return min(ans, tmp)

    r,c = pos[-1]
    rr,cc = move(r,c,dr,dc,d)
    # rr = r+dr[d]
    # cc = c+dc[d]
    while 0<=rr<n and 0<=cc<n:
        pos.append((rr,cc))
        ans = make_sq(d+1,ans)
        pos.pop()
        rr,cc = move(rr,cc,dr,dc,d)
        # rr+=dr[d]
        # cc+=dc[d]
    return ans

def cal():
    # print(1)
    s = [0]*5
    for t in range(4):
        tmp = 0
        r,c = pos[t]
        while (r,c) != pos[(t+1)%4]:
            rr,cc = move(r,c,addr,addc,t)
            # rr = r+addr[t]
            # cc = r+addc[t]
            while 0<=rr<n and 0<=cc<n:
                tmp += bd[rr][cc]
                rr,cc = move(rr,cc,addr,addc,t)
            r,c = move(r,c,dr,dc,t)
        # print(tmp)
        rr,cc = move(r,c,addr,addc,t)
        if t == 0:
            for i in range(rr,n):
                for j in range(cc,n):
                    tmp += bd[i][j]
        elif t == 1:
            for i in range(rr+1):
                for j in range(cc,n):
                    tmp += bd[i][j]
        elif t == 2:
            for i in range(rr+1):
                for j in range(cc+1):
                    tmp += bd[i][j]
        elif t == 3:
            for i in range(rr,n):
                for j in range(cc+1):
                    tmp += bd[i][j]
        s[t] = tmp
        # print(s)
    s[4] = total-sum(s)
    return max(s)-min(s)



n = int(input())
bd = [list(map(int,input().split())) for _ in range(n)]
total = 0
for b in bd:
    total += sum(b)
ans = 40000
pos = []
for r in range(2,n):
    for c in range(1,n-1):
        pos = [(r,c)]
        tmp = make_sq(0,40000)
        ans = min(ans,tmp)
        # print(ans)
print(ans)