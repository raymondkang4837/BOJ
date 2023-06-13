def solution(park, routes):
    col = len(park)
    row = len(park[0])
    
    # start point
    for i in range(col):
        for j in range(row):
            if park[i][j] == "S":
                x, y = i, j
    
    #direction vector
    dx = {"N":-1, "S":1, "W":0, "E":0}
    dy = {"N":0, "S":0, "W":-1, "E":1}

    for i in routes:
        d, n = i.split()
        n = int(n)
        cnt = 1

        while cnt <= n:
            p = x + dx[d]*cnt
            q = y + dy[d]*cnt
            if 0 <= p < col and 0 <= q < row and park[p][q] != "X":
                cnt += 1
            else:
                break
        if cnt > n:
            x, y = p, q
        else:
            continue
    return [x,y]        

