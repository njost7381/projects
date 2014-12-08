import time,mcpi.minecraft as mcpi
mc = mcpi.Minecraft.create()
pos = mc.player.getPos()

def house(x,y,z):
	mc.setBlocks(x+2,y,z+2,x+9,y+4,z+7,45)
	mc.setBlocks(x+3,y+1,z+3,x+8,y+3,z+6,0)
	mc.setBlock(x,y,z,x+6,y+2,z,0)
house(20,0,20)
house(30,0,20)
house(40,0,20)
