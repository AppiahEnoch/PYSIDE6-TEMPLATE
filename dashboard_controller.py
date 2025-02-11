
from dashboard_view import DashboardView
from sidebar_controller import SidebarController
# from classes_controller import ClassesController
# from subjects_controller import SubjectsController
# from topic_management_controller import TopicManagementController
# from question_management_controller import QuestionManagementController
# from import_questions_controller import ImportQuestionsController
# from quiz_management_controller import QuestionBankController
# from generated_links_controller import GeneratedLinksController
# from settings_controller import SettingsController




class DashboardController:
    def __init__(self):
   
        self.view = DashboardView()
        self.sidebar_controller = SidebarController(self.view.sidebar)
        
        # self.classes_controller = ClassesController()
        # self.subjects_controller = SubjectsController()
        # self.topic_management_controller = TopicManagementController()
        # self.question_management_controller = QuestionManagementController()
        # self.import_questions_controller = ImportQuestionsController()
        # self.quiz_management_controller = QuestionBankController()
        # self.generated_links_controller = GeneratedLinksController()
        # self.settings_controller = SettingsController()
        
        
        
        # self.view.add_page(self.classes_controller.view)
        # self.view.add_page(self.subjects_controller.view)
        # self.view.add_page(self.topic_management_controller.view)
        # self.view.add_page(self.question_management_controller.view)
        # self.view.add_page(self.import_questions_controller.view)
        # self.view.add_page(self.quiz_management_controller.view)
        # self.view.add_page(self.generated_links_controller.view)
        # self.view.add_page(self.settings_controller.view)
        
        
        self.sidebar_controller.page_changed.connect(self.change_page)
    
    def show(self):
        self.view.show()
    
    def change_page(self, index):
        self.view.set_current_page(index)
        # self.topic_management_controller.update_view()
        # self.question_management_controller.update_view()
        # self.import_questions_controller.update_view()  
        # self.quiz_management_controller.update_view()
        # self.generated_links_controller.update_view()
        # self.settings_controller.update_view()
     