from PyQt5 import QtWidgets, uic
from my_py_code.in_up import InUp
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from .internet_and_otp.internet_connection import check_internet
from .internet_and_otp.massage_box import show_internet_messagebox


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.anim2 = None
        self.page_show = None
        self.leftmenu = None
        self.footer = None
        self.anim = None
        self.new_width_leftmenu = None
        self.width_leftmenu = None
        self.v_bool = None
        self.style_button = None
        self.style_button = str(".QPushButton{"
                                "background-color: rgb(218, 218, 218, 0);"
                                "border: none;"
                                "color: #1A6DFF;"
                                "text-align: left;"
                                "font-size: 28px;"
                                "padding: 10px;"
                                "margin:0 0 0 0;"
                                "}"
                                ".QPushButton:hover{"
                                "background-color: rgb(218, 218, 218, 0.2);"
                                "}")
        self.style_button_clicked = str(".QPushButton{"
                                        "background-color: rgb(218, 218, 218);"
                                        "border: none;"
                                        "color: #1A6DFF;"
                                        "text-align: left;"
                                        "font-size: 28px;"
                                        "padding: 10px;"
                                        "margin:0 0 0 0;"
                                        "}"
                                        ".QPushButton:hover{"
                                        "background-color: rgb(218, 218, 218, 0.2);"
                                        "}")
        self.settings = None,
        self.dashboard = None,
        self.news = None,
        self.contact = None
        self.about = None
        self.stars = None
        self.videos = None
        self.lessons = None
        self.home = None
        self.signup = None
        self.signin = None
        self.s_up = None
        self.s_in = None

        self.in_up = InUp()
        uic.loadUi('./gui/mainwindow.ui', self)
        # loadJsonStyle(self)
        self.load_widgets_find()  # find widgets
        self.load_clicked_buttons()  # clicked buttons

        self.resize(500, 500)
        self.show()

    def load_widgets_find(self):
        self.home = self.findChild(QtWidgets.QPushButton, 'home')
        self.lessons = self.findChild(QtWidgets.QPushButton, 'lessons')
        self.videos = self.findChild(QtWidgets.QPushButton, 'videos')
        self.news = self.findChild(QtWidgets.QPushButton, 'news')
        self.signin = self.findChild(QtWidgets.QPushButton, 'signin')
        self.signup = self.findChild(QtWidgets.QPushButton, 'sign_up')
        self.about = self.findChild(QtWidgets.QPushButton, 'about')
        self.contact = self.findChild(QtWidgets.QPushButton, 'contact')
        self.stars = self.findChild(QtWidgets.QPushButton, 'stars')
        self.dashboard = self.findChild(QtWidgets.QPushButton, 'dashboard')
        self.settings = self.findChild(QtWidgets.QPushButton, 'settings')
        self.leftmenu = self.findChild(QtWidgets.QWidget, 'leftmenu')
        self.footer = self.findChild(QtWidgets.QWidget, 'fotter')
        self.page_show = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.page_show.setCurrentIndex(0)

    def load_clicked_buttons(self):
        self.signin.clicked.connect(self.sign_in_window)
        self.signup.clicked.connect(self.sign_up_window)
        self.home.clicked.connect(self.home_window)
        self.lessons.clicked.connect(self.lessons_window)
        self.videos.clicked.connect(self.videos_window)
        self.news.clicked.connect(self.news_window)
        self.about.clicked.connect(self.about_window)
        self.contact.clicked.connect(self.contact_window)
        self.stars.clicked.connect(self.stars_window)
        self.dashboard.clicked.connect(self.dashboard_window)
        self.settings.clicked.connect(self.settings_window)

    def home_window(self):
        self.set_style_button_clicked()
        self.home.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(0)

    def lessons_window(self):
        self.set_style_button_clicked()
        self.lessons.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(3)

    def videos_window(self):
        self.set_style_button_clicked()
        self.videos.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(2)

    def news_window(self):
        self.set_style_button_clicked()
        self.news.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(4)

    def about_window(self):
        self.set_style_button_clicked()
        self.about.setStyleSheet(self.style_button_clicked)

    def contact_window(self):
        self.set_style_button_clicked()
        self.contact.setStyleSheet(self.style_button_clicked)

    def stars_window(self):
        self.set_style_button_clicked()
        self.stars.setStyleSheet(self.style_button_clicked)

    def dashboard_window(self):
        self.width_leftmenu = self.leftmenu.width()
        if self.width_leftmenu == 61:
            self.v_bool = False
            self.new_width_leftmenu = 222
            self.dashboard.setStyleSheet(self.style_button)
        else:
            self.v_bool = True
            self.new_width_leftmenu = 61
            self.dashboard.setStyleSheet(self.style_button_clicked)

        self.anim = QPropertyAnimation(self.leftmenu, b"minimumWidth")
        self.anim.setDuration(500)
        self.anim.setStartValue(self.width_leftmenu)
        self.anim.setEndValue(self.new_width_leftmenu)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.start()
        self.footer.setHidden(self.v_bool)

    def settings_window(self):
        self.set_style_button_clicked()
        self.settings.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(1)

    def sign_in_window(self):
        if check_internet():
            self.set_style_button_clicked()
            self.signin.setStyleSheet(self.style_button_clicked)
            self.s_in = self.in_up.sign_in
            self.s_in.show()
        else:
            show_internet_messagebox()

    def sign_up_window(self):
        if check_internet():
            self.set_style_button_clicked()
            self.signup.setStyleSheet(self.style_button_clicked)
            self.s_up = self.in_up.sign_up
            self.s_up.show()
        else:
            show_internet_messagebox()

    def set_style_button_clicked(self):
        self.home.setStyleSheet(self.style_button)
        self.lessons.setStyleSheet(self.style_button)
        self.videos.setStyleSheet(self.style_button)
        self.news.setStyleSheet(self.style_button)
        self.signin.setStyleSheet(self.style_button)
        self.signup.setStyleSheet(self.style_button)
        self.about.setStyleSheet(self.style_button)
        self.contact.setStyleSheet(self.style_button)
        self.stars.setStyleSheet(self.style_button)
        self.settings.setStyleSheet(self.style_button)