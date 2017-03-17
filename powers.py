import random

def splay(func, num):
	retval = []
	for i in range(num):
		retval.append(func)
	return retval	

def moveDiagonal():
	print("mdiag")

def flatToSphere():
	print("f2s")

powerList = []
powerList += splay(moveDiagonal, 2)
powerList += splay(flatToSphere, 2)


if __name__ == "__main__":
	print(random.choice(powerList))