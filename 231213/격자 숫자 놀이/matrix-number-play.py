import sys
input = sys.stdin.readline

n = 100

def play(flag):
    tmp = [[0] * n for _ in range(n)]
    max_idx = 0
    global h,w
    if flag:
        for r in range(n):
            cnt = [0] * 101
            key = []
            for c in range(n):
                if bd[r][c] > 0:
                    cnt[bd[r][c]] += 1
            for i, v in enumerate(cnt):
                if i * v > 0:
                    key.append((v, i))
            key.sort()
            for idx, k in enumerate(key[:50]):
                cnt, val = k[0], k[1]
                tmp[r][2 * idx:2 * idx + 2] = [val, cnt]
            max_idx = max(max_idx,2*idx+1)
        w = max_idx
    else:
        for c in range(n):
            cnt = [0] * 101
            key = []
            for r in range(n):
                if bd[r][c] > 0:
                    cnt[bd[r][c]] += 1
            for i, v in enumerate(cnt):
                if i * v > 0:
                    key.append((v, i))
            key.sort()
            for idx, k in enumerate(key[:50]):
                cnt, val = k[0], k[1]
                tmp[2 * idx][c] = val
                tmp[2 * idx + 1][c] = cnt
            max_idx = max(max_idx,2*idx+1)
        h = max_idx
    return tmp, tmp[R][C] == K


R, C, K = map(int, input().split())
R -= 1; C -= 1
bd = [[0] * n for _ in range(n)]
for i in range(3):
    bd[i][:3] = list(map(int, input().split()))
h, w = 2,2
done = False
ans = -1
if bd[R][C] == K:
    print(0)
    exit()
for turn in range(1, n+1):
    bd, done = play(h >= w)
    if done:
        ans = turn
        break
print(ans)