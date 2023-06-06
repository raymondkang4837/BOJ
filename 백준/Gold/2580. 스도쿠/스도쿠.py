# 스도쿠 프로그램 만들기
mat = [list(map(int, input().split())) for _ in range(9)]

vst1 = [[False]*9 for _ in range(9)] # vst[i][j] i행에 숫자j가 들어 있는가
vst2 = [[False]*9 for _ in range(9)] # vst2[i][j] i열에 숫자j가 들어 있는가
vst3 = [[False]*9 for _ in range(9)] # vst3[i][j] i번쨰 그룹칸에 숫자 j가 들어 있는가

def group(i,j):
    return i//3*3 + j//3

# vst 배열들을 전부 채워주기
for i in range(9):
    for j in range(9):
        if mat[i][j]:
            vst1[i][mat[i][j]-1] = True
            vst2[j][mat[i][j]-1] = True
            vst3[group(i,j)][mat[i][j]-1] = True
        
# i,j에 들어갈 숫자를 백트레킹 기법으로 맞추는 함수
def track(i,j):
    if i==9:
        return True
    if mat[i][j]: # 해당 위치에 숫자가 있는지
        return track(i+(j+1)//9,(j+1)%9) #있으면 다음 위치로
    
    # 없으면 숫자 집어넣기
    
    for k in range(9):
        if vst1[i][k] or vst2[j][k] or vst3[group(i,j)][k]:
            continue # 행, 열, 군에 숫자가 있으면 생략
        mat[i][j] = k+1
        vst1[i][k] = vst2[j][k] = vst3[group(i,j)][k] = True
        if track(i+(j+1)//9,(j+1)%9):
            return True # 만약에 다음 트랙에서 오류가 발생되지 않으면 함수 종료
        mat[i][j] = 0
        vst1[i][k] = vst2[j][k] = vst3[group(i,j)][k] = False

# 함수 실행
track(0,0)
for i in mat:
    print(*i)