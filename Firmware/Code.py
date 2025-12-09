# Lifeboard — KMK Firmware
# 4 shortcuts per preset + 8x8 icons + marquee + mascot
# XIAO RP2040 + 4 switches + 2 EC11 encoders + SSD1306 128x32 OLED

import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import OLED

keyboard = KMKKeyboard()

# -------------------------
# Pins / rows
# -------------------------
keyboard.col_pins = []
keyboard.row_pins = [board.D26, board.D27, board.D28, board.D29]
keyboard.diode_orientation = None

# -------------------------
# Layers / presets
# -------------------------
layers = Layers()
keyboard.modules.append(layers)

L_SCHOOL, L_CHILL, L_HACKCLUB, L_GITHUB = 0, 1, 2, 3
layer_names = ["SCHOOL", "CHILL", "HACKCLUB", "GITHUB"]

# -------------------------
# New-tab URL launcher helper
# -------------------------
def launch(url: str):
    # Open new tab then type URL then Enter
    # Note: send_string accepts strings and KC.* combos; using this pattern used earlier
    return send_string(KC.LCTRL(KC.T), url, KC.ENTER)

# -------------------------
# Action functions (4 per preset)
# -------------------------
# SCHOOL
def google_classroom(): return launch("https://classroom.google.com")
def chatgpt():          return launch("https://chat.openai.com")
def youtube():          return launch("https://youtube.com")
def google_drive():     return launch("https://drive.google.com")

# CHILL
def spotify():          return launch("https://spotify.com")
def reddit():           return launch("https://reddit.com")
def discord():          return launch("https://discord.com")
def netflix():          return launch("https://www.netflix.com")

# HACKCLUB
def hackclub():         return launch("https://hackclub.com")
def makecode():         return launch("https://arcade.makecode.com")
def wokwi():            return launch("https://wokwi.com")
def figma():            return launch("https://www.figma.com")

# GITHUB
def github():           return launch("https://github.com")
def replit():           return launch("https://replit.com")
def git_notify():       return launch("https://github.com/notifications")
def stackoverflow():    return launch("https://stackoverflow.com")

# -------------------------
# Key legends
# -------------------------
key_legends = [
    ["Classroom", "ChatGPT", "YouTube", "Drive"],
    ["Spotify", "Reddit", "Discord", "Netflix"],
    ["Hackclub", "MakeCode", "Wokwi", "Figma"],
    ["GitHub", "Replit", "Notify", "StackOv"],
]

keyboard.keymap = [
    [google_classroom, chatgpt, youtube, google_drive],  # SCHOOL
    [spotify, reddit, discord, netflix],                 # CHILL
    [hackclub, makecode, wokwi, figma],                 # HACKCLUB
    [github, replit, git_notify, stackoverflow],        # GITHUB
]

# -------------------------
# 8x8 Icons (one list per icon)
# Each icon: 8 bytes (MSB = left)
# Simple stylized pixel art placeholders
# -------------------------
ICON_BOOK = [
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10111101,
    0b10000001,
    0b01000010,
    0b00111100
]

ICON_CHAT = [
    0b00111000,
    0b01000100,
    0b10000010,
    0b10100110,
    0b10111110,
    0b10000010,
    0b01000100,
    0b00111000
]

ICON_PLAY = [
    0b00010000,
    0b00111000,
    0b01111100,
    0b11111110,
    0b11111110,
    0b01111100,
    0b00111000,
    0b00010000
]

ICON_DRIVE = [
    0b00100100,
    0b00110100,
    0b00111100,
    0b01111110,
    0b01101110,
    0b01000100,
    0b01000100,
    0b00000000
]

ICON_SPOT = [
    0b00000000,
    0b00111000,
    0b00101000,
    0b00111000,
    0b00000000,
    0b00111000,
    0b00000000,
    0b00000000
]

ICON_REDDIT = [
    0b00000000,
    0b00100100,
    0b01000010,
    0b01011010,
    0b01000010,
    0b00100100,
    0b00000000,
    0b00000000
]

ICON_DISCORD = [
    0b00000000,
    0b01100110,
    0b01000010,
    0b01011010,
    0b01000010,
    0b01100110,
    0b00000000,
    0b00000000
]

ICON_NETFLIX = [
    0b10000010,
    0b11000010,
    0b10100010,
    0b10010010,
    0b10001010,
    0b10000110,
    0b10000010,
    0b00000000
]

ICON_FLAG = [
    0b10000000,
    0b11000000,
    0b11100000,
    0b11110000,
    0b11100000,
    0b11000000,
    0b10000000,
    0b00000000
]

ICON_GAMEPAD = [
    0b00000000,
    0b01111110,
    0b01011010,
    0b01011010,
    0b01011010,
    0b01111110,
    0b00000000,
    0b00000000
]

ICON_CHIP = [
    0b11111111,
    0b10000001,
    0b10100101,
    0b10100101,
    0b10100101,
    0b10000001,
    0b11111111,
    0b00000000
]

ICON_FIGMA = [
    0b01011000,
    0b01011000,
    0b01111100,
    0b01111100,
    0b01011000,
    0b01011000,
    0b00000000,
    0b00000000
]

ICON_OCTO = [
    0b00111000,
    0b01000100,
    0b10011010,
    0b10111110,
    0b10011010,
    0b01000100,
    0b00111000,
    0b00000000
]

