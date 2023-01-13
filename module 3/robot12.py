from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for f in range(100):
    robotArm.grab()
    if robotArm.scan() == 'red':
        for y in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()