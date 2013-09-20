# -*- coding: utf-8 -*-

from pymailed import MailedManager

if __name__ == "__main__":
    manager = MailedManager()
    mailed = manager.get_mailed()
    mailed.blink(interval=0.2, times=10)
    mailed.blink()
