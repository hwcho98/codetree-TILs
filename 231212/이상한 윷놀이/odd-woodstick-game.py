R, C, D = 0, 1, 2
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

def int_(i): return int(i) - 1
def toggle(d):
    if d & 1: return d - 1
    return d + 1

n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
bd = [[[] for _ in range(n)] for _ in range(n)]
marker = [[0, 0, 0]] + [list(map(int_, input().split())) for _ in range(k)]
for m in range(1, k + 1):
    r, c, d = marker[m]
    bd[r][c] = [m]
ans = 0
done = False
for turn in range(1, 1001):
    for m in range(1, k + 1):
        r, c, d = marker[m]
        idx = bd[r][c].index(m)
        tmp = bd[r][c][idx:]

        rr = r + dr[d]
        cc = c + dc[d]
        if 0 <= rr < n and 0 <= cc < n:
            if color[rr][cc] == 0:
                bd[r][c][idx:] = []
                bd[rr][cc].extend(tmp)
                for mm in tmp:
                    marker[mm][:2] = [rr, cc]
            elif color[rr][cc] == 1:
                bd[r][c][idx:] = []
                bd[rr][cc].extend(tmp[::-1])
                for mm in tmp:
                    marker[mm][:2] = [rr, cc]
            elif color[rr][cc] == 2:
                d = toggle(d)
                marker[m][D] = d
                rr = r + dr[d]
                cc = c + dc[d]

                if 0 <= rr < n and 0 <= cc < n:
                    if color[rr][cc] == 0:
                        bd[r][c][idx:] = []
                        bd[rr][cc].extend(tmp)
                        for mm in tmp:
                            marker[mm][:2] = [rr, cc]

                    elif color[rr][cc] == 1:
                        bd[r][c][idx:] = []
                        bd[rr][cc].extend(tmp[::-1])
                        for mm in tmp:
                            marker[mm][:2] = [rr, cc]
        else:
            d = toggle(d)
            marker[m][D] = d
            rr = r + dr[d]
            cc = c + dc[d]

            if 0 <= rr < n and 0 <= cc < n:
                if color[rr][cc] == 0:
                    bd[r][c][idx:] = []
                    bd[rr][cc].extend(tmp)
                    for mm in tmp:
                        marker[mm][:2] = [rr, cc]
                    # marker[m][D] = d
                elif color[rr][cc] == 1:
                    bd[r][c][idx:] = []
                    bd[rr][cc].extend(tmp[::-1])
                    for mm in tmp:
                        marker[mm][:2] = [rr, cc]

        if 0 <= rr < n and 0 <= cc < n and len(bd[rr][cc]) >= 4:
            ans = turn
            done = True
            break
    if done: break

else:
    ans = -1
print(ans)