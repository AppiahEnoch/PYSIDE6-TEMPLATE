from common_imports import *

class LoginRegisterUI(QWidget):
    switch_page = Signal()

    def __init__(self):
        super().__init__()
        self.login_height = 250
        self.register_height = 450  # Increased height for registration page
        self.initUI()
        self.center_window()

    def initUI(self):
        self.setWindowTitle('APP TITLE')
        self.setFixedWidth(300)
        self.setFixedHeight(self.login_height)  # Start with login height

        self.set_window_icon()
        self.load_stylesheet()

        main_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        # Login Page
        login_widget = QWidget()
        login_layout = QVBoxLayout(login_widget)

        login_layout.addWidget(QLabel('Login'))
        self.login_username = QLineEdit()
        self.login_username.setPlaceholderText('Username')
        login_layout.addWidget(self.login_username)

        self.login_password = QLineEdit()
        self.login_password.setEchoMode(QLineEdit.Password)
        self.login_password.setPlaceholderText('Password')
        login_layout.addWidget(self.login_password)

        self.login_button = QPushButton('Login')
        login_layout.addWidget(self.login_button)

        login_layout.addStretch()

        self.login_switch_label = QLabel('Don\'t have an account? Register')
        self.login_switch_label.setObjectName("switchLink")
        self.login_switch_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_switch_label.mousePressEvent = self.switch_to_register
        login_layout.addWidget(self.login_switch_label, alignment=Qt.AlignCenter)

        # Register Page
        register_widget = QWidget()
        register_layout = QVBoxLayout(register_widget)

        register_layout.addWidget(QLabel('Register'))

        self.reg_email = QLineEdit()
        self.reg_email.setPlaceholderText('Email')
        register_layout.addWidget(self.reg_email)

        self.reg_first_name = QLineEdit()
        self.reg_first_name.setPlaceholderText('First Name')
        register_layout.addWidget(self.reg_first_name)

        self.reg_middle_names = QLineEdit()
        self.reg_middle_names.setPlaceholderText('Middle Names (Optional)')
        register_layout.addWidget(self.reg_middle_names)

        self.reg_last_name = QLineEdit()
        self.reg_last_name.setPlaceholderText('Last Name')
        register_layout.addWidget(self.reg_last_name)

        self.reg_mobile = QLineEdit()
        self.reg_mobile.setPlaceholderText('Mobile')
        register_layout.addWidget(self.reg_mobile)
        
        self.reg_username = QLineEdit()
        self.reg_username.setPlaceholderText('Username')
        register_layout.addWidget(self.reg_username)

        self.reg_password = QLineEdit()
        self.reg_password.setEchoMode(QLineEdit.Password)
        self.reg_password.setPlaceholderText('Password')
        register_layout.addWidget(self.reg_password)

        self.reg_confirm_password = QLineEdit()
        self.reg_confirm_password.setEchoMode(QLineEdit.Password)
        self.reg_confirm_password.setPlaceholderText('Confirm Password')
        register_layout.addWidget(self.reg_confirm_password)

        self.register_button = QPushButton('Register')
        register_layout.addWidget(self.register_button)

        register_layout.addStretch()

        self.register_switch_label = QLabel('Already have an account? Login')
        self.register_switch_label.setObjectName("switchLink")
        self.register_switch_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_switch_label.mousePressEvent = self.switch_to_login
        register_layout.addWidget(self.register_switch_label, alignment=Qt.AlignCenter)

        self.stacked_widget.addWidget(login_widget)
        self.stacked_widget.addWidget(register_widget)

        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

    def set_window_icon(self):
            try:
                if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                    base_path = sys._MEIPASS
                else:
                    base_path = os.path.abspath(".")
                icon_path = os.path.join(base_path, "images", "logo.png")
                
                if os.path.exists(icon_path):
                    app_icon = QIcon(icon_path)
                    self.setWindowIcon(app_icon)
                else:
                    print(f"Icon file not found: {icon_path}")
            except Exception as e:
                print(f"Failed to set window icon: {str(e)}")

    def load_stylesheet(self):
        try:
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            style_path = os.path.join(base_path, "login_style.qss")
            
            with open(style_path, "r") as style_file:
                self.setStyleSheet(style_file.read())
        except Exception as e:
            print(f"Failed to load the style sheet: {str(e)}")



    def showLoginPage(self):
        self.stacked_widget.setCurrentIndex(0)
        self.animateResize(self.login_height)

    def showRegisterPage(self):
        self.stacked_widget.setCurrentIndex(1)
        self.animateResize(self.register_height)

    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, 
                  (screen.height() - size.height()) // 2)

    def switch_to_register(self, event):
        self.switch_page.emit()
        self.showRegisterPage()

    def switch_to_login(self, event):
        self.switch_page.emit()
        self.showLoginPage()

    def animateResize(self, target_height):
        current_height = self.height()
        step = 10 if target_height > current_height else -10
        
        def resize_step():
            nonlocal current_height
            if (step > 0 and current_height < target_height) or (step < 0 and current_height > target_height):
                current_height += step
                self.setFixedHeight(current_height)
                self.center_window()
                QApplication.processEvents()
                QTimer.singleShot(10, resize_step)
            else:
                self.setFixedHeight(target_height)
                self.center_window()

        resize_step()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     login_register_ui = LoginRegisterUI()
#     login_register_ui.show()
#     sys.exit(app.exec())