import microcontroller

try:
    if microcontroller.nvm[0:1] != b'\x00':
        microcontroller.nvm[0:1] = b'\x00'
except:
    pass
    
    # this is cause im using the NFC1 pin on the MCUs so i have to unlock them as GPIOs