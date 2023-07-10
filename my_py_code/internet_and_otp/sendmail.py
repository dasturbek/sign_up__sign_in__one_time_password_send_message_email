import math
import random
import smtplib
from .internet_connection import check_internet
from datetime import datetime


class OTP:
    send_email = str()

    def __init__(self, email):
        self.send_email = email

    def send_code(self):
        digits = "0123456789"
        one_time_password = ""
        for i in range(6):
            one_time_password += digits[math.floor(random.random() * 10)]
        msg = 'Your OTP Verification for app is ' + one_time_password + ' Note..  Please enter otp within 2 minutes ' \
                                                                        'and 3 attempts, ' \
                                                                        'otherwise it becomes invalid '

        my_email = "dasturbek.com@gmail.com"
        password = "shogofyzxfrbxfmb"
        # &&&&&&&&&&&&- Your mail id. SENDING OTP FROM mail id
        # ************- Your app password. If you do not know how to generate app password for your mail please google.
        if check_internet():
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login(my_email, password)
            s.sendmail(my_email, self.send_email, msg)

            return one_time_password
        else:
            return "no internet"

    def send_code_2(self):
        digits = "0123456789"
        one_time_password = ""
        now_time = datetime.now()
        hour = now_time.hour
        minute = now_time.minute
        second = now_time.second

        for i in range(6):
            one_time_password += digits[math.floor(random.random() * 10)]
        k = int(one_time_password) + hour + minute + second
        one_time_password = str(k)
        msg = 'Your OTP Verification for app is ' + one_time_password + 'Note..  Please enter otp within 2 minutes ' \
                                                                        'and 3 attempts, ' \
                                                                        'otherwise it becomes invalid '

        my_email = "dasturbek.com@gmail.com"
        password = "shogofyzxfrbxfmb"
        # &&&&&&&&&&&&- Your mail id. SENDING OTP FROM mail id
        # ************- Your app password. If you do not know how to generate app password for your mail please google.
        if check_internet():
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login(my_email, password)
            s.sendmail(my_email, self.send_email, msg)

            return one_time_password
        else:
            return "no internet"
