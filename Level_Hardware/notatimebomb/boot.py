import board
import digitalio
import storage
import usb_cdc
import usb_midi
import usb_hid
import time

col_pin = digitalio.DigitalInOut(board.GP9)
row_pin = digitalio.DigitalInOut(board.GP19)

col_pin.direction = digitalio.Direction.INPUT
col_pin.pull = digitalio.Pull.UP
row_pin.direction = digitalio.Direction.OUTPUT

def check_switch():
    row_pin.value = False
    time.sleep(0.001)
    is_pressed = not col_pin.value
    row_pin.value = True
    return is_pressed

time.sleep(0.5)

if check_switch():
    print("Switch pressed - maintaining full USB access")
    try:
        usb_cdc.enable()
        usb_midi.enable()
        storage.enable_usb_drive()
        usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)
    except Exception as e:
        print(f"Error enabling USB features: {e}")
else:
    print("Switch not pressed - entering keyboard-only mode")
    try:
        usb_cdc.disable()
        usb_midi.disable()
        storage.disable_usb_drive()
        usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)
    except Exception as e:
        print(f"Error configuring USB: {e}")
        usb_cdc.enable()
        storage.enable_usb_drive()

# Clean up pins
col_pin.deinit()
row_pin.deinit()