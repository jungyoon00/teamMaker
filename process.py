f = open("namelist.txt", 'r', encoding="utf-8")  # 이름 리스트 읽기
context = f.read()
f.close()

division = context.split("\n\n")

gsa38 = division[0].split("\n")
gsa39 = division[1].split("\n")
gsa40 = division[2].split("\n")

GSA = [gsa38, gsa39, gsa40]

teams = []

for gsa in GSA:   # 38, 39, 40기에 반복한다.
    team = []   # 한 기수를 10개의 팀으로 나누고 하나의 리스트로 묶는다.
    for i in range(10):
        if i != 9:
            team.append(gsa[i*10:i*10+10])
        else:
            team.append(gsa[i*10:])    # 완벽히 100명이 아니므로 마지막은 그냥 추가한다.
    teams.append(team)  # 전체 팀 리스트에 이 기수의 팀들(team)을 추가한다.

# 현재 팀즈의 상태: teams = [[gsa38 teams], [gsa39 teams], [gsa40 teams]]

teamslist = open("teams.txt", 'w')

for i in range(10):
    teamslist.write(f"<{i+1}조>\n")
    part = []
    for j in teams:   # 각 기수에서 10명 씩 나누어진 리스트를 가져옴
        part += j[i]  # 인스턴스한 변수로 한 조의 본문을 만듦
    for line in part:
        teamslist.write(line+"\n")  # 파일에 씀
    teamslist.write("\n")

teamslist.close()