import mcpi.minecraft as minecraft, time as t #importing time and minecraft modules
mc = minecraft.Minecraft.create()#connecting to minecraft game

#move player close to origin
mc.player.setPos(10,10,0)

black=7
red=14
orange=1
green=5

mc.setBlock(0,0,0,35,black)#setting blocks to game
mc.setBlock(0,1,0,35,black)
mc.setBlock(0,2,0,35,black)
mc.setBlock(0,3,0,35,black)
mc.setBlock(0,4,0,35,black)
mc.setBlock(0,5,0,35,black)
mc.setBlock(0,6,0,35,black)
t.sleep(1)
while True:
	mc.setBlock(0,5,0,35,black)
	mc.setBlock(0,6,0,35,red)
	t.sleep(10)
	mc.setBlock(0,5,0,35,orange)
	mc.setBlock(0,6,0,35,red)
	t.sleep(2)
	mc.setBlock(0,5,0,35,black)
	mc.setBlock(0,6,0,35,black)
	mc.setBlock(0,4,0,35,green)
	t.sleep(10)
	mc.setBlock(0,5,0,35,orange)
	mc.setBlock(0,6,0,35,black)
	mc.setBlock(0,4,0,35,black)
	t.sleep(2) 
