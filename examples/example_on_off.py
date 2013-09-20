# -*- coding: utf-8 -*-

import time

from pymailed import MailedManager

if __name__ == "__main__":
    manager = MailedManager()
    mailed = manager.get_mailed()
    mailed.on()
    time.sleep(2)
    mailed.off()
