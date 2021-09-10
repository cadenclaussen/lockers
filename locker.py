# This is for the money variant. This one is where person #1 puts $1 then #2 puts 2$ and so on
import sys

lockerCount = int(sys.argv[1])
studentCount = int(sys.argv[2])
lockers = {}
optimal = 0

for lockerNumber in range(lockerCount):
	lockers[lockerNumber] = 0

for lockerNumber in range(1, lockerCount):
	for studentNumber in range(1, studentCount):
		if lockerNumber % studentNumber == 0:
			lockers[lockerNumber] += studentNumber

print(lockers)
for value in lockers.values():
	if value > optimal:
		optimal = value

for key in lockers.keys():
	if lockers[key] == optimal:
		perfect = key

print("")
print("The optimal solution is: #" + str(perfect) + " with $" + str(optimal))

while True:
	find = input("What do you want? ")
	if find == "quit":
		break
	else:
		print(lockers[int(find)])

