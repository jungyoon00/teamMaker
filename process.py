f = open("namelist.txt", 'r', encoding="utf-8")
context = f.read()
f.close()

division = context.split("\n\n")

gsa38 = division[0].split("\n")
gsa39 = division[1].split("\n")
gsa40 = division[2].split("\n")

GSA = [gsa38, gsa39, gsa40]

teams = []

for gsa in GSA:
    team = []
    for i in range(10):
        if i != 9:
            team.append(gsa[i*10:i*10+10])
        else:
            team.append(gsa[i*10:])
    teams.append(team)

teamslist = open("teams.txt", 'w')

for i in range(10):
    teamslist.write(f"<{i+1}조>\n")
    part = []
    for j in teams:
        part += j[i]
    for line in part:
        teamslist.write(line+"\n")
    teamslist.write("\n")

teamslist.close()