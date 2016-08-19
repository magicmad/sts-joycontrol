from asyncore import file_dispatcher, loop
import evdev

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if device.name == 'Microsoft X-Box 360 pad':
        dev = evdev.InputDevice(device.fn)


#dev = InputDevice('/dev/input/event4')

class InputDeviceDispatcher(file_dispatcher):
     def __init__(self, device):
         self.device = device
         file_dispatcher.__init__(self, device)

     def recv(self, ign=None):
         return self.device.read()

     def handle_read(self):
         for event in self.recv():
             print(repr(event))

InputDeviceDispatcher(dev)
loop()
