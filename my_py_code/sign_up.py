from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from .internet_and_otp.cert_authentication import deshefr


class SignUp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        self.certificate = None
        self.sign_in_up = None
        self.label_2 = None
        self.signUp = None
        self.acount_icon_2 = None
        self.password2 = None
        self.checkBox_2 = None
        self.newparol1 = None
        self.newparol2 = None
        self.password1 = None
        self.email_c = None
        self.ism = None
        self.fam = None
        self.orqaga_2 = None
        self.frame_3 = None
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

        uic.loadUi('./gui/sign_up.ui', self)
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
        self.frame_3 = self.findChild(QtWidgets.QFrame, 'frame_3')

        # button find
        # singup frame button
        self.signUp = self.findChild(QtWidgets.QPushButton, 'signUp')
        self.certificate = self.findChild(QtWidgets.QPushButton, 'certificate')
        self.orqaga_2 = self.findChild(QtWidgets.QPushButton, 'orqaga_2')
        # icon button find
        self.acount_icon_2 = self.findChild(QtWidgets.QPushButton, 'acount_icon_2')  # signUp

        # lineedit find
        # singup frame lineedit
        self.ism = self.findChild(QtWidgets.QLineEdit, 'ism')
        self.fam = self.findChild(QtWidgets.QLineEdit, 'fam')
        self.email_c = self.findChild(QtWidgets.QLineEdit, 'email_c')
        self.password1 = self.findChild(QtWidgets.QLineEdit, 'password1')
        self.password2 = self.findChild(QtWidgets.QLineEdit, 'password2')

        # checkBox find
        self.checkBox_2 = self.findChild(QtWidgets.QCheckBox, 'checkBox_2')  # signup

        # label find
        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')  # signup

    def show_and_hide_frame(self):
        self.certificate.clicked.connect(self.certificate_pass)
        self.checkBox_2.clicked.connect(self.checkbox_2_pass)

        self.ism.textChanged.connect(self.ism_style_editing)
        self.ism.editingFinished.connect(self.ism_style_finish)

        self.fam.textChanged.connect(self.fam_style_editing)
        self.fam.editingFinished.connect(self.fam_style_finish)

        self.email_c.textChanged.connect(self.email_c_style_editing)
        self.email_c.editingFinished.connect(self.email_c_style_finish)

        self.password1.textChanged.connect(self.password1_style_editing)
        self.password1.editingFinished.connect(self.password1_style_finish)

        self.password2.textChanged.connect(self.password2_style_editing)
        self.password2.editingFinished.connect(self.password2_style_finish)

    def certificate_pass(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Json Files (*.json)", options=options)
        infor = deshefr(fileName)
        if infor["open_key"] == "123456" and infor["comp_key"] == "123456":
            self.label_2.setText("Welcome !!!")
        else:
            self.label_2.setText("Goodbye !!!")

    def checkbox_2_pass(self):
        if self.checkBox_2.isChecked():
            self.password1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.password2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.checkBox_2.setText("Parolni yashirish")
        else:
            self.checkBox_2.setText("Parolni ko'rsatish")
            self.password1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.password2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def ism_style_editing(self):
        self.ism.setStyleSheet(self.line_style_edit)

    def ism_style_finish(self):
        self.ism.setStyleSheet(self.line_style_finish)

    def kod_style_editing(self):
        self.kod.setStyleSheet(self.line_style_edit)

    def kod_style_finish(self):
        self.kod.setStyleSheet(self.line_style_finish)

    def fam_style_editing(self):
        self.fam.setStyleSheet(self.line_style_edit)

    def fam_style_finish(self):
        self.fam.setStyleSheet(self.line_style_finish)

    def email_c_style_editing(self):
        self.email_c.setStyleSheet(self.line_style_edit)

    def email_c_style_finish(self):
        self.email_c.setStyleSheet(self.line_style_finish)

    def password1_style_editing(self):
        self.password1.setStyleSheet(self.line_style_edit)

    def password1_style_finish(self):
        self.password1.setStyleSheet(self.line_style_finish)

    def password2_style_editing(self):
        self.password2.setStyleSheet(self.line_style_edit)

    def password2_style_finish(self):
        self.password2.setStyleSheet(self.line_style_finish)