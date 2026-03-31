class soccer:
    def __init__(self, name, win):
        self.name = name
        self.win = win

    def print(self, M):
        if M >= self.win:
            print(f"{self.name}")

team = []

N = int(input())

for _ in range(N):
    name, win = map(int(input().split()))
    team.append(team(name, win))

for s in team:
    s.print()