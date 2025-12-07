# Lifeboard :)

[![Downloads](https://img.shields.io/github/downloads/{user}/{repo}/total)](https://github.com/{user}/{repo}/releases)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/{user}/{repo}/releases)
[![Last Commit](https://img.shields.io/github/last-commit/{user}/{repo})](https://github.com/{user}/{repo}/commits)

A **Micropad** with ease-of-life shortcuts that, with the click of a button, instantly opens apps and websites like **Google Classroom**, **YouTube**, and more. Save time, reduce procrastination, and streamline your workflow with a single press.

---

## Inspiration 💡

I often procrastinate on my work and end up completing tasks at the last minute. This made me think: _how can I save even a couple of minutes every day?_

The idea of the **Lifeboard** was born — a customizable board that lets me open multiple important apps or websites with just a few button presses.

For example, if I need to complete an AP World assignment due in an hour, I can press **3 buttons** to open **Google Classroom**, **ChatGPT**, and **YouTube**, cutting down my setup time by almost **2 minutes**. Every second counts!

---

## Features ⚡

- **Preset Modes:** Use the **EC11 Rotary Encoder** to switch between different modes like **School**, **Chill**, **Hackclub**, **GitHub**, etc.
- **Custom Shortcuts:** Map each button to websites, apps, or scripts of your choice.
- **Time-Saving:** Open multiple essential tools with a single button press.
- **Portable Design:** Compact Micropad that fits on any desk setup.

---

## The Full Design 🎨

<img width="800" alt="Lifeboard Design" src="https://github.com/user-attachments/assets/cd962fde-6a7c-4e54-bbd5-7e3b4c520dea" />

The **EC11 Rotary Encoder** on the left allows you to switch between presets. Each preset corresponds to a specific workflow or activity:

- **School:** Google Classroom, ChatGPT, YouTube  
- **Chill:** Music, Netflix, Social Media  
- **Hackclub:** Coding tools, GitHub, Discord  
- **Github:** Repository shortcuts and dev tools  

---

## Schematic 📐

Here’s a screenshot of the Lifeboard schematic:

<img width="800" alt="Lifeboard Schematic" src="https://github.com/user-attachments/assets/0ce87430-7ea7-489b-ba20-e166d7a3aad3" />

---

## PCB Layout 🖥️

Here’s a screenshot of the Lifeboard PCB:

<img width="800" alt="Lifeboard PCB" src="https://github.com/user-attachments/assets/9409af7d-17f9-4205-8673-4005c1dc2197" />

---

## 3D Print – Top View 🖨️

Here’s a top view of the Lifeboard 3D print:

<img width="800" alt="Lifeboard 3D Print Top" src="https://github.com/user-attachments/assets/7bbfccf9-59dd-4ae9-ab0a-0b528fe39ebe" />

---

## 3D Print – Base View 🖨️

Here’s a view of the Lifeboard 3D print from the base:

<img width="800" alt="Lifeboard 3D Print Base" src="https://github.com/user-attachments/assets/a88314f5-86c1-45ad-8a86-36721547021f" />

---

## How It Works ⚙️

1. Select your preset using the **rotary encoder**.  
2. Press the desired button.  
3. The Lifeboard executes your pre-configured shortcut(s).  

Think of it as a **streamlined, one-click productivity booster**.

---

## Bill of Materials (BOM) 📋

| Id | Designator             | Footprint                                    | Quantity | Designation       | Supplier & Ref |
|----|-----------------------|---------------------------------------------|----------|-----------------|----------------|
| 1  | SW3, SW2, SW1, SW4   | SW_Cherry_MX_1.00u_PCB                      | 4        | SW_Push          |                |
| 2  | SW7, SW5              | RotaryEncoder_Alps_EC12E-Switch_Vertical_H20mm | 2        | RotaryEncoder    |                |
| 3  | J1                    | OLED_128x32                                 | 1        | OLED_128x32      |                |
| 4  | R2, R1                | R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | 2        | 4.7 kΩ           |                |
| 5  | U1                    | XIAO-RP2040-DIP                             | 1        | XIAO-RP2040-SMD  |                |
| 6  | Screws                | M5x15mm                                     | 4        | Mounting Screws  |                |

---

## Future Improvements 🚀

- Add **macro recording** for multiple actions per button.  
- Wireless connection support via **Bluetooth**.  
- Custom RGB lighting for different presets.  
- Mobile app integration for dynamic preset control.

---

## Contributing 🤝

Have ideas or want to improve the Lifeboard? Feel free to **fork this repo** and submit a pull request!

---

## License 📄

This project is **MIT licensed** – feel free to use, modify, and share!
