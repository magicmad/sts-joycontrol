import evdev

device = evdev.InputDevice('/dev/input/event4')
print(device)

#print (device.capabilities())
#print("\n")

#print(device.capabilities(verbose=True))
#print("\n")

print(device.capabilities(absinfo=True,verbose=True))
#print(device.leds(verbose=True))
print("\n")

#device.leds()

#dev.set_led(ecodes.LED_NUML, 1)  # enable numlock
#dev.set_led(ecodes.LED_NUML, 0)  # disable numlock
