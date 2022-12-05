def determineWinnerPartOne(you, me):
    if you == "A" and me == "X":
        return 3 + 1
    elif you == "A" and me == "Y":
        return 6 +2
    elif you == "A" and me == "Z":
        return 0 + 3 
    elif you == "B" and me == "X":
        return 0 + 1
    elif you == "B" and me == "Y":
        return 3 + 2
    elif you == "B" and me == "Z":
        return 6 + 3
    elif you == "C" and me == "X":
        return 6 + 1
    elif you == "C" and me == "Y":
        return 0 + 2
    elif you == "C" and me == "Z":
        return 3 + 3

def determineWinnerPartTwo(you, me):
    if you == "A" and me == "X":
        return 0 + 3
    elif you == "A" and me == "Y":
        return 3 + 1
    elif you == "A" and me == "Z":
        return 6 + 2 
    elif you == "B" and me == "X":
        return 0 + 1
    elif you == "B" and me == "Y":
        return 3 + 2
    elif you == "B" and me == "Z":
        return 6 + 3
    elif you == "C" and me == "X":
        return 0 + 2
    elif you == "C" and me == "Y":
        return 3 + 3
    elif you == "C" and me == "Z":
        return 6 + 1



def main():
    file = open("dayTwo/data.txt", "r")

    content = file.read()
    content_list = content.split("\n")


    # A = X = Rock = 1
    # B = Y = Paper = 2
    # C = Z = Scissors = 3

    totalPoints = 0
    totalPointsTwo = 0
    for line in content_list:
        opponentsShot = line[0]
        myShot = line[2]

        totalPoints += determineWinnerPartOne(opponentsShot, myShot)
        totalPointsTwo += determineWinnerPartTwo(opponentsShot,myShot)

    print(totalPoints)
    print(totalPointsTwo)
if __name__ =="__main__":
    main()