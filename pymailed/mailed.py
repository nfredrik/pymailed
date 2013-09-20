# -*- coding: utf-8 -*-

import time
import thread
import usb.util


class Mailed(object):
    OFF = 0x00
    ON = 0x01

    def __init__(self, device):
        self._device = device

        config = device.get_active_configuration()
        interface_number = config[(0, 0)].bInterfaceNumber
        alternate_setting = usb.control.get_interface(device, interface_number)
        intf = usb.util.find_descriptor(config, bInterfaceNumber=interface_number, bAlternateSetting=alternate_setting)

        self._ep = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
        assert self._ep, "Endpoint not found"

    def off(self):
        self.set_color(Mailed.OFF)

    def on(self):
        self.set_color(Mailed.ON)

    def blink(self, interval=0.5, times=10):
        for i in range(times):
            self.on()
            time.sleep(interval)
            self.off()
            time.sleep(interval)

    def blink_async(self, interval=0.5, times=10):
        thread.start_new_thread(self.blink, (interval, times))

    def set_color(self, color):
        self._ep.write([color, 0x00, 0x00, 0x00, 0x00])
