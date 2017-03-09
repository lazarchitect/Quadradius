import random

def moveDiag():
	print("Hello, World!")


powerList = {
	"moveDiagonal": moveDiag,
	"a": 3,
	"c": 2
}


s = "moveDiagonal"

powerList[s]

print(random.choice(list(powerList.items())))