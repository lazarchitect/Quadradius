#This fn is just for adding duplicates of powers to the powerlist for probability manipulation 
#when selecting a power at random.
def duplicate(func, num):
	retval = []
	for i in range(num):
		retval.append(func)
	return retval	

def recruit():
	pass
def swap():
	pass
def wall():
	pass
def plateau():
	pass
def trench():
	pass
def moat():
	pass
def raiseTile():
	pass
def lowerTile():
	pass
def dredge():
	pass
def invert():
	pass
def tripwire():
	pass	
def destroy():
	pass
def acidic():
	pass	
def kamikaze():
	pass
def bombs():
	pass
def smartBombs():
	pass
def inhibit():
	pass
def snakeTunneling():
	pass
def parasite():
	pass
def spyware():
	pass
def pilfer():
	pass
def beneficiary():
	pass
def teach():
	pass
def learn():
	pass
def climb():
	pass
def flatToSphere():
	pass
def moveDiagonal():
	pass
def jumpProof():
	pass
def growQuadradius():
	pass
def scavenger():
	pass
def purify():
	pass
def relocate():
	pass
def scramble():
	pass
def bankrupt():
	pass
def hotspot():
	pass
def refurb():
	pass
def orbSpy():
	pass
def bunker():
	pass
def moveAgain():
	pass
def multiply():
	pass
def orbicRehash():
	pass

powerList = []
powerList += duplicate(recruit, 1)
powerList += duplicate(swap, 3)

powerList += duplicate(wall, 5)
powerList += duplicate(plateau, 5)
powerList += duplicate(trench, 5)
powerList += duplicate(moat, 3)
powerList += duplicate(raiseTile, 5)
powerList += duplicate(lowerTile, 5)
powerList += duplicate(dredge, 3)
powerList += duplicate(invert, 4)

powerList += duplicate(tripwire, 4)
powerList += duplicate(destroy, 2)
powerList += duplicate(acidic, 3)
powerList += duplicate(kamikaze, 4)
powerList += duplicate(bombs, 3)
powerList += duplicate(smartBombs, 1)
powerList += duplicate(inhibit, 4)
powerList += duplicate(snakeTunneling, 2)

powerList += duplicate(parasite, 3)
powerList += duplicate(spyware, 4)
powerList += duplicate(pilfer, 4)

powerList += duplicate(beneficiary, 3)
powerList += duplicate(teach, 4)
powerList += duplicate(learn, 4)

powerList += duplicate(climb, 5)
powerList += duplicate(flatToSphere, 4)
powerList += duplicate(moveDiagonal, 4)
powerList += duplicate(jumpProof, 2)
powerList += duplicate(growQuadradius, 5)
powerList += duplicate(scavenger, 3)
powerList += duplicate(purify, 4)

powerList += duplicate(relocate, 5)
powerList += duplicate(scramble, 4)

powerList += duplicate(bankrupt, 2)
powerList += duplicate(hotspot, 3)
powerList += duplicate(orbSpy, 3) #ORB SPY ALLOWS U TOO SEE ORBS ON TILES
powerList += duplicate(refurb, 3)
#also bunker possibly

powerList += duplicate(moveAgain, 4)
powerList += duplicate(multiply, 4)
powerList += duplicate(orbicRehash, 5)


# if __name__ == "__main__":
# 	import random
# 	print(random.choice(powerList))
	
	
	
	