"""
          __                 __    
  _______/  |______    ____ |  | __
 /  ___/\   __\__  \ _/ ___\|  |/ /
 \___ \  |  |  / __ \\  \___|    < 
/____  > |__| (____  /\___  >__|_ \
     \/            \/     \/     \/
                             .__                         
  ______ _____ _____    _____|  |__   ___________  ______
 /  ___//     \\__  \  /  ___/  |  \_/ __ \_  __ \/  ___/
 \___ \|  Y Y  \/ __ \_\___ \|   Y  \  ___/|  | \/\___ \ 
/____  >__|_|  (____  /____  >___|  /\___  >__|  /____  >
     \/      \/     \/     \/     \/     \/           \/ 

@author: Andrea Simeoni 
@date: 12/07/2017
"""

import sys
import os
import pyscreenshot as ImageGrab
import pythoncom, pyHook
import time


def printScreen():
    dest_dir = sys.argv[1] + '\\'
    now = str(int(time.time()))
    im = ImageGrab.grab()
    ImageGrab.grab_to_file(dest_dir + now + '.png')


def right_down(event):
    printScreen()
    return True


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit(
            '*****Usage*****\n- Run\n    python pyscreen.py [destdir]\n- Run in background\n    pythonw pyscreen.py [destdir]')
    elif not os.path.exists(sys.argv[1]):
        os.makedirs(sys.argv[1])

    hm = pyHook.HookManager()
    hm.SubscribeMouseRightDown(right_down)
    hm.HookMouse()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
    