ICON_BRACKETS = [
    0b11100000,
    0b11010000,
    0b11001000,
    0b11000100,
    0b11001000,
    0b11010000,
    0b11100000,
    0b00000000
]

ICON_BELL = [
    0b00111000,
    0b01010100,
    0b10000010,
    0b10000010,
    0b10000010,
    0b01000010,
    0b00111100,
    0b00000000
]

ICON_STACK = [
    0b00010000,
    0b00111000,
    0b01111100,
    0b00111000,
    0b00010000,
    0b00000000,
    0b00111100,
    0b00000000
]

ICON_DASH = [
    0b00000000,
    0b00000000,
    0b00000000,
    0b01111110,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000
]

# layer_icons: 4 icons each
layer_icons = [
    [ICON_BOOK, ICON_CHAT, ICON_PLAY, ICON_DRIVE],      # SCHOOL
    [ICON_SPOT, ICON_REDDIT, ICON_DISCORD, ICON_NETFLIX],  # CHILL
    [ICON_FLAG, ICON_GAMEPAD, ICON_CHIP, ICON_FIGMA],   # HACKCLUB
    [ICON_OCTO, ICON_BRACKETS, ICON_BELL, ICON_STACK],  # GITHUB
]

# -------------------------
# OLED + animations
# -------------------------
oled = OLED(i2c=board.I2C(), width=128, height=32, refresh_rate=60)
keyboard.modules.append(oled)

boot_done = False
boot_frame = 0
marquee_text = ""
marquee_x = 0
marquee_active = False

mascot_pos = 0
mascot_dir = 1
mascot_last = time.monotonic()

# draw 8x8 icon helper
def draw_icon(display, x, y, bitmap):
    try:
        for row in range(8):
            byte = bitmap[row]
            for col in range(8):
                if (byte >> (7 - col)) & 1:
                    display.pixel(x + col, y + row, 1)
                else:
                    display.pixel(x + col, y + row, 0)
    except Exception:
        for row in range(8):
            byte = bitmap[row]
            for col in range(8):
                if (byte >> (7 - col)) & 1:
                    try:
                        display.fill_rect(x + col, y + row, 1, 1, 1)
                    except Exception:
                        pass

def start_marquee(text):
    global marquee_text, marquee_x, marquee_active
    marquee_text = text
    marquee_x = 128
    marquee_active = True

def oled_draw(display):
    global boot_done, boot_frame, marquee_active, marquee_x, mascot_pos, mascot_dir, mascot_last

    display.fill(0)

    # boot slide
    if not boot_done:
        x = 128 - boot_frame
        if x < -64:
            boot_done = True
        else:
            try:
                display.text("LIFEBOARD", max(0, x), 10)
            except Exception:
                pass
            display.show()
            boot_frame += 6
            return

    # marquee active?
    if marquee_active:
        try:
            display.text(marquee_text, marquee_x, 0)
        except Exception:
            pass
        marquee_x -= 3
        if marquee_x + (len(marquee_text) * 6) < 0:
            marquee_active = False

    # draw icons + legends
    preset = layers.active_layer
    icons = layer_icons[preset]
    legends = key_legends[preset]

    # positions
    # left column: icons at x=0, text x=12 (keys 1 & 2)
    # right column: icons x=68, text x=80 (keys 3 & 4)
    draw_icon(display, 0, 8, icons[0])
    try:
        display.text("1:" + legends[0], 12, 8)
    except Exception:
        pass

    draw_icon(display, 0, 16, icons[1])
    try:
        display.text("2:" + legends[1], 12, 16)
    except Exception:
        pass

    draw_icon(display, 68, 8, icons[2])
    try:
        display.text("3:" + legends[2], 80, 8)
    except Exception:
        pass

    draw_icon(display, 68, 16, icons[3])
    try:
        display.text("4:" + legends[3], 80, 16)
    except Exception:
        pass

    # draw preset name top-left if not marquee (or keep both)
    if not marquee_active:
        try:
            display.text(layer_names[preset], 0, 0)
        except Exception:
            pass

    # mascot (2x2) bottom
    now = time.monotonic()
    if now - mascot_last > 0.12:
        mascot_last = now
        mascot_pos += mascot_dir
        if mascot_pos <= 0:
            mascot_pos = 0
            mascot_dir = 1
        if mascot_pos >= 120:
            mascot_pos = 120
            mascot_dir = -1

    try:
        display.pixel(mascot_pos, 30, 1)
        display.pixel(mascot_pos+1, 30, 1)
        display.pixel(mascot_pos, 31, 1)
        display.pixel(mascot_pos+1, 31, 1)
    except Exception:
        try:
            display.fill_rect(mascot_pos, 30, 2, 2, 1)
        except Exception:
            pass

    display.show()

oled.display_func = oled_draw

# -------------------------
# Encoders
# left -> presets, right -> volume
# -------------------------
enc = EncoderHandler()
keyboard.modules.append(enc)

enc.pins = ((board.D3, board.D4), (board.D2, board.D1))

def next_mode():
    layers.active_layer = (layers.active_layer + 1) % 4
    start_marquee(layer_names[layers.active_layer])

def prev_mode():
    layers.active_layer = (layers.active_layer - 1) % 4
    start_marquee(layer_names[layers.active_layer])

enc.map = [((lambda: next_mode()), (lambda: prev_mode())), ((KC.VOLU,), (KC.VOLD,))]

# -------------------------
# Start
# -------------------------
if __name__ == "__main__":
    start_marquee(layer_names[layers.active_layer])
    keyboard.go()
