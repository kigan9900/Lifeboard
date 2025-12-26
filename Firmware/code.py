# 🚀 LIFEBOARD — FULLY WORKING OLED EDITION
# ✅ Clear recognizable icons
# ✅ Volume shows as arrow icon (▲ or ▼) ONLY
# ✅ Fixed AttributeError

import board, time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions import Extension

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Macros())
keyboard.modules.append(Layers())

encoder = EncoderHandler()
keyboard.modules.append(encoder)

keyboard.matrix = KeysScanner(
    pins=[board.A0, board.A1, board.A2, board.A3],
    value_when_pressed=False,
    pull=True,
)

encoder.pins = [(board.D10, board.D9), (board.D7, board.D8)]
encoder.pullups = True
encoder.divisor = 4

def URL(url):
    return KC.MACRO(
        Press(KC.LCTL), Tap(KC.T), Release(KC.LCTL),
        Delay(120), url, Delay(40), Tap(KC.ENTER)
    )

keyboard.keymap = [
    [URL("classroom.google.com"), URL("chat.openai.com"), URL("youtube.com"), URL("drive.google.com")],
    [URL("netflix.com"), URL("spotify.com"), URL("discord.com"), URL("twitch.tv")],
    [URL("hackclub.com"), URL("github.com"), URL("replit.com"), URL("slack.com")],
    [KC.LCTL(KC.K), KC.LCTL(KC.LSFT(KC.F)), KC.LCTL(KC.ENT), KC.LCTL(KC.SLSH)],
    [KC.SPC, KC.X, KC.Z, KC.M],
]

encoder.map = [
    ((KC.DF(4), KC.DF(1)), (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)),
    ((KC.DF(0), KC.DF(2)), (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)),
    ((KC.DF(1), KC.DF(3)), (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)),
    ((KC.DF(2), KC.DF(4)), (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)),
    ((KC.DF(3), KC.DF(0)), (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP)),
]

