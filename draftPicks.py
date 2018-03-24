import sys
if __name__ == '__main__':
    print('Welcome! Find out your pick position in a serpentine draft!')
    numOfTeams = input('How many teams are picking in your league? ')
    yourPick = input('What is your draft position? ')
    order = []
    count = 1
    currTeamPick = 1
    backwards = 0
    forwards = 1
    currentRound = 1

    def forwardOrder():
        global count
        global currTeamPick
        global backwards
        global forwards
        for i in range(1, int(numOfTeams)+1):
            if int(yourPick) == int(currTeamPick):
                print(count)

            if currTeamPick == int(numOfTeams):
                backwards = 1
                forwards = 0
            else:
                currTeamPick += 1
            count += 1

    def backwardOrder():
        global count
        global currTeamPick
        global backwards
        global forwards
        for i in range(1, int(numOfTeams)+1):
            if int(yourPick) == int(currTeamPick):
                print(count)

            if currTeamPick == 1:
                backwards = 0
                forwards = 1
            else:
                currTeamPick -= 1
            count += 1



    for num in range(1,int(numOfTeams) +1):
        order.append(num)

    while currentRound < 26:
        if forwards == 1:
            forwardOrder()
            currentRound += 1
        elif backwards == 1:
            backwardOrder()
            currentRound += 1

