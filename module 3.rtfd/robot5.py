from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed=4
for x in range(1,8):
    robotArm.moveRight()
for x in range(3):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
