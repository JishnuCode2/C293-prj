
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 320


motorRPC = robot.getDevice("RPC")
motorRPF = robot.getDevice("RPF");
motorRMC = robot.getDevice("RMC");
motorRMF = robot.getDevice("RMF");
motorRAC = robot.getDevice("RAC");
motorRAF = robot.getDevice("RAF");

motorRPC.setPosition(0.0);
motorRPF.setPosition(0.0);
motorRMC.setPosition(0.0);
motorRMF.setPosition(0.0);
motorRAC.setPosition(0.0);
motorRAF.setPosition(0.0);

motorLPC = robot.getDevice("LPC");
motorLPF = robot.getDevice("LPF");
motorLMC = robot.getDevice("LMC");
motorLMF = robot.getDevice("LMF");
motorLAC = robot.getDevice("LAC");
motorLAF = robot.getDevice("LAF");

motorLPC.setPosition(0.0);
motorLPF.setPosition(0.0);
motorLMC.setPosition(0.0);
motorLMF.setPosition(0.0);
motorLAC.setPosition(0.0);
motorLAF.setPosition(0.0);

flag = 0;

while robot.step(timestep) != -1:
   
    if(flag%12 == 0):
       motorRPC.setPosition(-0.3);
       motorLPC.setPosition(0.8);
    if(flag%12 == 2):
       motorRMC.setPosition(-0.3);
       motorLMC.setPosition(0.8);
    if(flag%12 == 4):
       motorRAC.setPosition(-0.3);
       motorLAC.setPosition(0.8);
    if(flag%12 == 6):
       motorLPC.setPosition(-0.3);
       motorRPC.setPosition(0.8);
    if(flag%12 == 8):
       motorLMC.setPosition(-0.3);
       motorRMC.setPosition(0.8);
    if(flag%12 == 10):
       motorLAC.setPosition(-0.3);
       motorRAC.setPosition(0.8);
    flag+= 1 ;