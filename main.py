
from create_table import create_tables
create_tables()
import sys
from PySide6.QtWidgets import QApplication
from dashboard_controller import DashboardController
from login_register_controller import LoginRegisterController



def main():
    app = QApplication(sys.argv)
   
 
    login_register_controller = LoginRegisterController()
    login_register_controller.view.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()