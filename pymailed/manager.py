# -*- coding: utf-8 -*-

import sys
import usb.core

from mailed import Mailed


class MailedManager(object):
    VENDOR = 0x1294
    PRODUCT = 0x1320

    def __init__(self):
        self._load_devices()

    def _load_devices(self):
        self._devices = usb.core.find(find_all=True, idVendor=MailedManager.VENDOR, idProduct=MailedManager.PRODUCT)
        for d in self._devices:
            if d.is_kernel_driver_active(0):
                d.detach_kernel_driver(0)

            d.set_configuration()

    def get_devices(self):
        return self._devices

    def get_device(self, idx=0):
        try:
            return self._devices[idx]
        except IndexError:
            sys.stderr.write("No device with idx:%d found\n" % idx)
            return None

    def get_mailed(self, idx=0):
        device = self.get_device(idx)
        if not device:
            sys.stderr.write("Cannot create mailed\n")
            return None

        return Mailed(device)
