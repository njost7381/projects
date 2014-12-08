import time,mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
while True:
    mc.player.setPos(90,90,90)
    time.sleep(2)
    mc.player.setPos(123,221,123)
    time.sleep(2)
    mc.player.setPos(10,20,40)
    time.sleep(2)
mc.postToChat("teleportation complete")
