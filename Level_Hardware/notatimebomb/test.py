import board
import digitalio
import time

print("Starting switch test...")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

col_pins = (board.GP9, board.GP10, board.GP12)
row_pins = (board.GP19, board.GP21, board.GP22)

cols = []
for pin in col_pins:
    col = digitalio.DigitalInOut(pin)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP
    cols.append(col)

rows = []
for pin in row_pins:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row.value = True
    rows.append(row)

def check_switches():
    pressed = False
    for row_num, row in enumerate(rows):
        row.value = False
        
        for col_num, col in enumerate(cols):
            if not col.value:
                print(f"Switch pressed at row {row_num + 1}, column {col_num + 1}")
                pressed = True
                
        row.value = True
        time.sleep(0.001)
    
    return pressed

print("Starting main loop...")
while True:
    if check_switches():
        led.value = True
        time.sleep(0.1)
        led.value = False
    else:
        led.value = False
    
    time.sleep(0.01)

