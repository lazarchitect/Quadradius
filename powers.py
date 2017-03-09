import random

def moveDiag():
	print("Hello, World!")


powerList = {
	"moveDiagonal": moveDiag,
	"a": 3,
	"c": 2
}

if __name__ == "__main__":
	print("Hello, World!")

	s = "moveDiagonal"

	powerList[s]

	print(random.choice(list(powerList.items())))