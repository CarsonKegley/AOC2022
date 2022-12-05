with open("dayOne/data.txt", "r") as file:
    lines = file.readlines()

elves = []
currentBalance = 0

for line in lines:
    if line != ("" or "\n") :
        currentBalance += int(line)
    else:
        elves.append(currentBalance)
        currentBalance = 0 

print(sorted(elves).pop())

#Part Two
print(sum(sorted(elves)[len(elves)-3:]))