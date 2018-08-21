#!/usr/bin/env python

import sys
from phue import Bridge

color = {
   'red': [0.6721, 0.2989],
   'yellow': [0.4876, 0.423],
   'normal': [0.3788, 0.3541]
}[sys.argv[1]]

b = Bridge('192.168.0.67')
b.set_light(['Gang','Stua'], 'on', True)
b.set_light(['Gang','Stua'], 'xy', color)
