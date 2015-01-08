import time,mcpi.minecraft as minecraft # imports the time, mcpi.minecraft as minecraft libraries 
mc = minecraft.Minecraft.create()
#this project is my space invader which changes colour and does a ripple effect to do this


def space(x,y,z): # defines the space function with parameters xyz
	for block in(3,9):# for block 3 to 9 set block, (3-9) y+8 , z, and block 22. 
        	mc.setBlock(block,y+8,z,22)
	for block in(4,8):
        	mc.setBlock(block,y+7,z,22)
	for block in range(3,10):
        	mc.setBlock(block,y+6,z,22)
	for block in(2,3,5,6,7,9,10):
        	mc.setBlock(block,y+5,z,22)
	for blocks in range(1,12):
        	mc.setBlock(blocks,y+4,z,22)
	for block in(1,3,4,5,6,7,8,9,11):
		mc.setBlock(block,y+3,z,22)
	for block in(1,3,9,11):
		mc.setBlock(block,y+2,z,22)
	for block in(4,5,7,8):
		mc.setBlock(block,y+1,z,22)
def space2(x,y,z):
  	for block in(3,9):
                mc.setBlock(block,y+8,z,24)
        for block in(4,8):
                mc.setBlock(block,y+7,z,24)
        for block in range(3,10):
                mc.setBlock(block,y+6,z,24)
        for block in(2,3,5,6,7,9,10):
                mc.setBlock(block,y+5,z,24)
        for blocks in range(1,12):
                mc.setBlock(blocks,y+4,z,24)
        for block in(1,3,4,5,6,7,8,9,11):
                mc.setBlock(block,y+3,z,24)
        for block in(1,3,9,11):
                mc.setBlock(block,y+2,z,24)
 	for block in(4,5,7,8):
                mc.setBlock(block,y+1,z,24)
while True: #do this forever
	space (0,0,0)
	time.sleep(1)
	space2(0,0,0)