try:
    import displayio, terminalio
    from adafruit_display_text import label
    from i2cdisplaybus import I2CDisplayBus
    import adafruit_displayio_ssd1306

    displayio.release_displays()
    display = adafruit_displayio_ssd1306.SSD1306(
        I2CDisplayBus(board.I2C(), device_address=0x3C),
        width=128, height=32
    )

    # CLEAR RECOGNIZABLE ICONS - 16x16
    ANIMATED_ICONS = {
        # Layer 0: SCHOOL - Schoolhouse with flag
        0: [
            [
                0b0000001111110000,
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0011111111110000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
            [
                0b0000001111110000,
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0011111111110000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
        ],
        # Layer 1: CHILL - Netflix "N"
        1: [
            [
                0b1110000000001110,
                0b1111000000001110,
                0b1111100000001110,
                0b1110110000001110,
                0b1110011000001110,
                0b1110001100001110,
                0b1110000110001110,
                0b1110000011001110,
                0b1110000001101110,
                0b1110000000111110,
                0b1110000000011110,
                0b1110000000001110,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
            [
                0b1110000000001110,
                0b1111000000001110,
                0b1111100000001110,
                0b1111110000001110,
                0b1110111000001110,
                0b1110011100001110,
                0b1110001110001110,
                0b1110000111001110,
                0b1110000011101110,
                0b1110000001111110,
                0b1110000000111110,
                0b1110000000011110,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
        ],
        # Layer 2: HACKCLUB - Code brackets { }
        2: [
            [
                0b0001100000011000,
                0b0011000000001100,
                0b0110000000000110,
                0b0110000000000110,
                0b0110000000000110,
                0b1100000000000011,
                0b0110000000000110,
                0b0110000000000110,
                0b0110000000000110,
                0b0011000000001100,
                0b0001100000011000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
            [
                0b0011000000001100,
                0b0110000000000110,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1000000000000001,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b0110000000000110,
                0b0011000000001100,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
        ],
        # Layer 3: GITHUB - Folder/files
        3: [
            [
                0b1111111100000000,
                0b1111111111111111,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1111111111111111,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
            [
                0b1111111100000000,
                0b1111111111111111,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1100000000000011,
                0b1111111111111111,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
                0b0000000000000000,
            ],
        ],
        # Layer 4: KSP - Detailed rocket with fins (4 frame countdown)
        4: [
            # T-3: Ready
            [
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0111011111011100,
                0b0111011111011100,
                0b0011111111110000,
                0b0011111111110000,
                0b0111001100011100,
                0b1110000000001110,
                0b0000000000000000,
                0b0000000000000000,
            ],
            # T-2: Pre-ignition
            [
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0111011111011100,
                0b0111011111011100,
                0b0011111111110000,
                0b0011111111110000,
                0b0111001100011100,
                0b1110000000001110,
                0b0100000000000010,
                0b0000000000000000,
            ],
            # T-1: Ignition
            [
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0111011111011100,
                0b0111011111011100,
                0b0011111111110000,
                0b0011111111110000,
                0b0111111111111100,
                0b1111001100011110,
                0b1100000000000110,
                0b0100000000000010,
            ],
            # LIFTOFF: Full thrust!
            [
                0b0000001100000000,
                0b0000011110000000,
                0b0000111111000000,
                0b0001111111100000,
                0b0001111111100000,
                0b0011111111110000,
                0b0011001100110000,
                0b0011001100110000,
                0b0111011111011100,
                0b0111011111011100,
                0b0011111111110000,
                0b0111111111111000,
                0b1111111111111110,
                0b1111011111011110,
                0b1110001100001110,
                0b1000000000000001,
            ],
        ],
    }

    PAGES = [
        ("SCHOOL", "GPT CLS DRV YT"),
        ("CHILL", "SPT NFX TWI DSC"),
        ("HACKCLUB", "GH HC SLK RPL"),
        ("GITHUB", "FND K / RUN"),
        ("KSP", "100% LAUNCH MAP 0%"),
    ]

    class OLED(Extension):
        def __init__(self):
            self.root = displayio.Group()
            display.root_group = self.root

            # Icon (16x16)
            self.icon_bitmap = displayio.Bitmap(16, 16, 2)
            self.icon_palette = displayio.Palette(2)
            self.icon_palette[0] = 0x000000
            self.icon_palette[1] = 0xFFFFFF
            self.icon_grid = displayio.TileGrid(
                self.icon_bitmap, pixel_shader=self.icon_palette, x=2, y=8
            )

            # Particles
            self.particles = []
            for i in range(8):
                p_bitmap = displayio.Bitmap(2, 2, 2)
                p_palette = displayio.Palette(2)
                p_palette[0] = 0x000000
                p_palette[1] = 0xFFFFFF
                p_bitmap[0, 0] = 1
                p_bitmap[1, 0] = 1
                p_bitmap[0, 1] = 1
                p_bitmap[1, 1] = 1
                p_grid = displayio.TileGrid(
                    p_bitmap, pixel_shader=p_palette, x=-10, y=-10
                )
                self.root.append(p_grid)
                self.particles.append({
                    'grid': p_grid, 'active': False, 'x': 0, 'y': 0,
                    'vx': 0, 'vy': 0, 'life': 0
                })

            # Text labels
            self.title = label.Label(
                terminalio.FONT, text="LIFEBOARD", x=22, y=4, scale=1
            )

            # Volume arrow ONLY (no number)
            self.vol_label = label.Label(
                terminalio.FONT, text="", x=112, y=4, scale=1
            )

            self.keys = label.Label(
                terminalio.FONT, text="", x=2, y=28, scale=1
            )

            # Progress bar
            self.prog_bitmap = displayio.Bitmap(60, 2, 2)
            self.prog_palette = displayio.Palette(2)
            self.prog_palette[0] = 0x000000
            self.prog_palette[1] = 0xFFFFFF
            self.prog_grid = displayio.TileGrid(
                self.prog_bitmap, pixel_shader=self.prog_palette, x=22, y=10
            )

            # Add to display
            self.root.append(self.icon_grid)
            self.root.append(self.prog_grid)
            self.root.append(self.title)
            self.root.append(self.vol_label)
            self.root.append(self.keys)

            self.last_layer = None
            self.frame = 0
            self.anim_frame = 0
            self.vol_arrow_timer = 0
            self.last_vol_action = None  # Track last volume action

        def draw_icon(self, icon_data):
            """Draw 16x16 icon"""
            for y in range(16):
                row = icon_data[y]
                for x in range(16):
                    self.icon_bitmap[x, y] = 1 if (row & (1 << (15 - x))) else 0

        def spawn_particles(self, count=5):
            """Spawn particles"""
            import random
            spawned = 0
            for p in self.particles:
                if not p['active'] and spawned < count:
                    p['active'] = True
                    p['x'] = 10.0 + random.uniform(-2, 2)
                    p['y'] = 16.0 + random.uniform(-2, 2)
                    p['vx'] = random.uniform(-2.0, 2.0)
                    p['vy'] = random.uniform(-2.0, 2.0)
                    p['life'] = 25
                    p['grid'].x = int(p['x'])
                    p['grid'].y = int(p['y'])
                    spawned += 1

        def update_particles(self):
            """Update particles"""
            for p in self.particles:
                if p['active']:
                    p['x'] += p['vx']
                    p['y'] += p['vy']
                    p['life'] -= 1
                    if (p['life'] <= 0 or p['x'] < 0 or p['x'] > 128 or
                        p['y'] < 0 or p['y'] > 32):
                        p['active'] = False
                        p['grid'].x = -10
                        p['grid'].y = -10
                    else:
                        p['grid'].x = int(p['x'])
                        p['grid'].y = int(p['y'])

        def check_volume_change(self, keyboard):
            """Check if volume encoder was turned"""
            # Check the actual pressed keys in the matrix
            current_action = None

            # Look through keyboard's active matrix for volume keys
            if hasattr(keyboard, 'hid_pending') and keyboard.hid_pending:
                for key in keyboard.hid_pending:
                    if hasattr(key, 'code'):
                        if key.code == KC.AUDIO_VOL_UP.code:
                            current_action = "UP"
                        elif key.code == KC.AUDIO_VOL_DOWN.code:
                            current_action = "DOWN"

            # Only update if action changed (new press detected)
            if current_action and current_action != self.last_vol_action:
                if current_action == "UP":
                    self.vol_label.text = "▲"
                    self.vol_arrow_timer = 60  # Show for 2 seconds
                    self.spawn_particles(4)
                elif current_action == "DOWN":
                    self.vol_label.text = "▼"
                    self.vol_arrow_timer = 60
                    self.spawn_particles(4)
                self.last_vol_action = current_action
            elif not current_action:
                self.last_vol_action = None

            # Fade out arrow after timer
            if self.vol_arrow_timer > 0:
                self.vol_arrow_timer -= 1
            else:
                self.vol_label.text = ""

        def update_progress_bar(self, layer):
            """Update progress bar"""
            target = int((layer + 1) * 60 / 5)
            for x in range(60):
                for y in range(2):
                    self.prog_bitmap[x, y] = 1 if x <= target else 0

        def boot_sequence(self):
            """Boot animation"""
            for i in range(5):
                self.draw_icon(ANIMATED_ICONS[i][0])
                time.sleep(0.15)
                self.spawn_particles(8)

        def during_bootup(self, keyboard):
            self.boot_sequence()

        def before_matrix_scan(self, keyboard):
            pass

        def after_matrix_scan(self, keyboard):
            layer = keyboard.active_layers[0] if keyboard.active_layers else 0
            layer %= len(PAGES)

            # Layer change
            if layer != self.last_layer:
                self.spawn_particles(10)
                self.title.text = PAGES[layer][0]
                self.keys.text = PAGES[layer][1]
                self.update_progress_bar(layer)
                self.last_layer = layer
                self.anim_frame = 0

            # Animate icon
            self.frame += 1
            anim_speed = 12 if layer == 4 else 20
            if self.frame % anim_speed == 0:
                frames = ANIMATED_ICONS[layer]
                self.anim_frame = (self.anim_frame + 1) % len(frames)
                self.draw_icon(frames[self.anim_frame])

            # Update particles
            if self.frame % 2 == 0:
                self.update_particles()

            # Check volume changes
            self.check_volume_change(keyboard)

            # Icon bounce
            if self.frame % 40 == 0:
                offset = [0, -1, -1, 0][(self.frame // 40) % 4]
                self.icon_grid.y = 8 + offset

        def before_hid_send(self, keyboard):
            pass

        def after_hid_send(self, keyboard):
            pass

        def on_powersave_enable(self, keyboard):
            pass

        def on_powersave_disable(self, keyboard):
            pass

        def on_runtime_enable(self, keyboard):
            pass

        def on_runtime_disable(self, keyboard):
            pass

        def deinit(self, keyboard):
            pass

    keyboard.extensions.append(OLED())

except Exception as e:
    print("OLED disabled:", e)

if __name__ == "__main__":
    keyboard.go()
