# boot.py — Seeed XIAO RP2040 (KMK-safe)

import usb_cdc
import usb_hid
import storage
import board

# Enable USB HID (keyboard)
usb_hid.enable((usb_hid.Device.KEYBOARD,))

# Enable USB serial (REPL)
usb_cdc.enable(console=True, data=True)

# OPTIONAL: comment this line if you want CIRCUITPY drive visible
storage.disable_usb_drive()

# OPTIONAL: set default LED off (if present)
try:
    import digitalio
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
except:
    pass
