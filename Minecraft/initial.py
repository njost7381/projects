import time,mcpi.minecraft as mcpi
mc = mcpi.Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
def n(x,y,z):
	mc.setBlocks(x,y,z,x,y+6,z,35)
	mc.setBlocks(x+4,y,z,x+4,y+6,z,35)
	mc.setBlock(x+1,y+4,z,35)
	mc.setBlock(x+2,y+3,z,35)
	mc.setBlock(x+3,y+2,z,35)
def j(x,y,z):
	mc.setBlock(x,y+2,z,35)
	mc.setBlocks(x+1,y,z,x+2,y,z,35)
	mc.setBlocks(x+3,y+1,z,x+3,y+5,z,35)
	mc.setBlocks(x+2,y+6,z,x+4,y+6,z,35)

n(35,5,20)
j(42,10,25)
