from common_imports import *
from sidebar_view import SidebarView

class DashboardView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMART QUESTIONS BANK")
        self.setGeometry(100, 100, 1000, 500)
        self.load_stylesheet()
        self.set_window_icon()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        self.sidebar = SidebarView()
        main_layout.addWidget(self.sidebar)
        
        self.content_stack = QStackedWidget()
        main_layout.addWidget(self.content_stack)
        
        main_layout.setStretchFactor(self.sidebar, 0)
        main_layout.setStretchFactor(self.content_stack, 1)
        
        
        
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
            
    
    def add_page(self, page):
        self.content_stack.addWidget(page)
    
    def load_stylesheet(self):
        try:
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            style_path = os.path.join(base_path, "dashbaord.qss")
            with open(style_path, "r") as style_file:
                self.setStyleSheet(style_file.read())
        except Exception as e:
            print(f"Failed to load the style sheet: {str(e)}")
            
    
    def set_current_page(self, index):
        self.content_stack.setCurrentIndex(index)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = DashboardView()
    view.show()
    sys.exit(app.exec())