from asyncore import file_dispatcher, loop
from evdev import InputDevice, categorize, ecodes, events, list_devices
import explorerhat as eh

axismax = 32768
deadzone = 25


def calcRate(raw):
    result = raw * 100 / axismax
    if result < deadzone and result > -deadzone:
        result = 0
    return result


class InputDeviceDispatcher(file_dispatcher):
     #motor1 = 0
     #motor2 = 0

     def __init__(self, device):
         self.device = device
         file_dispatcher.__init__(self, device)

     def recv(self, ign=None):
         return self.device.read()

     def handle_read(self):
         for event in self.recv():
             if event.code == 4:
                 motor1 = event.value
                 motor1 = calcRate(motor1)
                 eh.motor.one.speed(motor1)
             elif event.code == 1:
                 speed = event.value
                 speed = calcRate(speed)
                 speed *= -1
                 eh.motor.two.speed(speed)


#find device
devices = [InputDevice(fn) for fn in list_devices()]
for device in devices:
    if device.name == 'Microsoft X-Box 360 pad':
        dev = InputDevice(device.fn)

InputDeviceDispatcher(dev)
loop()
