def who_lose(arr):
    if arr[1]>arr[3]:
        return arr[2]
    else:
        return arr[0]
def who_win(arr):
    if arr[1]<arr[3]:
        return arr[2]
    else:
        return arr[0]


def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

count=int(input())
matches = [input().split(';') for i in range(0,count)]

teams=[]
for i in matches:
    teams.append(i[0])
    teams.append(i[2])
teams=unique(teams)

games={}
wins={}
loses={}
par={}
scores={}

for i in teams:
    games.setdefault(i,0)
    wins.setdefault(i, 0)
    loses.setdefault(i, 0)
    par.setdefault(i, 0)
    scores.setdefault(i, 0)


for match in matches:
    games[match[0]] += 1
    games[match[2]] += 1
    if match[1]==match[3]:
        par[match[0]] += 1
        par[match[2]] += 1
        scores[match[0]] += 1
        scores[match[2]] += 1
    else:
        wins[who_win(match)] += 1
        scores[who_win(match)] += 3
        loses[who_lose(match)] += 1

for team in teams:
    print(team+":"+str(games[team])+" "+str(wins[team])+" "+str(par[team])+" "+str(loses[team])+" "+str(scores[team]))