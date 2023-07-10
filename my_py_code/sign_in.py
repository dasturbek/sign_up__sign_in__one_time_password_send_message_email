from PyQt5 import QtWidgets, uic, QtCore
from .internet_and_otp.sendmail import OTP
from .internet_and_otp.internet_connection import check_internet
from .internet_and_otp.massage_box import show_internet_messagebox
from PyQt5.QtCore import QTimer, QDateTime


class SignIn(QtWidgets.QMainWindow):
    def __init__(self):
        self.time_left_int = None
        self.my_qtimer = None

        super(SignIn, self).__init__()
        self.code = None
        self.send_kod = None
        self.text_email_3 = None
        self.sign_up = None
        self.orqaga_3 = None
        self.forgotNext_2 = None
        self.kirish = None
        self.label_3 = None
        self.label = None
        self.signUp = None
        self.email = None
        self.checkBox_3 = None
        self.password = None
        self.kirishForgot = None
        self.acount_icon = None
        self.forgot = None
        self.checkBox = None
        self.newparol1 = None
        self.newparol2 = None
        self.email_3 = None
        self.kod = None
        self.forgotNext_3 = None
        self.orqaga = None
        self.create_acount = None
        self.frame_2 = None
        self.frame_5 = None
        self.line_style_edit = str("height:40px;"
                                   "color: #fff;"
                                   "font-size:20px;"
                                   "margin-bottom:15px;"
                                   "background-color: rgba(1, 57, 44, 0.8);"
                                   "border:none;"
                                   "border-bottom: 2px solid rgba(255, 255, 255);"
                                   "border-top: 1px solid rgba(53, 106, 139, 0.9);"
                                   "border-left: 1px solid rgba(53, 106, 139, 0.9);"
                                   "border-right: 1px solid rgba(53, 106, 139, 0.9);")
        self.line_style_finish = str("height:40px;"
                                     "color: #fff;"
                                     "font-size:20px;"
                                     "margin-bottom:15px;"
                                     "background-color: rgba(1, 57, 44, 0.5);"
                                     "border:none;"
                                     "border-bottom: 2px solid rgb(26, 109, 255);"
                                     "border-top: 1px solid rgba(53, 106, 139, 0.9);"
                                     "border-left: 1px solid rgba(53, 106, 139, 0.9);"
                                     "border-right: 1px solid rgba(53, 106, 139, 0.9);")

        uic.loadUi('./gui/sign_in.ui', self)
        self.centralWidget().setStyleSheet("#centralwidget"
                                           "{"
                                           "background-image: url('./gui/qrc/background.png'); "
                                           "background-repeat: no-repeat;"
                                           "background-position: center"
                                           "}"
                                           )

        self.widgets_find()  # find widgets
        self.show_and_hide_frame()  # frames

        self.resize(500, 500)
        self.move(600, 50)

    def widgets_find(self):
        # frame find
        self.frame_5 = self.findChild(QtWidgets.QFrame, 'frame_5')
        self.frame_2 = self.findChild(QtWidgets.QFrame, 'frame_2')

        # button find
        # kirsh frame button
        self.kirish = self.findChild(QtWidgets.QPushButton, 'kirish')
        self.forgot = self.findChild(QtWidgets.QPushButton, 'forgot')
        self.create_acount = self.findChild(QtWidgets.QPushButton, 'create_acount')
        # forgot frame button
        self.orqaga = self.findChild(QtWidgets.QPushButton, 'orqaga')
        self.orqaga_3 = self.findChild(QtWidgets.QPushButton, 'orqaga_3')
        self.orqaga_3.setHidden(True)
        self.kirishForgot = self.findChild(QtWidgets.QPushButton, 'kirishForgot')
        self.kirishForgot.setHidden(True)
        self.forgotNext_2 = self.findChild(QtWidgets.QPushButton, 'forgotNext_2')
        self.forgotNext_3 = self.findChild(QtWidgets.QPushButton, 'forgotNext_3')
        self.forgotNext_3.setHidden(True)
        # icon button find
        self.acount_icon = self.findChild(QtWidgets.QPushButton, 'acount_icon')  # kirish

        # lineedit find
        # kirsh frame lineedit
        self.email = self.findChild(QtWidgets.QLineEdit, 'email')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password')
        # forgot frame lineedit
        self.email_3 = self.findChild(QtWidgets.QLineEdit, 'email_3')
        self.kod = self.findChild(QtWidgets.QLineEdit, 'kod')
        self.kod.setHidden(True)
        self.newparol1 = self.findChild(QtWidgets.QLineEdit, 'newparol1_2')
        self.newparol1.setHidden(True)
        self.newparol2 = self.findChild(QtWidgets.QLineEdit, 'newparol2')
        self.newparol2.setHidden(True)

        # checkBox find
        self.checkBox = self.findChild(QtWidgets.QCheckBox, 'checkBox')  # kirish
        self.checkBox_3 = self.findChild(QtWidgets.QCheckBox, 'checkBox_3')  # forgot
        self.checkBox_3.setHidden(True)

        # label find
        self.label = self.findChild(QtWidgets.QLabel, 'label')  # kirish
        self.label_3 = self.findChild(QtWidgets.QLabel, 'label_3')  # forgot

    def show_and_hide_frame(self):
        self.sign_in_window_show()  # kirish window show
        self.forgot.clicked.connect(self.forgot_window_show)
        self.orqaga.clicked.connect(self.sign_in_window_show)
        self.checkBox.clicked.connect(self.checkbox_pass)
        self.checkBox_3.clicked.connect(self.checkbox_3_pass)
        self.forgotNext_2.clicked.connect(self.forgot_next_2)
        self.forgotNext_3.clicked.connect(self.forgot_next_3)
        self.orqaga_3.clicked.connect(self.orqaga_email_tah)

        self.email.textChanged.connect(self.email_style_editing)
        self.email.editingFinished.connect(self.email_style_finish)

        self.password.textChanged.connect(self.password_style_editing)
        self.password.editingFinished.connect(self.password_style_finish)

        self.email_3.textChanged.connect(self.email_3_style_editing)
        self.email_3.editingFinished.connect(self.email_3_style_finish)

        self.kod.textChanged.connect(self.kod_style_editing)
        self.kod.editingFinished.connect(self.kod_style_finish)

        self.newparol1.textChanged.connect(self.newparol1_style_editing)
        self.newparol1.editingFinished.connect(self.newparol1_style_finish)

        self.newparol2.textChanged.connect(self.newparol2_style_editing)
        self.newparol2.editingFinished.connect(self.newparol2_style_finish)

    def sign_in_window_show(self):
        self.setWindowTitle('Sign In')
        self.frame_2.setHidden(False)
        self.frame_5.setHidden(True)

    def forgot_window_show(self):
        self.setWindowTitle('Forgot Password')
        self.frame_2.setHidden(True)
        self.frame_5.setHidden(False)

    def checkbox_pass(self):
        if self.checkBox.isChecked():
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.checkBox.setText("Parolni yashirish")
        else:
            self.checkBox.setText("Parolni ko'rsatish")
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def checkbox_3_pass(self):
        if not self.checkBox_3.isChecked():
            self.checkBox_3.setText("Parolni ko'rsatish")
            self.newparol1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.newparol2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
            self.newparol1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.newparol2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.checkBox_3.setText("Parolni yashirish")

    def forgot_next_2(self):
        self.text_email_3 = self.email_3.text()
        if len(self.text_email_3) == 0:
            self.label_3.setText("Fill the field")
        else:
            if check_internet():
                self.send_kod = OTP(self.text_email_3)  # create otp Object
                # self.code = self.send_kod.send_code()
                self.code = self.send_kod.send_code_2()

                self.kod.setHidden(False)
                self.orqaga_3.setHidden(False)
                self.orqaga.setHidden(True)
                self.email_3.setEnabled(False)
                self.label_3.setHidden(True)
                self.forgotNext_2.setHidden(True)
                self.forgotNext_3.setHidden(False)
            else:
                show_internet_messagebox()

    def orqaga_email_tah(self):
        # self.email_3.
        self.kod.setHidden(True)
        self.email_3.setEnabled(True)
        self.label_3.setHidden(False)
        self.label_3.setText('')
        self.orqaga.setHidden(False)
        self.orqaga_3.setHidden(True)
        self.forgotNext_2.setHidden(False)
        self.forgotNext_3.setHidden(True)

    def forgot_next_3(self):
        if check_internet():
            if self.kod.text() == self.code:
                self.email_3.setHidden(True)
                self.orqaga_3.setHidden(True)
                self.orqaga.setHidden(False)
                self.kod.setHidden(True)
                self.label_3.setHidden(True)
                self.newparol1.setHidden(False)
                self.newparol2.setHidden(False)
                self.checkBox_3.setHidden(False)
                self.kirishForgot.setHidden(False)
                self.forgotNext_3.setHidden(True)
            else:
                self.label_3.setText("Parol xato")
                self.label_3.setHidden(False)

        else:
            show_internet_messagebox()

    def timer_start(self):
        self.time_left_int = 6

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_show)
        self.my_qtimer.start(1000)

        self.label_3.setText(str(self.time_left_int))

    def timer_show(self):
        self.time_left_int -= 1

        self.label_3.setText(str(self.time_left_int))
        if self.time_left_int == 0:
            self.send_kod = OTP(self.text_email_3)  # create otp Object
            self.code = self.send_kod.send_code()
            self.my_qtimer.stop()
            self.label_3.setText("Qayta urining")

    # style editing lineedit
    def email_style_editing(self):
        self.email.setStyleSheet(self.line_style_edit)

    def email_style_finish(self):
        self.email.setStyleSheet(self.line_style_finish)

    def password_style_editing(self):
        self.password.setStyleSheet(self.line_style_edit)

    def password_style_finish(self):
        self.password.setStyleSheet(self.line_style_finish)

    def email_3_style_editing(self):
        self.email_3.setStyleSheet(self.line_style_edit)

    def email_3_style_finish(self):
        self.email_3.setStyleSheet(self.line_style_finish)

    def kod_style_editing(self):
        self.kod.setStyleSheet(self.line_style_edit)

    def kod_style_finish(self):
        self.kod.setStyleSheet(self.line_style_finish)

    def newparol1_style_editing(self):
        self.newparol1.setStyleSheet(self.line_style_edit)

    def newparol1_style_finish(self):
        self.newparol1.setStyleSheet(self.line_style_finish)

    def newparol2_style_editing(self):
        self.newparol2.setStyleSheet(self.line_style_edit)

    def newparol2_style_finish(self):
        self.newparol2.setStyleSheet(self.line_style_finish)
