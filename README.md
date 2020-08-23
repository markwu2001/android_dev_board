# Project Objectives:

The aim of this project is to finally hack the smartphone. Smartphones are powerful, efficient, and highly integrated devices that can add tremendous value to an electronics prototype. Think of starting with a raspberry pi zero, $100 and lots of time later, you finally have your storage, TFT display, hardware inputs, power management, and cloud integration. But all of that is already integrated into the modern smartphone, so why can’t we just use them? Outdated smartphones are becoming faster and faster and are approaching a point where consumers are throwing out powerful computing devices; reusing smartphones opens up doors for AI data processing as hardware trends also point in that direction. Software is not lagging behind with simple python tools being developed such as tensorflow. With this combination of technology, we can bring advanced computational power to beginners and make hardware more financially accessible.
Also this article explains the pain point we are solving: hackaday.com/2018/10/18/ask-hackaday-why-arent-we-hacking-cellphones/

# Requirements:

- A1: Allow the end user to interface in a beginner friendly programming language with lots of community support
- A1.1: End-user language of choice: python
- A1.2: Python shall be able to interact with USB-OTG drivers
- A1.2.1: ChaQuoPy can integrate with Android Studio
- B1: Create hardware that can interface with common sensors
- B1.1: Create hardware that can interface with digital I/O sensors and bus I/O sensors (SPI, I2C)
- B1.2: Hardware shall interface with Android USB-OTG driver
- B1.1.1: FTDI USB-UART -> UART to uC -> peripherals
- B1.1.2: Atmega32u4 ->peripherals
- C1: Create an user-friendly IDE that abstracts underlying integration
- C1.1: Android Studio supplies command line tools for IDE to utilize discreetly
- C2: IDE backend shall support USB-OTG drivers
- C2.1: Android Studio supports USB-OTG-Serial library

# Block Diagram:

Day 3 Goals:
Finalize IDE Backend
Create IDE GUI/ Fake IDE GUI for demonstration purposes
Final Testing and Debugging
Layout and 3D Render Hardware
