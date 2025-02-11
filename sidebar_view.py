# sidebar_view.py
from common_imports import *
import os
import sys

def resource_path(relative_path):
    """
    Get the correct path for resources, works both for development
    and for PyInstaller bundled applications.
    
    Args:
    relative_path (str): The relative path to the resource file.
    
    Returns:
    str: The absolute path to the resource file.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If not running as bundled exe, use the script's directory
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SidebarView(QWidget):
    page_changed = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.setFixedWidth(60)
        self.load_stylesheet()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 10)
        layout.setSpacing(10)
        
        self.classes_btn = self.create_button(resource_path("icons/classes_icon.png"), "Classes")
        self.subjects_btn = self.create_button(resource_path("icons/subjects_icon.png"), "Subjects")
        self.topics_btn = self.create_button(resource_path("icons/topics_icon.png"), "Topics")
        self.questions_btn = self.create_button(resource_path("icons/questions_icon.png"), "Questions")
        self.import_btn = self.create_button(resource_path("icons/import_icon.png"), "Import")
        self.quiz_btn = self.create_button(resource_path("icons/quiz_icon.png"), "Quiz")   
        self.generated_links_btn = self.create_button(resource_path("icons/generated_links_icon.png"), "Links")
        self.settings_btn = self.create_button(resource_path("icons/settings_icon.png"), "Settings")
        
        layout.addWidget(self.classes_btn)
        layout.addWidget(self.subjects_btn)
        layout.addWidget(self.topics_btn)
        layout.addWidget(self.questions_btn)
        layout.addWidget(self.import_btn)
        layout.addWidget(self.quiz_btn)
        layout.addWidget(self.generated_links_btn)
        layout.addWidget(self.settings_btn)
        layout.addStretch()
        
        
        
    def load_stylesheet(self):
        try:
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            style_path = os.path.join(base_path, "sidebar.qss")
            with open(style_path, "r") as style_file:
                self.setStyleSheet(style_file.read())
        except Exception as e:
            print(f"Failed to load the style sheet: {str(e)}")
            
    
    def create_button(self, icon_path, tooltip):
        btn = QPushButton()
        btn.setIcon(QIcon(icon_path))
        btn.setIconSize(QSize(32, 32))
        btn.setCheckable(True)
        btn.setToolTip(tooltip)
        return btn
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SidebarView()
    window.show()
    sys.exit(app.exec_())