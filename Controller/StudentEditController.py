from PyQt5.QtWidgets import QMainWindow, QDataWidgetMapper

from Entities.Student import Student
from Models.StudentModel import StudentModel
from Views.StudentAddView import StudentAddView
from Views.StudentEditView import StudentEditView


class StudentEditController:

    def __init__(self, main_window):
        self.model: StudentModel = StudentModel()
        self.view: StudentEditView = StudentEditView()
        self.mapper: QDataWidgetMapper = QDataWidgetMapper()
        from main import MainWindow
        self.main_window: MainWindow = main_window
        self.assign_buttons()

    def show(self, s=None):
        i = self.is_selected()
        if i & i >= 0:
            self.mapper.setCurrentIndex(i)
        self.view.show()

    def hide(self, s=None):
        self.view.hide()

    def assign_buttons(self):
        pass

    def is_selected(self, s=None) -> int:
        # print(self.selection_model.hasSelection())
        # print(self.selection_model.isRowSelected(0))
        index = self.main_window.tbl_students.selectionModel().currentIndex().row()

        return index

    def delete_student(self):
        student_id = int(self.view.lineEditStudentID.text())

        self.model.delete_student(student_id)
        self.main_window.refresh_table()

    def update_student(self):
        student_id = int(self.view.lineEditStudentID.text())
        student_name = self.view.lineEditStudentName.text()
        student_grade = self.view.lineEditStudentGrade.text()
        student_age = self.view.lineEditStudentAge.text()

        student = Student(student_name, student_age, student_grade)

        self.model.update_student(student, student_id)
        self.main_window.refresh_table()

    def set_student_editor(self, index=0):
        self.mapper = QDataWidgetMapper()
        self.view.btnEditStudentPrevious.clicked.connect(self.mapper.toPrevious)
        self.view.btnEditStudentNext.clicked.connect(self.mapper.toNext)
        self.view.btnEditStudentSave.clicked.connect(self.update_student)
        self.view.btnEditStudentDelete.clicked.connect(self.delete_student)
        self.mapper.setModel(self.main_window.sql_query_model)
        self.mapper.addMapping(self.view.lineEditStudentID, 0)
        self.mapper.addMapping(self.view.lineEditStudentName, 1)
        self.mapper.addMapping(self.view.lineEditStudentGrade, 2)
        self.mapper.addMapping(self.view.lineEditStudentAge, 3)

        # self.set_student_table(self.model)
        # if index > 0:
        #     self.mapper.setCurrentIndex(index)
        self.mapper.toFirst()