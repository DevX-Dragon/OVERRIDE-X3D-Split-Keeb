import board
import keypad
import adafruit_ble
from adafruit_ble.advertising.standard import Advertisement
from adafruit_ble.services.nordic import UARTService

# Hardware Setup
rows = [board.D11, board.D9, board.D8, board.D7]
cols = [board.D1, board.D2, board.D3, board.D4, board.D5]
keys = keypad.KeyMatrix(rows, cols, columns_to_anodes=False)

ble = adafruit_ble.BLERadio()
uart = UARTService()
advertisement = Advertisement()
advertisement.connectable = True
advertisement.short_name = "XIAO_L"

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        event = keys.events.get()
        if event:
            # Send key index and state (1=pressed, 0=released)
            msg = f"{event.key_number},{int(event.pressed)}\n"
            uart.write(msg.encode("utf-8"))