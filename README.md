# Lifeboard :)

[![Downloads](https://img.shields.io/github/downloads/kigan9900/Lifeboard/total)](https://github.com/kigan9900/Lifeboard/releases) [![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/kigan9900/Lifeboard/releases) [![Last Commit](https://img.shields.io/github/last-commit/kigan9900/Lifeboard)](https://github.com/kigan9900/Lifeboard/commits)

Lifeboard is a small micropad that opens apps and websites with one button press. Classroom, YouTube, ChatGPT—whatever you need, instantly. It cuts down setup time and helps you stay focused.

---

## Inspiration

I procrastinate a lot, and I waste more time than I should opening the same apps every day. So I built something that just… does it for me.

If I have something due soon, I can hit a few buttons and instantly open Classroom, ChatGPT, and YouTube. Saves a couple minutes and makes everything smoother.

---

## How it works

- Preset modes controlled by an EC11 rotary encoder (School, Chill, Hackclub, GitHub, etc.)
- One-press multi-app launching
- Small and simple enough to fit anywhere

---

## Code and Animations

This is a **surprise** for you to find once you make it, but there is a mascot and a bunch of icons!

> PS the code is in <ins>KMK</ins> because you can hot swap the binds easier, and because Python's easy

---

## Design

### *The Keys are supposed to be white*

<img width="1970" height="1025" src="https://github.com/user-attachments/assets/152734f7-dc1c-4482-80cf-8e0648a494b4" />

<img width="2066" height="1037" src="https://github.com/user-attachments/assets/bba959f7-bb61-4406-838d-956fe2d76d85" />

<img width="1603" height="784" src="https://github.com/user-attachments/assets/ab8c4d1d-4d04-4b93-962f-018315203cea" />

#### Turn the encoder to switch presets. Press a button to launch whatever you assigned.

---

## Schematic

<img width="800" src="https://github.com/user-attachments/assets/0ce87430-7ea7-489b-ba20-e166d7a3aad3" />

---

## PCB Layout

**PCB Design:**

<img width="1487" height="648" src="https://github.com/user-attachments/assets/e817c978-3194-49e1-9585-61a4f7382682" />

**3D PCB Model:**

<img width="688" height="448" src="https://github.com/user-attachments/assets/e87b5ced-050a-43af-90f7-c2e93f0a26cd" />

---

## 3D Prints

**Top view:**

<img width="2062" height="1050" src="https://github.com/user-attachments/assets/e21452da-9c42-48d9-a631-cb7f9ad7d82b" />

**Bottom view:**

<img width="800" src="https://github.com/user-attachments/assets/a88314f5-86c1-45ad-8a86-36721547021f" />

---

## Bill of Materials (BOM)

- 4× SW_Push — SW_Cherry_MX_1.00u_PCB
- 2× RotaryEncoder — RotaryEncoder_Alps_EC12E-Switch_Vertical_H20mm
- 1× OLED_128x32 — OLED_128x32
- 2× 4.7 kΩ — R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal
- 1× XIAO-RP2040-SMD — XIAO-RP2040-DIP
- 4× Mounting Screws — M3x16mm
