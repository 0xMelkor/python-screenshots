import sys
import os
import pyscreenshot as ImageGrab
import pythoncom, pyHook
import time
import threading


def printScreen():
    dest_dir = sys.argv[1] + '\\'
    now = str(int(time.time()))
    im = ImageGrab.grab()
    ImageGrab.grab_to_file(dest_dir + now + '.png')


def right_down(event):
    t = threading.Thread(target=printScreen) #added to queue
    t.start()
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
