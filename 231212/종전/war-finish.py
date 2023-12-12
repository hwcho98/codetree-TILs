import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# make square direction
dr = (-1,-1,1,1)
dc = (1,-1,-1,1)

# add direction
addr = (1,0,-1,0)
addc = (0,1,0,-1)

# there are 2 ways of direction, use function for convenience
def move(r,c,dr,dc,d):
    return r+dr[d], c+dc[d]

# make square (direction, answer)
def make_sq(d,ans):
    # when choosing last V, there is only one point can be V
    if d == 2:
        r, c = pos[-1]
        rr, cc = move(r, c, dr, dc, d)
        while (pos[0][0]-rr) != (pos[0][1]-cc):
            rr, cc = move(rr, cc, dr, dc, d)
        pos.append((rr, cc))
        tmp = cal()
        pos.pop()

        return min(ans, tmp)

    # for other cases, brute force
    r,c = pos[-1]
    rr,cc = move(r,c,dr,dc,d)
    while 0<=rr<n and 0<=cc<n:
        pos.append((rr,cc))
        ans = make_sq(d+1,ans)
        pos.pop()
        rr,cc = move(rr,cc,dr,dc,d)
    return ans

# calculate each # of group, devide into triangle and rectangle
# starting with each V of given rectangle,
# goes outward along the boundary line (line by line),
# as reaches the next vertex, and then calculate rest rectangle
def cal():
    # sum of each group
    s = [0]*5
    for t in range(4):
        tmp = 0
        r,c = pos[t]
        # calculate triangle first
        while (r,c) != pos[(t+1)%4]:
            rr,cc = move(r,c,addr,addc,t)
            while 0<=rr<n and 0<=cc<n:
                tmp += bd[rr][cc]
                rr,cc = move(rr,cc,addr,addc,t)
            r,c = move(r,c,dr,dc,t)
        # then rectangle: for each case
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
print(ans)