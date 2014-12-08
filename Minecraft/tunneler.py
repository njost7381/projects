import time, mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos= mc.player.getPos()

mc.setBlock(pos.x+1,pos.y+1,0)
