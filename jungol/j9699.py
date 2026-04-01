N, M = map(int,input().split())
team = []

class Soccer:
    def __init__(self, name, win):
        self.name = name
        self.win = win

for _ in range(N):
    name, win = input().split()
    win = int(win)           
    team.append(Soccer(name, win))

for s in reversed(team):
    if s.win >= M:
        print(s.name)