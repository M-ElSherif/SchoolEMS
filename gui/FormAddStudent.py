# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAddStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAddStudent(object):
    def setupUi(self, FormAddStudent):
        FormAddStudent.setObjectName("FormAddStudent")
        FormAddStudent.setWindowModality(QtCore.Qt.NonModal)
        FormAddStudent.resize(361, 138)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormAddStudent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayoutAddStudent = QtWidgets.QFormLayout()
        self.formLayoutAddStudent.setObjectName("formLayoutAddStudent")
        self.lblAddStudentName = QtWidgets.QLabel(FormAddStudent)
        self.lblAddStudentName.setObjectName("lblAddStudentName")
        self.formLayoutAddStudent.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblAddStudentName)
        self.lineAddStudentName = QtWidgets.QLineEdit(FormAddStudent)
        self.lineAddStudentName.setObjectName("lineAddStudentName")
        self.formLayoutAddStudent.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineAddStudentName)
        self.lblAddStudentGrade = QtWidgets.QLabel(FormAddStudent)
        self.lblAddStudentGrade.setObjectName("lblAddStudentGrade")
        self.formLayoutAddStudent.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblAddStudentGrade)
        self.lineAddStudentGrade = QtWidgets.QLineEdit(FormAddStudent)
        self.lineAddStudentGrade.setObjectName("lineAddStudentGrade")
        self.formLayoutAddStudent.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineAddStudentGrade)
        self.lineAddStudentAge = QtWidgets.QLineEdit(FormAddStudent)
        self.lineAddStudentAge.setObjectName("lineAddStudentAge")
        self.formLayoutAddStudent.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineAddStudentAge)
        self.lbl = QtWidgets.QLabel(FormAddStudent)
        self.lbl.setObjectName("lbl")
        self.formLayoutAddStudent.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl)
        self.verticalLayout.addLayout(self.formLayoutAddStudent)
        self.horizontalLayoutAddStudent = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAddStudent.setObjectName("horizontalLayoutAddStudent")
        self.btnSaveStudent = QtWidgets.QPushButton(FormAddStudent)
        self.btnSaveStudent.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnSaveStudent.setObjectName("btnSaveStudent")
        self.horizontalLayoutAddStudent.addWidget(self.btnSaveStudent)
        self.btnClearStudent = QtWidgets.QPushButton(FormAddStudent)
        self.btnClearStudent.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnClearStudent.setObjectName("btnClearStudent")
        self.horizontalLayoutAddStudent.addWidget(self.btnClearStudent)
        self.verticalLayout.addLayout(self.horizontalLayoutAddStudent)

        self.retranslateUi(FormAddStudent)
        QtCore.QMetaObject.connectSlotsByName(FormAddStudent)

    def retranslateUi(self, FormAddStudent):
        _translate = QtCore.QCoreApplication.translate
        FormAddStudent.setWindowTitle(_translate("FormAddStudent", "Add Student"))
        self.lblAddStudentName.setText(_translate("FormAddStudent", "Name"))
        self.lblAddStudentGrade.setText(_translate("FormAddStudent", "Grade"))
        self.lbl.setText(_translate("FormAddStudent", "Age"))
        self.btnSaveStudent.setText(_translate("FormAddStudent", "Save"))
        self.btnClearStudent.setText(_translate("FormAddStudent", "Clear"))