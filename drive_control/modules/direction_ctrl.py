import cart_module as m
import logging

# Drive Computer Core Library
# Direction Controller Module
#
# This module controls both steering and braking
#
# Hardware definition class to store messages for this module
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class Direction_Controller:

    def __int__(self, can_address = 4081):
        # CAN Address
        self.can_address = can_address

        # Components
        self.steering_motor = self.Steering_Motor(can_address=self.can_address)
        self.steering_mode = self.Steering_Mode(can_address=self.can_address)
        self.wheel_input = self.Wheel(can_address=self.can_address)
        self.brake_motor = self.Brake_Motor(can_address=self.can_address)

        # Setup the message logging
        logging.basicConfig(filename='direction_ctrl.log', filemode='w', format=' %(asctime)s - %(message)s')

    
    # ----------------------------
    # Steering Motor Controller
    # ----------------------------

    class Steering_Motor:

        def __init__(self, can_address):
            self.can_address = can_address

        # Disable Steering Motor
        def disable(self):
            logging.debug("Disabling Steering Motor")
            return f"({self.can_address}) {m.set} 1 10 1 {m.fill(4)}"

        # Enable Steering Motor
        def enable(self):
            logging.debug("Enabling Steering Motor")
            return f"({self.can_address}) {m.set} 1 10 2 {m.fill(4)}"

        def reqStatus(self):
            logging.debug("Requesting the Steering Motor Status")
            return f"({self.can_address}) {m.get} 1 10 {m.fill(5)}"

        def checkStatusResponse(self, message):
            pass
    
        def readStatus(self, message):
            pass

        def forwards(self, power = 255):
            pass

        def backwards(self, power = 255):
            pass

        def setPos(self, pos):
            pass

        def reqPos(self):
            pass
    
    # ----------------------------
    # Steering Mode
    # ----------------------------

    class Steering_Mode:

        def __init__(self, can_address):
            self.can_address = can_address

        def setControlledSteering(self):
            pass

        def setWheelInputSteering(self):
            pass

        def reqSteeringMode(self):
            pass

    # ----------------------------
    # Steering Wheel Input
    # ----------------------------

    class Wheel:

        def __init__(self, can_address):
            self.can_address = can_address

        def getPos(self):
            pass

        def setSpeed(self, power = 128):
            pass

    class Brake_Motor:

        def __init__(self, can_address):
            self.can_address = can_address

        def disable(self):
            pass

        def enable(self):
            pass

        def reqStatus(self):
            pass

        def checkStatusResponse(self, message):
            pass
    
        def readStatus(self, message):
            pass

        def forwards(self, power = 255):
            pass

        def backwards(self, power = 255):
            pass

        def resetEncoder(self):
            pass

        def reqEncoderTicks(self):
            pass

        def checkTicksResponse(self, message):
            pass
    
        def readTicks(self, message):
            pass