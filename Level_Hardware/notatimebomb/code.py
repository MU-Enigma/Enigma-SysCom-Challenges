print("Starting")

import board
import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9, board.GP10, board.GP12) # Cols
keyboard.row_pins = (board.GP19, board.GP21, board.GP22) # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

CMD_TAB = KC.LGUI(KC.TAB)
FULL_SCREEN = KC.LCTRL(KC.LCMD(KC.F))
CMD_OPTN_ESC = KC.LGUI(KC.LALT(KC.ESC))
F1 = KC.F1
CMD_W = KC.LGUI(KC.W)

# Keymap
keyboard.keymap = [
    [
        CMD_TAB, CMD_OPTN_ESC, FULL_SCREEN,
        F1, CMD_W, KC.N6,
        KC.N7, KC.N8, KC.N9,
    ]
]
if __name__ == '__main__':
    keyboard.go()

