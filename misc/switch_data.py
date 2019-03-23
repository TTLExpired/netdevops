import sys
import os

from netmiko import ConnectHandler
from getpass import getpass


class Switch:
    ''' Module, Ports and OS '''
    def __init__(self, module, platform, firmware):
        self.module = module
        self.platform = platform
        self.firmware = firmware
        