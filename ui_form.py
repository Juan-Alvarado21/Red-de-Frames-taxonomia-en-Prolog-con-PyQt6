# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 900)
        palette = QPalette()
        brush = QBrush(QColor(255, 29, 97, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush1 = QBrush(QColor(138, 180, 248, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush1)
        brush2 = QBrush(QColor(197, 138, 249, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush2)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"img/Poke.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 29, 97);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1000, 900))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 500 11pt \"Roboto\";\n"
"color: rgb(0, 0, 0);")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 20))
        self.label.setStyleSheet(u"font: 900 11pt \"Roboto\";\n"
"color: rgb(0, 0, 0);")
        self.imagen = QLabel(self.tab_1)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setGeometry(QRect(480, 30, 480, 590))
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 275, 91, 20))
        self.label_2.setStyleSheet(u"font: 900 11pt \"Roboto\";\n"
"color: rgb(0, 0, 0);")
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 300, 410, 190))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.propiedades = QLabel(self.frame)
        self.propiedades.setObjectName(u"propiedades")
        self.propiedades.setGeometry(QRect(10, 10, 390, 170))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.propiedades.setFont(font1)
        self.propiedades.setStyleSheet(u"")
        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 500, 91, 20))
        self.label_4.setStyleSheet(u"font: 900 11pt \"Roboto\";\n"
"color: rgb(0, 0, 0);")
        self.frame_2 = QFrame(self.tab_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 530, 410, 90))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.descripcion = QLabel(self.frame_2)
        self.descripcion.setObjectName(u"descripcion")
        self.descripcion.setGeometry(QRect(0, -10, 411, 101))
        self.descripcion.setFont(font)
        self.tree_clases = QTreeWidget(self.tab_1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_clases.setHeaderItem(__qtreewidgetitem)
        self.tree_clases.setObjectName(u"tree_clases")
        self.tree_clases.setGeometry(QRect(10, 30, 410, 230))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.tree_clases.setFont(font2)
        self.tree_clases.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(206, 253, 255);\n"
"font: 12pt \"Roboto\";\n"
"border-radius: 5px;  \n"
"    QTreeWidget::item:pressed {\n"
"        padding-top: 17px;  /* Desplazamiento hacia abajo al presionar */\n"
"        \n"
"	background-color: rgb(224, 27, 36);\n"
"    }\n"
"\n"
"")
        self.tree_clases.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tree_clases.setAnimated(True)
        self.tabWidget.addTab(self.tab_1, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listPropiedades = QListWidget(self.tab_2)
        self.listPropiedades.setObjectName(u"listPropiedades")
        self.listPropiedades.setGeometry(QRect(10, 30, 480, 700))
        self.listPropiedades.setStyleSheet(u"background-color: rgb(206, 253, 255);\n"
"font: 500 15pt \"Roboto\";\n"
"border-radius: 5px")
        self.todasclases = QLabel(self.tab_2)
        self.todasclases.setObjectName(u"todasclases")
        self.todasclases.setGeometry(QRect(530, 0, 450, 700))
        self.todasclases.setStyleSheet(u"font: 300 14pt \"Roboto\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px; \n"
"padding: 20px; \n"
"")
        self.todasclases.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2, icon, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pok\u00e9dex", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Clases:", None))
        self.imagen.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Propiedades:", None))
        self.propiedades.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.descripcion.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Consulta de Clases", None))
        self.todasclases.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"B\u00fasqueda por Propiedades", None))
    # retranslateUi

