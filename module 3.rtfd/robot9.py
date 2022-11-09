from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for x in range(13):
    robotArm.grab()
    if x == 1:
        robotArm.moveRight()
    if x == 4:
        robotArm.moveRight()
    if x == 8:
        robotArm.moveRight()
    for x in range(1,6):
        robotArm.moveRight()
    robotArm.drop() 
    for x in range(1,6):
        robotArm.moveLeft()

robotArm.wait()
