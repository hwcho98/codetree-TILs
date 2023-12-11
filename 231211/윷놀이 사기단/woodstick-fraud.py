# board idx, pedding -1 behind for goal
bd = (
    (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,31,-1,-1,-1,-1,-1),
    (5,20,21,22,28,29,30,31,-1,-1,-1,-1,-1),
    (10,23,24,28,29,30,31,-1,-1,-1,-1,-1),
    (15,25,26,27,28,29,30,31,-1,-1,-1,-1,-1)
)

# change direction idx
change = (5,10,15)

# score each idx
score = (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
         13,16,19,
         22,24,
         28,27,26,
         25,30,35,40,
         0)

# wether there is a marker
exist = [False]*33
pos = [(0,0) for _ in range(4)]

def dfs(idx,sc):
    if idx == 10:
        global ans
        ans = max(ans,sc)
        return
    
    m = move[idx]
    for i in range(4):
        w,p = pos[i]
        # if cur position is goal, skip
        cur = bd[w][p]
        if cur < 0: continue
        
        # if another marker already exist, skip
        dest = bd[w][p+m]
        if exist[dest]: continue
        
        # if marker is on 5,10,15, renew pos
        neww,newp = w,p+m
        if dest in change:
            neww,newp = dest//5,0
        
        # update state
        exist[cur] = False
        # if a marker reaches goal, donot save exisitence
        if dest > 0:
            exist[dest] = True
        pos[i] = (neww,newp)
        
        dfs(idx+1,sc+score[dest])
        
        # restore state
        pos[i] = (w,p)
        exist[cur] = True
        exist[dest] = False

move = list(map(int,input().split()))
ans = 0
dfs(0,0)
print(ans)
