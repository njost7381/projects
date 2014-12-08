# Demonstration of for loops in python
import mcpi.minecraft as minecraft ,random,time
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)#clears an area.
#loops through 0-14 using these for the y coord and colour.
for b in range(14,0,-1) :
	mc.postToChat(b)
	mc.setBlock(0,b,0,35,b)
	time.sleep(3)
