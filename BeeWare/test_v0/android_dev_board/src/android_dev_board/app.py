"""
Testing Blinkah library with Beeware
"""
import adafruit_blinka
import board
import digitalio

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

led = digitalio.DigitalInOut(board.C0)
led.direction = digitalio.Direction.OUTPUT

class Android_Dev_Board(toga.App):
    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Test Packet: ',
            style=Pack(padding=(0, 5))
        )
        self.test_packet = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.test_packet)

        button = toga.Button(
            'Send Test Packet',
            on_press=self.send_packet,
            style=Pack(padding=5)
        )
        button1 = toga.Button(
            'Toggle GPIO C0',
            on_press=self.toggle_gpio,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(button1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def send_packet(self, widget):
        print(self.test_packet.value)

    def toggle_gpio(self,widget):
        led.value = (not led.value)


def main():
    return Android_Dev_Board()
