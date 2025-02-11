from common_imports import *
from common_functions import get_config_value, set_config_value, resource_path
get_db_connection()
set_config_value("user_id", 0)
from create_table import create_tables
from dashboard_controller import DashboardController
from login_register import LoginRegisterUI

class LoginRegisterController(QObject):
    def __init__(self):
        super().__init__()
        self.view = LoginRegisterUI()
        self.setup_connections()
        create_tables()

    def initialize(self):
        self.view = LoginRegisterUI()
        self.setup_connections()

    def setup_connections(self):
        # Connect the switch_page signal to switch between login and register pages
        self.view.switch_page.connect(self.switch_page)
        
        # Connect return press events for login and register
        self.view.login_username.returnPressed.connect(self.handle_login)
        self.view.login_password.returnPressed.connect(self.handle_login)
        self.view.reg_confirm_password.returnPressed.connect(self.handle_registration)

        # Connect login and register buttons
        self.view.login_button.clicked.connect(self.handle_login)
        self.view.register_button.clicked.connect(self.handle_registration)

    @Slot()
    def switch_page(self):
        # The view now handles the page switching internally
        pass

    @Slot()
    def handle_login(self):
        username = self.view.login_username.text()
        password = self.view.login_password.text()

        if not username or not password:
            self.show_message("Error", "Please fill in all fields.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM app_user WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user:
                stored_password = user[2]
                # Check if stored_password is already bytes, if not encode it
                if isinstance(stored_password, str):
                    stored_password = stored_password.encode('utf-8')
                
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    set_config_value("user_id", user[0])
                    # open dashboard
                    self.open_dashboard()
                else:
                    self.show_message("Error", "Invalid username or password.")
            else:
                self.show_message("Error", "Invalid username or password.")
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()

    def open_dashboard(self):
        self.dashboard = DashboardController()
        self.dashboard.view.hide()  # Hide the dashboard initially
        QTimer.singleShot(0, self.show_dashboard)  # Delay showing the dashboard

    def show_dashboard(self):
        # Close old window
        self.view.close()
        
        # Assuming the dashboard controller has a 'view' attribute that is the actual QWidget
        dashboard_widget = self.dashboard.view
        
        # Get the geometry of the main screen
        screen = QApplication.primaryScreen().availableGeometry()
        
        # Get the size of the dashboard window
        dashboard_size = dashboard_widget.sizeHint()
        
        # Calculate the center position
        center_x = (screen.width() - dashboard_size.width()) // 2
        center_y = (screen.height() - dashboard_size.height()) // 2
        
        # Move the dashboard window to the center
        dashboard_widget.move(center_x, center_y)
        
        # Show the dashboard
        dashboard_widget.show()

    @Slot()
    def handle_registration(self):
        username = self.view.reg_username.text()
        email = self.view.reg_email.text()
        first_name = self.view.reg_first_name.text()
        middle_names = self.view.reg_middle_names.text()
        last_name = self.view.reg_last_name.text()
        mobile = self.view.reg_mobile.text()
        password = self.view.reg_password.text()
        confirm_password = self.view.reg_confirm_password.text()

        if not all([username, email, first_name, last_name, password, confirm_password, mobile]):
            self.show_message("Error", "Please fill in all required fields.")
            return

        if password != confirm_password:
            self.show_message("Error", "Passwords do not match.")
            return

        if len(password) < 8:
            self.show_message("Error", "Password must be at least 8 characters long.")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO app_user (username, password, first_name, middle_names, last_name, mobile, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (username, hashed_password, first_name, middle_names, last_name, mobile, email))
            conn.commit()
            self.show_message("Success", "Registration successful!")
            self.view.showLoginPage()  # Switch to login page after successful registration
        except sqlite3.IntegrityError:
            self.show_message("Error", "Username already exists. Please choose a different username.")
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()

    def show_message(self, title, message):
        QMessageBox.information(self.view, title, message)

    def show(self):
        self.view.show()

def main():
    app = QApplication(sys.argv)
    
    # Create main controller and initialize
    controller = LoginRegisterController()
    controller.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()