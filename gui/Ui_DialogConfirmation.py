# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogConfirmation.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(227, 127)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.dlgBtnOkCancel = QtWidgets.QDialogButtonBox(Dialog)
        self.dlgBtnOkCancel.setGeometry(QtCore.QRect(30, 90, 156, 23))
        self.dlgBtnOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dlgBtnOkCancel.setCenterButtons(True)
        self.dlgBtnOkCancel.setObjectName("dlgBtnOkCancel")
        self.lblDialogConfirm = QtWidgets.QLabel(Dialog)
        self.lblDialogConfirm.setGeometry(QtCore.QRect(10, 20, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDialogConfirm.sizePolicy().hasHeightForWidth())
        self.lblDialogConfirm.setSizePolicy(sizePolicy)
        self.lblDialogConfirm.setObjectName("lblDialogConfirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblDialogConfirm.setText(_translate("Dialog", "Student something successfully!"))
