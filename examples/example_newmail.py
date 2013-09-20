# -*- coding: utf-8 -*-

import time
import imaplib
from pymailed import MailedManager

username = ""
password = ""


if __name__ == "__main__":
    manager = MailedManager()
    mailed = manager.get_mailed(0)

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    while True:
        new_mail = mail.search(None, "UnSeen")[1][0]
        if new_mail:
            mailed.on()
        else:
            mailed.off()
        time.sleep(1)
