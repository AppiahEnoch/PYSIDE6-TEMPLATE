from PySide6.QtCore import QObject, Signal

# from topic_management_controller import TopicManagementController


class SidebarController(QObject):
    page_changed = Signal(int)
    
    def __init__(self, view):
        super().__init__()
        self.view = view
        # self.topic_management_controller = TopicManagementController()
        
        self.view.classes_btn.clicked.connect(lambda: self.change_page(0))
        self.view.subjects_btn.clicked.connect(lambda: self.change_page(1))
        self.view.topics_btn.clicked.connect(lambda: self.change_page(2))
        self.view.questions_btn.clicked.connect(lambda: self.change_page(3))
        self.view.import_btn.clicked.connect(lambda: self.change_page(4))
        self.view.quiz_btn.clicked.connect(lambda: self.change_page(5))
        self.view.generated_links_btn.clicked.connect(lambda: self.change_page(6))
        self.view.settings_btn.clicked.connect(lambda: self.change_page(7))
        
        self.view.classes_btn.setChecked(True)
    
    def change_page(self, index):
        self.page_changed.emit(index)
        self.update_button_states(index)
    
    def update_button_states(self, index):
        self.view.classes_btn.setChecked(index == 0)
        self.view.subjects_btn.setChecked(index == 1)
        self.view.topics_btn.setChecked(index == 2)
        self.view.questions_btn.setChecked(index == 3)
        self.view.import_btn.setChecked(index == 4)
        self.view.quiz_btn.setChecked(index == 5)
        self.view.generated_links_btn.setChecked(index == 6)
        self.view.settings_btn.setChecked(index == 7)
    