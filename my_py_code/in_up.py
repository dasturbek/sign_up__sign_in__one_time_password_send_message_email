from .sign_in import SignIn
from .sign_up import SignUp
from .internet_and_otp.internet_connection import check_internet
from .internet_and_otp.massage_box import show_internet_messagebox


class InUp:
    def __init__(self):
        self.sign_in = SignIn()
        self.sign_up = SignUp()
        self.sign_in.create_acount.clicked.connect(self.up_show)
        self.sign_up.orqaga_2.clicked.connect(self.in_show)

    def up_show(self):
        if check_internet():
            self.sign_up.show()
            self.sign_in.close()
        else:
            show_internet_messagebox()

    def in_show(self):
        if check_internet():
            self.sign_in.show()
            self.sign_up.close()
        else:
            show_internet_messagebox()