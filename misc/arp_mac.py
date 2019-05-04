from napalm import get_network_driver

import json

# A small script to get ip to mac table

# Get the drivers
ios_driver = get_network_driver('ios')
iosxr_driver = get_network_driver('iosxr')

devices = ['10.47.254.252',
           '10.47.254.251',
           '10.0.7.254',
           '10.0.7.253']

