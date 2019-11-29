import time

from .c_struct_definitions import *
from .helpers import *

E_KEY_CODE = 0x12
DELAY_AFTER_MOVE_DOWN = 1


def press_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = InputI()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def release_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = InputI()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def move_mouse(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = InputI()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))
    cmd = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(cmd), ctypes.sizeof(cmd))


def main():
    args = parse_args()
    time.sleep(args['delay'])
    while True:
        press_key(E_KEY_CODE)
        release_key(E_KEY_CODE)
        time.sleep(args['wait'])
        move_mouse(0, args['move'])
        time.sleep(DELAY_AFTER_MOVE_DOWN)
