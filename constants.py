from enum import Enum

bots= ["bot1","bot2","bot3"]

maze1 = [
[1,0,-1],
[1,-1,0],
[-1,1,0],
[0,-1,1],
[1,-1,0],
]
mazeLength = 5
mazeDoor = 3


steppingGlass = [
[1,0],
[1,0],
[1,0],
[0,1],
[1,0],
]
steppingGlassLength = 5

rockPaperScissor1 = [
1,1,3,2,3
]

rockPaperScissorLength = 5






class Superpower(Enum):
	EnhancedReflex = 1
	SuperStrength = 2
	EnhancedVision = 3

superpowerDescription = [
	"Advantage in rock paper scissors. Get to know oppponents hand signs faster",
	"Advantage in maze escape. Break any door and pass the level",
	"Advantage in stepping stone. Get to know about the properties of steps"
]