import random, mcpi.minecraft as minecraft, time

mc= minecraft.Minecraft.create()

while True:
	pos = mc.player.getPos()
	x =int(pos.x)
	y =int(pos.y)
	z =int(pos.z)
	Block = 13
	xg = random.randint(x-10,x+10)
	zg = random.randint(z-10,z+10)
	mc.setBlock(xg,y+50,zg,Block)
	time.sleep(0.2)
