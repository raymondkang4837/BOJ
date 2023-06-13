def solution(wallpaper):
    col = len(wallpaper)
    row = len(wallpaper[0])

    x = set()
    y = set()

    for i in range(col):
        for j in range(row):
            if wallpaper[i][j] == "#":
                x.add(j)
                y.add(i)

    return [min(y),min(x),max(y)+1,max(x)+1]