from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.grab()
for x in range(9):
    robotArm.moveRight()
robotArm.drop()
for x in range(4):
    for x in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for x in range(4):
        robotArm.moveRight()
    robotArm.drop()