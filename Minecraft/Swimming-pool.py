import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

playerPos = mc.player.getPos()
 
mc.setBlocks(0,0,0,25,10,10,20)
mc.setBlocks(1,1,1,24,10,9,9)
mc.setBlocks(10,10,10,15,15,15,46)
